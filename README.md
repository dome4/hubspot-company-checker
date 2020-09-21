# HubSpot Company Checker

Check if companies already exists in Hubspot

## Prerequisites

To run this quickstart, you'll need:

1. Python 2.6 or greater
2. [pip](https://pypi.python.org/pypi/pip) package management tool - To install OAUTH management packages.
3. A HubSpot Developer Account - To create your app credentials. [Signup for free Developer account here.](https://developers.hubspot.com/get-started?utm_source=khlavka-hubspotquickstartpython&utm_medium=git)
4. A HubSpot CRM Account - To connect with your app. [Signup for a free CRM account here.](https://www.hubspot.com/products/get-started?utm_source=khlavka-hubspotquickstartpython&utm_medium=git)

## Step 1: Create a HubSpot App

1. Open your **Developer Account** and browse to the Apps management page.

> <a href="https://app.hubspot.com/l/developer/applications" target="_blank">Open your Developer App Manager</a> - Select your Developer Account on the next page.

2. Click **Create App**. Give your app a name,
3. From the **Auth** tab, copy your **Client ID** and **Client Secret**. You will need these for Step 3.
4. Leave the **Redirect URL** blank. (Note: Required for using the local server created by the script.)

Now that you have your App Name, Client ID, and Client Secret, you can setup the quickstart on your local machine.

## Step 2: Install required packages via `pip`

1. Run the following command to install the Python packages used for OAUTH: `pip install -r requirements.txt`
2. Update `CLIENT_ID` and `CLIENT_SECRET` with your App's ID and Secret from Step 1.

## Step 3: Run your app

Run your app with the following command:

    $ python main.py

1. If you are running the app for the first time, the app will open your browser and ask to connect to your HubSpot CRM.

> Log in with your user account (if needed) and, if you have multiple CRM accounts, select the account to use with your app.

2. Click the `Grant Access` button.

3. Your app will continue automatically, and you may close the window/tab.

**Done!** Your app will print the API response.
