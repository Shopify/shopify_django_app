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

1. Copy over the `.env.local` file into a `.env` file and fill out the `SHOPIFY_API_KEY` and `SHOPIFY_API_SECRET` fields
```
cp .env.local .env
```

2. Generate a secret key and fill out the `DJANGO_SECRET` value in `.env` file by running the following in the terminal 

Open the python interpreter:
```
python or python3
```
Inside the python interpreter, generate the secret key, copy it, and exit:

```python
>>> import random
>>> print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))
>>> exit()

```
Or use the command below in your terminal. Copy and paste the output into the value of `DJANGO_SECRET` in .env

```
python3 -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))' >> .env
```


**For Windows Users:** Run this command in [GIT Bash](https://git-scm.com/) or [Windows Subsystem For Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Alternatively, you can generate a secret key using the Python interpreter. This requires you to manually add the Django secret key to your `.env` file by doing the following:

**[For Windows OS]:** Use ```python``` instead of  ```python3``` in CMD



3. [Optional] you can add the api version and api scopes environment variables to the `.env` file:

  * `SHOPIFY_API_VERSION` default is `unstable`

  * `SHOPIFY_API_SCOPE` a comma-separated list of scopes, default is `read_products,read_orders`

### Manual Setup [Optional] 

4. Create virtual environment

For Linux and macOS

```
python3 -m venv virtual         # 'virtual' can be any name/term
```


5. Activate the virtual environment

For Linux and macOS 
```
. virtual/bin/activate
```
or 
```
source virtual/bin/activate
```

For windows
```
source virtual\Scripts\activate

```

6. Install dependencies
```
pip install -r requirements.txt
```

7. Apply Migrations
```
python3 manage.py migrate
```

8. Run the app
```
python3 manage.py runserver
```



### Run the App

We use [pipenv](https://github.com/pypa/pipenv) to get running faster. With the
`.env` already created in the root directory, run the app:

```
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

Open <http://localhost:8000> in your browser to view the example.
