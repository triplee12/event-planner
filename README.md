# Event Planner Application

Event Planner is a fastapi application that provides a simple interface for event planning.

## Structuring in Event Planner applications

- planner/
  - apps/
      - __ini__.py
      - main.py
  - auths/
      - __init__.py
      - authenticate.py
      - jwt_handler.py
      - password_hasher.py
  - models/
      - __init__.py
      - db_connects.py
  - routes/
      - __init__.py
      - events.py
      - users.py
  - schemas/
      - __init__.py
      - events.py
      - users.py

Each file has its function, as stated here:

- Files in the apps folder:
  - main.py: This file will serve as the entry point for events planner applications.
- Files in the auths folder:
  - __init__.py: This file indicates the contents of the folder as a module.
  - authenticate.py: This file will contain the authenticate dependency,
  which will be injected into our routes to enforce authentication and authorization.
  - jwt_handler.py: This file will contain the functions required to encode and decode the JWT strings.
  - password_hasher.py: This file will contain the functions that will be used to encrypt the password of a user during sign-up and compare passwords during sign-in.
- Files in the models folder:
  - db_connect.py: This file will handle the database connection.
- Files in the routes folder:
  - events.py: This file will handle routing operations such as creating, updating,
    and deleting events.
  - users.py: This file will handle routing operations such as the registration and
    signing-in of users.
- Files in the schemas folder:
  - events.py: This file will contain the model definition for events operations.
  - users.py: This file will contain the model definition for user operations.
