# coffee_restful
Complete Flask Restful API with PostgreSQL DB.

## Overview
Project to share information about local coffee shops using serialization with marshmallow to convert complex objects into server-side JSON data. Endpoints include /api for GET all requests, and /api:\<name\> for GET, POST, PUT, and DELETE requests. Server is secured using JWT authentication, will be adding bcrypt for password hashing.
  
## Setup
1. main
2. models
3. auth
4. app.py
5. security.py

## How To Run
Clone repo and startup virtual environment using venv. Use the command -->>

```bash
  source venv/bin/activate
```

Next, install nesseary dependencies found in <code>requirements.txt</code>, and create an <code>.env</code> file with constants for listing PORT=7000 or any desired PORT. To use this API setup, navigate the directory so that it contains the <code>app.py</code> file. Once, this has been satisfied run -->>

```python
  python app.py
```

This command will start the server on localhost.
