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
for the next steps.

### Setup Environment

1. Create a `.env` file in the root of your project and add to it the following contents
```
SHOPIFY_API_KEY=[your api key]
SHOPIFY_API_SECRET=[your api secret]
```
2. Generate a secret key and add it to `.env` by running the following in the command line: `printf 'DJANGO_SECRET=' >> .env; python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))' >> .env`

   * For PC Users: Run this command in [GIT Bash](https://git-scm.com/) or [Windows Subsystem For Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Or you can generate a secret key using the Python interpreter and manually add the Django secret key to your `.env` file:
   ```
   python
   import random
   print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))
   exit()
   ```


3. [Optional] you can add to `.env` the api version and api scopes environment variables:

  * `SHOPIFY_API_VERSION` default is `unstable`

  * `SHOPIFY_API_SCOPE` a comma-separated list of scopes, default is `read_products,read_orders`



### Run the App

We use [pipenv](https://github.com/pypa/pipenv) to get running faster. With the
`.env` already created in the root directory, run the app:

```
pipenv install
pipenv run python manage.py runserver
```

You may get warnings about migrations, but they should not stop you.

Open <http://localhost:8000> in your browser to view the example.
