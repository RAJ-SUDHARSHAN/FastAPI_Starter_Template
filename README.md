# FastAPI Backend with PostgreSQL

This is a starter template for a FastAPI backend application using PostgreSQL as the database. The project includes basic setup for API routing, database connection, and middleware configuration.


## Requirements

- Python 3.8+
- PostgreSQL

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/RAJ-SUDHARSHAN/FastAPI_Starter_Template.git
    cd FastAPI_Starter_Template
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:
    Create a `.env` file in the project root and add the following variable:
    ```
    DATABASE_URL=postgresql://user:password@localhost:port/db_name
    ```

## Running the Application

1. **Start the FastAPI server**:
    ```sh
    uvicorn server:app --reload
    ```

    The application will be available at `http://localhost:8000`.

## Project Files

### `server.py`

The entry point for the FastAPI application. It sets up the application, includes routers, and configures middleware.

### `database/connection.py`

Handles the database connection using SQLAlchemy. It sets up the engine, session, and base model for the database.

### `database/models/test_table.py`

Defines a sample database model `TestTable` using SQLAlchemy.

### `api/v1/test_api.py`

Contains a sample API route to interact with the `TestTable` model.

## Middleware

The project uses `CORSMiddleware` to handle Cross-Origin Resource Sharing (CORS) which allows the backend to interact with the frontend running on a different domain or port.

### Example Usage

To test the sample API, you can use the following endpoint:

- **GET ```/api/v1/test_table```**: Retrieves all entries from the `test_table`.