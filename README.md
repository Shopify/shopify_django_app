Shopify Django App Example
==========================

This project makes it easy to get a Shopify app up and running with
[Django](https://www.djangoproject.com/) and the
[Python Shopify API](https://github.com/shopify/shopify_python_api).

This project contains
[this example Shopify app](http://shopify-django-example.appspot.com),
which simply displays basic information about the shop's products
and orders. This project contains two django apps, `shopify_app`
which handles authentication (meant to be reusable) and `home`
which contains the example code to demonstrate how to use the API
(meant to be modified or replaced to create your Shopify App).

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

1.  Obtain your applications API Key and Shared Secret, and modify
    `shopify_settings.py` to use these values.

2.  Install the pre-requisites:

    `easy_install Django ShopifyAPI PyYAML pyactiveresource`

3.  Start the server

    `python manage.py runserver`

4.  Visit <http://localhost:8000> to view the example.

Google App Engine
-----------------

1.  [Create an application](https://appengine.google.com/start) with
    Google App Engine, and modify the application line in `app.yaml`
    with the application ID registered with Google App Engine.

2.  Install the [App Engine SDK](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python)

3.  Download and unzip the [pre-configured zip file for App Engine](https://github.com/downloads/shopify/shopify_django_app/shopify_appengine-0.1.1.zip).

    Applications for the App Engine need to be self-contained, so
    the required libraries are included in the zip file along with
    the projects source code.

    To migrate an existing project to App Engine, just copy the
    following directories from zip file to your projects root
    directory:

    * [dateutil](http://pypi.python.org/pypi/python-dateutil)
    * [django](http://www.allbuttonspressed.com/projects/django-nonrel)
    * [djangoappengine](http://www.allbuttonspressed.com/projects/djangoappengine)
    * [djangotoolbox](http://www.allbuttonspressed.com/projects/djangotoolbox)
    * [pyactiveresource](http://pypi.python.org/pypi/pyactiveresource)
    * [shopify](http://pypi.python.org/pypi/ShopifyAPI)

    Or follow the links to download the source code for any of the
    projects, and run `python setup.py build` in the projects root
    directory, then move `build/lib/*` into the root of this project.

4.  Obtain your applications API Key and Shared Secret, and modify
    `shopify_settings.py` to use these values.

5.  Start the server

    `python manage.py runserver`

6.  Visit <http://localhost:8000> to view the example.

7.  When you are ready to deploy your application, update the return
    URL on Shopify to point to your App Engine domain name (e.g.
    https://APPLICATION-ID.appspot.com/login/finalize).

    Then upload the application:

    `appcfg.py update .`

Questions or problems?
----------------------

Read up on the possible API calls:
<http://api.shopify.com>

Talk to new friends:
<http://forums.shopify.com/categories/9>

Edit the docs:
<http://wiki.shopify.com/Shopify_App_Development>
