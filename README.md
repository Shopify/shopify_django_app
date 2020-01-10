Shopify Django App Example
==========================

This project makes it easy to get a Shopify app up and running with
[Django](https://www.djangoproject.com/) and the
[Python Shopify API](https://github.com/shopify/shopify_python_api).

This project  simply displays basic information about the shop's products
and orders. 

This project has the following structure
- `shopify_app` an app which handles authentication (meant to be reusable) 
- `home` an app which contains the example code to demonstrate how to use the API (meant to be modified or replaced to create your Shopify App).
- `shopify_django_app` project files for serving this app.


Requirements
------------
This was built and tested with

- python 3.6.5
- django 3.0.2
- shopifyapi 5.1.2

Get It Running
--------------

### Create Your App Configuration
- Log in to your [partners dashboard](https://partners.shopify.com/)
- Navigate to [your apps](https://partners.shopify.com/current/apps)
- Click `Create App`
- Choose a custom app or public app
- Fill in the app name
- Set the Application Url http://localhost:8000/
- Set Whitelisted redirection URL( http://localhost:8000/shopify/finalize/

You will then have access to your API key and API secret KEY, you will need these
for the next steps

### Run the App

Run the following command in the repo (remember to be using the correct python and dependencies)
```
SHOPIFY_API_KEY=[key] SHOPIFY_API_SECRET=[secret] python manage.py runserver
```

You may get warnings about migrations, but they should not stop you.

Open <http://localhost:8000> in your browser to view the example.
