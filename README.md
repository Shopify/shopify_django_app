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

When you create your app in the Shopify Partner Account, set the
return URL to "http://localhost:8000/login".

Developing on Nitrous.IO
------------------------

Start hacking on this app on [Nitrous.IO](https://www.nitrous.io/?utm_source=github.com&utm_campaign=shopify_django_app&utm_medium=hackonnitrous) in seconds:

[![Hack shopify/shopify_django_app on
Nitrous.IO](https://d3o0mnbgv6k92a.cloudfront.net/assets/hack-l-v1-3cc067e71372f6045e1949af9d96095b.png)](https://www.nitrous.io/hack_button?source=embed&runtime=django&repo=shopify%2Fshopify_django_app&file_to_open=README.nitrous.md)


Regular Django Application
--------------------------

1.  Obtain your applications API Key and Shared Secret, and modify
    `shopify_settings.py` to use these values. You can also modify
    the permissions that your app needs in this settings file.

2.  Install or upgrade the pre-requisites:

    ```shell
    pip install --upgrade Django ShopifyAPI
    ```

    or

    ```shell
    easy_install -U Django ShopifyAPI
    ```

3.  Create the database

    ```shell
    python manage.py syncdb
    ```

4.  Start the server

    ```shell
    python manage.py runserver
    ```

5.  Visit <http://localhost:8000> to view the example.

Google App Engine
-----------------

1. Applications for the App Engine need to be self-contained, so
   the required libraries need to be included along with the
   projects source code.

   Follow the links to download the source code for these of the
   dependant libraries, and run `python setup.py build` in the
   projects root directory, then move `build/lib/*` into the root
   of this project.
   * [dateutil](http://pypi.python.org/pypi/python-dateutil)
   * [django](http://www.allbuttonspressed.com/projects/django-nonrel)
   * [djangoappengine](http://www.allbuttonspressed.com/projects/djangoappengine)
   * [djangotoolbox](http://www.allbuttonspressed.com/projects/djangotoolbox)
   * [pyactiveresource](http://pypi.python.org/pypi/pyactiveresource)
   * [shopify](http://pypi.python.org/pypi/ShopifyAPI)

2.  [Create an application](https://appengine.google.com/start) with
    Google App Engine, and modify the application line in `app.yaml`
    with the application ID registered with Google App Engine.

3.  Install the [App Engine SDK](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python)

4.  Obtain your applications API Key and Shared Secret, and modify
    `shopify_settings.py` to use these values.

5.  Start the server

    ```shell
    python manage.py runserver
    ```

6.  Visit <http://localhost:8000> to view the example.

7.  When you are ready to deploy your application, update the return
    URL on Shopify to point to your App Engine domain name (e.g.
    https://APPLICATION-ID.appspot.com/login).

    Then upload the application:

    ```shell
    appcfg.py update .
    ```

Questions or problems?
----------------------

Read up on the possible API calls:
<http://api.shopify.com>

Learn how to use the shopify\_python\_api library:
<http://wiki.shopify.com/Using_the_shopify_python_api>

Ask technical questions on Stack Overflow:
<http://stackoverflow.com/questions/tagged/shopify>

Read and edit the wiki on Shopify App Developement:
<http://wiki.shopify.com/Shopify_App_Development>
