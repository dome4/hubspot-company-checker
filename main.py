import json
import io
from prettytable import PrettyTable

from utils import init


def main():
    hubspotClient = init.initHubspotClient()

    # seach queries
    companies = []

    # read data from file
    file1 = io.open("input.txt", mode="r", encoding="utf-8")
    lines = file1.readlines()
    for line in lines:
        companies.append(line)

    for company in companies:
        checkCompany(hubspotClient, company)


def checkCompany(hubspotClient, searchQuery):

    # create table
    table = PrettyTable()
    table.field_names = ["Search Query", "Company Name", "Hubspot URL"]

    response = findCompanyByName(hubspotClient, searchQuery)

    # response is an array
    for match in response:
        table.add_row([searchQuery, match.get(
            'properties').get('name'), 'https://app.hubspot.com/contacts/6708064/company/' + match.get('id')])

    print(table)


def findCompanyByName(hubspotClient, query):
    payload = {
        'query': query
    }

    headers = {'content-type': 'application/json'}

    # make request
    response = hubspotClient.post(
        'https://api.hubapi.com/crm/v3/objects/companies/search',
        data=json.dumps(payload),
        headers=headers
    )

    # Pretty-print our API result to console
    print('Response from your CRM:')
    print('-----------------------------------------')
    print('status: ' + str(response.status_code))

    return response.json().get("results")


if __name__ == '__main__':
    main()
