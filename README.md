# README

Technical test: PokeAPI


Goal: Create a Poke-berries statistics API.


General rules:

- Commit your changes to a public repository in GitHub.

- Add a README.md with instructions to run the code.


Support the following endpoints

````
GET /allBerryStats
````

    Response: {

        "berries_names": [...],

        "min_growth_time": "" // time, int

        "median_growth_time": "", // time, float

        "max_growth_time": "" // time, int

        "variance_growth_time": "" // time, float

        "mean_growth_time": "", // time, float

        "frequency_growth_time": "", // time, {growth_time: frequency, ...}

    }


This endpoint should consume an external API to get the proper info, here

is the documentation page: https://pokeapi.co/docs/v2#berries


- The data must be human-readable.

- Use environment variables for configuration.

- The response must include the content-type header (application/json)

- Functions must be tested with pytest.


For extra points:

- Upload and deploy the solution to a free cloud service like Heroku.

- Use a Python library (example: Matplotlib) to create a Histogram graph and display the image in a plain html. 


Thank you
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

6. Set up environmental variables in a `.env` file. First, run this command to generate a secrete key
    ```bash
    echo "SECRET_KEY=$(openssl rand -base64 32)">.env
    ```
    To enable debug mode for dev purposes run
    ```bash
    echo "DEBUG_VALUE=TRUE">.env
    ```
    To make any further changes edit the `.env.` file directly

7. Launch application using the Heroku CLI. The advantage is that it reads the enviromental variables from the `.env` file
   ```bash 
   heroku local
   ```
   You'll find your server at `http://0.0.0.0:5006/`

8. Alternatively, the application can be run by using the Django `manage.py` script, but it requires that the enviromental variables are set manually
   ```bash
   DEBUG_VALUE=TRUE SECRET_KEY=FHHG python manage.py runserver
   ```
   You'll find your server at `http://127.0.0.1:8000/`
   

## Useful tipsDEBUG_VALUE=TRUE SECRET_KEY=FHHG python manage.py runserver

1. [Install sqliteBrowser](https://sqlitebrowser.org/dl/#linux) for a quick peek into database
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