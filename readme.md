# Algorithm Generation Assesment task

### Project setup

- Clone the repository: https://github.com/CodeForTravel/test_assesment.git

  ```bash
  git clone https://github.com/CodeForTravel/test_assesment.git
  ```

- Create a **.env** file inside the project directory and copy from **env_example** to **.env** and set the environment variables according to the needs.

  Such as, set your local `postgres` user name and password to the DB_USER and DB_PASSWORD:

  ```bash
  # example
  DB_NAME=example_db
  DB_USER=postgres
  DB_PASSWORD=admin1234
  DB_PORT=5432
  WEATHER_API_URL=https://api.openweathermap.org/data/2.5/weather
  WEATHER_API_KEY=49611bbd929ed98af4fcfb28gfdf48f8d32
  LONGITUDE=90
  LATITUDE=24
  ```

- Create an account in **https://openweathermap.org/** get the API_KEY and set is to .env file:

  ```bash
  WEATHER_API_KEY=your_weather_api_key
  ```

- Create a virtual environment named **env** with Python's **venv**:

  ```bash
  python3 -m venv env
  ```

  - Activate the virtual environment (For Ubuntu):
    ```bash
    source env/bin/activate
    ```
  - For Windows:
    ```bash
    env\Scripts\activate
    ```

- Install all required packages:

  ```bash
  pip install -r requirements.txt
  ```

- Install redis server, if dont'n have in your machine yet. It will need for django-huey

  ```bash
  sudo apt-get install redis-server
  ```

- Run **migrate** command to propagate the migrations files into the db

  ```bash
  python manage.py migrate
  ```

- Create admin account, By default user will be admin user

  ```
  python manage.py createsuperuser
  ```

- Run Django server

  ```bash
  python manage.py runserver ip_address:port
  ```

- Run Django huey server: It will run the tasks scheduler

  ```bash
  python manage.py run_huey
  ```

- fetch the current weather:
  Note: This system will fetch the current weather after every 10 minutes, and it will store the current weather data to constance. So that we can use this data to recommand product to user based on current weather.

- Project APIs: Postman api collections link, here you will find the APIs created for this project

```bash
  https://www.postman.com/collections/49feeffba81a96b99c92
```

### Makefile

- Delete `.pyc` files with the command:

  ```bash
  make clean
  ```
