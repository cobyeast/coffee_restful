# coffee_restful
CRUD Flask Restful API with PostgreSQL DB.

## Overview
Project to share information about local coffee shops using serialization with marshmallow to convert complex objects into server-side JSON data. Server is secured using JWT authentication, inculding usernames, and hashed passwords with bcrypt.

Endpoints have three different params: items, users, and auth. Item paths include: /api/items for GET all requests, and /api/items:\<name\> for GET, POST, PUT, and DELETE requests. For users, paths include: /api/users for GET all requests, and /api/users:\<id\> for GET, PUT, and DELETE requests. For auth, paths include: /api/auth/register for POST requests, and lastly /api/auth/login for GET, and POST requests.

Note: the path /auth has been reserved for serverside JWT authentication. 
  
## Folder Setup
1. main
2. models
3. routes
4. auth
5. app.py
6. security.py
7. middleware
8. env

## How To Run
1. Clone this repo and create a virtual environment using the command in the bash shell -->>

```bash
  python3 -m venv env
```

Next you can run the virtual environment in bash using -->>

```bash
  source env/bin/activate
```

2. Install all necessary dependencies found in <code>requirements.txt</code>. You will also need to create an <code>.env</code> file with constants like variables PORT=8000 or alter 8000 to any desired PORT number, ADMIN=YOURUSERNAME, PASSWORD=YOURPASSWORD, and also inculde your PostgreSQL URI using variable POSTGRESQL_URI=YOURURI. At the end, it should look something like this -->>

```env
PORT=8000
ADMIN=YOURUSERNAME
SECRET_KEY=SECRETSTRING
PASSWORD=YOURPASSWORD
POSTGRESQL_URI=YOURURI
```

Note: Postgres URI is often broken down in the following format postgresql://[USERNAME]:[PASSWORD]@localhost/[DATABASE]. I am using coffeedb as my database, for this specific project.

3. In order to create tables with Postgres run the bash command -->>

```bash
  python
```

In the python terminal run the following commands to create the item and user table.

```python
from config import db
db.create_all()
exit()
```

4. Navigate the directory so that it contains the <code>app.py</code> file. Once, this has been satisfied run -->>

```python
  python app.py
```

Running this command will start the server on http://localhost:8000/.
