# coffee_restful
Complete Flask Restful API with PostgreSQL DB.

## Overview
Project to share information about local coffee shops using serialization with marshmallow to convert complex objects into server-side JSON data. Endpoints include /api for GET all requests, and /api:\<name\> for GET, POST, PUT, and DELETE requests. Server is secured using JWT authentication, inculding usernames, and hashed passwords with bcrypt.
  
## Setup
1. main
2. models
3. auth
4. app.py
5. security.py

## How To Run
1. Clone repo and startup virtual environment using venv. Use the command -->>

```bash
  source venv/bin/activate
```

2. Install all necessary dependencies found in <code>requirements.txt</code>. You will also need to create an <code>.env</code> file with constants like variables PORT=7000 or alter 7000 to any desired PORT number, ADMIN=YOURUSERNAME, PASSWORD=YOURPASSWORD, and also inculde your PostgreSQL URI using variable POSTGRESQL_URI=YOURURI.

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

This command will start the server on http://localhost:7000/.
