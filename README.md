# README

This application is a simple API that 

## Installation
1. Install [Python3](https://www.python.org/downloads/).

2. Activate the virtual environment by running this command on your command line 
    ``` bash
    source env/bin/activate
    ```

3.  Install the required packages. These packages are listed in the `requirements.txt` and can be installed with `PIP` by running this command
    ```bash
    python -m pip install -r requirements.txt
    ``` 

4. Initialize the database by running
   ```bash
   python manage.py migrate
    ```

5. Start a local django server by running
   ```bash 
   python manage.py runserver
   ```

## Useful tips

1. [Install sqliteBrowser] (https://sqlitebrowser.org/dl/#linux) for a quick peek into database
2. Use Django [Admin console](http://127.0.0.1:8000/admin/). Read more at [part 2 of Djando Tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#introducing-the-django-admin) to setup the admin console users
3. Use interactive shell with Django
    ```bash
    python manage.py shell
    ```
    Now you can interact with models by importing them on the interactive shell
    ```python
    from GlobantPokeBerries.models import pokeBerry
    ```
    And also with the services
    ```python
    import GlobantPokeBerries.services as services
    ```
    Read more [in here](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api)