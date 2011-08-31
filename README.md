Shopify Django App Example
==========================

This package makes it easy to get a Django app up and running with
the [Python Shopify API](https://github.com/shopify/shopify_python_api).

This package contains two django apps, `shopify_app` which contains
handles authentication and `home` which contains an example of how
to use the API. Currently `home` displays basic information about
the shop's products and orders, but is meant to be modifed or
replaced to create your Shopify App.

Requirements
------------

If you don't have an API key yet, create a
[Shopify Partner account](http://shopify.com/partners) and create
an app. You can also create test shops once you're logged in as a
partner.

When you create your app in the Shopify Partner Account, set the return URL to
http://localhost:8000/login/finalize

You can also create a private application that only works for your shop by
visiting https://YOUR-SHOP.myshopify.com/admin/api

Regular Django Application
--------------------------

1. Obtain your applications API Key and Shared Secret, and modify
   `shopify_settings.py` to use these values.

2. Install the pre-requisites:

   `easy_install Django ShopifyAPI PyYAML pyactiveresource`

3. Start the server

   `python manage.py runserver`

4. Visit <http://localhost:8000> to view the example.

Questions or problems?
----------------------

Read up on the possible API calls:
<http://api.shopify.com>

Talk to new friends:
<http://forums.shopify.com/categories/9>

Edit the docs:
<http://wiki.shopify.com/Shopify_App_Development>
