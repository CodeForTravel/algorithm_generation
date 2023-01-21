# Algorithm Generation Assesment task

### Project setup

- Clone the repository: https://github.com/CodeForTravel/algorithm_generation.git

  ```bash
  git clone https://github.com/CodeForTravel/algorithm_generation.git
  ```

- Create a **.env** file inside the project directory and copy from **env_example** to **.env** and set the environment variables according to the needs.

  Such as, set your local `postgres` user name and password to the DB_USER and DB_PASSWORD:

  ```bash
  # example
  DB_NAME=example_db
  DB_USER=postgres
  DB_PASSWORD=admin1234
  DB_PORT=5432
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
  python manage.py runserver
  ```

- Project APIs: Postman api collections link, here you will find the APIs created for this project

```bash
  https://www.postman.com/collections/49feeffba81a96b99c92
```

### Makefile

- Delete `.pyc` files with the command:

  ```bash
  make clean
  ```
