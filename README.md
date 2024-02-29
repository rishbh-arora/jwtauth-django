# jwtauth-django

A simple jwt authenticator implemented using Django rest framework and MongoDB and deployed using AWS.

---

### Endpoints

- **POST** /login: Client sends email ID and password to log in. Returns a json containing jwt token and refresh token.<br/>
  Request body template:

  ```
  body: {
      email: johndoe@example.com,
      password: XXXXX
  }
  ```

  <br/>
  Response body template:

  ```
    body: {
        "refresh": "XXXXXXXXXXXX",
        "access":  "XXXXXXXXXXXXX"
    }
  ```

- **POST** /register: Client sends email ID and password. User object created in database. <br/>
  Request body template:

  ```
  body: {
      email: johndoe@example.com,
      password: XXXXX
  }
  ```

   <br/>
  Response body template:

  ```
   body: {
       email: johndoe@example.com,
   }
  ```

### Setup

1. Clone the repository:
   Get the repo locally to setup the developement server by simply running `git clone https://github.com/rishbh-arora/jwtauth-django`

2. Installing dependencies:
   Install all required libraries and dependencies by running `pip install -r requirements.txt`

3. Configuring the environment variables:
   The connection string for the database must be stored in `path/to/base/directory/.env` as `MONGO_CONNETION_STRING=<YOUR_CONNECTION_STRING>`. In this case, the `.env` file should be in the same directory as `manage.py`

4. Create migrations:
   Make migration configurations for all models(database schemas) by running `python manage.py makemigrations`

5. Migrate to database:
   Run the migration using `python manage.py migrate`

6. Start server:
   Finally, start the server on local host using `python manage.py runserver`

```

```
