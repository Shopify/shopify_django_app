Shopify Django App Example
==========================

This package makes it easy to get a Django app up and running with
the [Python Shopify API](https://github.com/shopify/shopify_python_api).

This package contains two django apps, `shopify_app` which contains
handles authentication and `home` which contains an example of how
to use the API. Currently `home` displays basic information about
the shop's products and orders, but is meant to be modified or
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

Google App Engine
-----------------

1. Obtain your applications API Key and Shared Secret, and modify
   `shopify_settings.py` to use these values.

2. [Create an application](https://appengine.google.com/start) with
   Google App Engine, and modify the application line in `app.yaml`
   with the application ID registered with Google App Engine.

3. Install the [App Engine SDK](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python)

3. Install the pre-requisites:

   Applications for the App Engine need to be self-contained, so
   the libraries that are needed need to be installed inside the
   application's directory.

   Download and unzip the following libraries:

   * [python-dateutil](http://pypi.python.org/pypi/python-dateutil)
   * [pyactiveresource](http://pypi.python.org/pypi/pyactiveresource)
   * [ShopifyAPI](http://pypi.python.org/pypi/ShopifyAPI)

   Run `python setup.py build` in each unzipped package, then move
   `build/lib/*` into the root of this example django package.

   Next, download and unzip the
   [django-norel](http://bitbucket.org/twanschik/nonrel-guestbook/downloads/nonrel-guestbook.zip)
   package pre-configured for App Engine. Move the `django`
   `djangoappengine` and `djangotoolbox` directories to the root
   of this example django package.

   For more information, refer to the following references:
   * [Running Pure Django Projects on Google App Engine](http://code.google.com/appengine/articles/django-nonrel.html)
   * [djangoappengine](http://www.allbuttonspressed.com/projects/djangoappengine)

3. Start the server

   `python manage.py runserver`

4. Visit <http://localhost:8000> to view the example.

5. When you are ready to deploy your application, update the return
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
