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

