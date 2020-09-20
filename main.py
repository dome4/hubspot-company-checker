import json

from utils import init


def main():
    hubspotClient = init.initHubspotClient()

    # Call the 'Get all contacts' API endpoint
    response = hubspotClient.get(
        'https://api.hubapi.com/contacts/v1/lists/all/contacts/all',
        params={'count': 1}  # Return only 1 result -- for demo purposes
    )

    # Pretty-print our API result to console
    print('Here is one Contact Record from your CRM:')
    print('-----------------------------------------')
    print(json.dumps(response.json(), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
