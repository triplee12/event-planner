# Event Planner Application

Event Planner is a fastapi application that provides a simple interface for event planning.

## Structuring in Event Planner applications

- planner/
  - apps/
      - __ini__.py
      - main.py
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
