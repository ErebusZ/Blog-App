# Blog-App

## Project Setup

### Creating Environment Files

Before running the project, you need to create two .env files:

1. For the frontend app (in the frontend app's root directory):
   - **File name:** `.env`
   - **Content:**
     ```
     VITE_CORE_API_URL=http://127.0.0.1:8000
     VITE_COMMENT_API_URL=http://127.0.0.1:8001
     ```

2. For Docker Compose (in the project root directory):
   - **File name:** `.env`
   - **Content:**
     ```
     ###>>> backend postgres creds
     SETTINGS_DB_NAME=blog_database
     SETTINGS_DB_USER=django_user
     SETTINGS_DB_PASSWORD=mypassword
     DB_HOST=backend_db
     DB_PORT=5432
     ###<<< backend postgres creds
     
     ###>>> comments postgres creds
     COMMENTS_DB_NAME=blog_database
     COMMENTS_DB_USER=django_user
     COMMENTS_DB_PASSWORD=mypassword
     ###<<< comments postgres creds
     ```

### Running the Project

To run the project using Docker Compose:

- **Command:**
  ```
  docker compose up --build
  ```
- **Description:** This command builds the Docker images (if not already built) and starts the containers defined in your `docker-compose.yml` file.

### Connecting to the Backend Container

To connect to the backend container:

- **Command:**
  ```
  docker compose exec -it backend bash
  ```
- **Description:** This command gives you an interactive bash shell inside the running backend container.

### Applying Migrations

Once connected to the backend container, apply database migrations:

- **Command:**
  ```
  python3.11 manage.py migrate
  ```
- **Description:** This command applies any pending database migrations to set up your database schema.

### Creating a Superuser

To create an admin superuser:

- **Command:**
  ```
  python3.11 manage.py createsuperuser
  ```
- **Description:** This command starts an interactive prompt to create a superuser. You'll be asked to provide a username, email, and password.

# API Documentation

## Blog Post API

### Get Blog Posts

Retrieves blog posts with optional filtering and pagination.

- **URL:** `/articles/blog/`
- **Method:** `GET`
- **Authentication:** Not required
- **Query Parameters:**
  - `search` (optional): Keyword to search in title and content
  - `page` (optional): Page number for pagination (default: 1)
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "data": [
        {
          "id": 1,
          "title": "Sample Blog Post",
          "content": "This is the content of the blog post",
          "author": 1,
          "created_at": "2024-10-01T12:00:00Z",
          "updated_at": "2024-10-01T12:00:00Z"
        }
      ],
      "message": "Success."
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"message": "Invalid page."}`

### Get Single Blog Post

Retrieves a specific blog post by ID.

- **URL:** `/articales/blog/<int:blog_id>/`
- **Method:** `GET`
- **Authentication:** Not required
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "data": {
        "id": 1,
        "title": "Sample Blog Post",
        "content": "This is the content of the blog post",
        "author": 1,
        "created_at": "2024-10-01T12:00:00Z",
        "updated_at": "2024-10-01T12:00:00Z"
      },
      "message": "Success."
    }
    ```
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"error": "Blog post not found."}`

### Create Blog Post

Creates a new blog post.

- **URL:** `/articales/blog/`
- **Method:** `POST`
- **Authentication:** Required
- **Data Params:**
  ```json
  {
    "title": "New Blog Post",
    "content": "This is the content of the new blog post"
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** 
    ```json
    {
      "data": {
        "id": 2,
        "title": "New Blog Post",
        "content": "This is the content of the new blog post",
        "author": 1,
        "created_at": "2024-10-01T13:00:00Z",
        "updated_at": "2024-10-01T13:00:00Z"
      },
      "message": "Success."
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"title": ["This field is required."]}`

### Update Blog Post

Updates an existing blog post.

- **URL:** `/articales/blog/`
- **Method:** `PATCH`
- **Authentication:** Required
- **Data Params:**
  ```json
  {
    "id": 1,
    "title": "Updated Blog Post Title",
    "content": "Updated content of the blog post"
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** 
    ```json
    {
      "data": {
        "id": 1,
        "title": "Updated Blog Post Title",
        "content": "Updated content of the blog post",
        "author": 1,
        "created_at": "2024-10-01T12:00:00Z",
        "updated_at": "2024-10-01T14:00:00Z"
      },
      "message": "Success."
    }
    ```
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "Article not found."}`
  - **Code:** 401
  - **Content:** `{"message": "Unauthorized Action."}`

### Delete Blog Post

Deletes a blog post.

- **URL:** `/articales/blog/`
- **Method:** `DELETE`
- **Authentication:** Required
- **Data Params:**
  ```json
  {
    "id": 1
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** `{"message": "Success."}`
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"message": "Article not found."}`
  - **Code:** 401
  - **Content:** `{"message": "Unauthorized Action."}`

## User Authentication API

### User Registration

Registers a new user.

- **URL:** `/user_portal/signup/`
- **Method:** `POST`
- **Authentication:** Not required
- **Data Params:**
  ```json
  {
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword123"
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** `{"message": "Success"}`
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"username": ["A user with that username already exists."]}`

### User Login

Authenticates a user and returns a JWT token.

- **URL:** `/user_portal/login/`
- **Method:** `POST`
- **Authentication:** Not required
- **Data Params:**
  ```json
  {
    "username": "existinguser",
    "password": "userpassword123"
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"non_field_errors": ["Unable to log in with provided credentials."]}`

### Validate Token

Validates a JWT token (entended to be used by for other services to confirm user identity).

- **URL:** `/user_portal/validate-token/`
- **Method:** `POST`
- **Authentication:** Not required
- **Data Params:**
  ```json
  {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "valid": true,
      "user_id": 1
    }
    ```
- **Error Response:**
  - **Code:** 400
  - **Content:** `{"valid": false, "error": "No token provided"}`
  - **Code:** 401
  - **Content:** `{"valid": false, "error": "Invalid token"}`

## Comments API

### List Comments by Post

Retrieves all comments for a specific post.

- **URL:** `/comments/post/{post_id}`
- **Method:** `GET`
- **Authentication:** Not required
- **URL Parameters:**
  - `post_id`: ID of the post to fetch comments for
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    [
      {
        "id": 1,
        "user_id": 1,
        "post_id": 1,
        "content": "This is a comment"
      },
      {
        "id": 2,
        "user_id": 2,
        "post_id": 1,
        "content": "This is another comment"
      }
    ]
    ```

### Create Comment

Creates a new comment.

- **URL:** `/comment/`
- **Method:** `POST`
- **Authentication:** Required
- **Data Params:**
  ```json
  {
    "user_id": 1,
    "post_id": 1,
    "content": "This is a new comment"
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "id": 3,
      "user_id": 1,
      "post_id": 1,
      "content": "This is a new comment"
    }
    ```
- **Error Response:**
  - **Code:** 401
  - **Content:** `{"detail": "Authentication required"}`
  - **Code:** 403
  - **Content:** `{"detail": "User ID in comment does not match authenticated user"}`

### Update Comment

Updates an existing comment.

- **URL:** `/comment/{comment_id}`
- **Method:** `PUT`
- **Authentication:** Required
- **URL Parameters:**
  - `comment_id`: ID of the comment to update
- **Data Params:**
  ```json
  {
    "content": "This is an updated comment"
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** 
    ```json
    {
      "id": 1,
      "user_id": 1,
      "post_id": 1,
      "content": "This is an updated comment"
    }
    ```
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"detail": "Comment not found"}`
  - **Code:** 403
  - **Content:** `{"detail": "Not authorized to edit this comment"}`
  - **Code:** 403
  - **Content:** `{"detail": "Cannot change the user_id of a comment"}`

### Delete Comment

Deletes an existing comment.

- **URL:** `/comments/{comment_id}`
- **Method:** `DELETE`
- **Authentication:** Required
- **URL Parameters:**
  - `comment_id`: ID of the comment to delete
- **Success Response:**
  - **Code:** 200
  - **Content:** `{"detail": "Comment deleted"}`
- **Error Response:**
  - **Code:** 404
  - **Content:** `{"detail": "Comment not found"}`
  - **Code:** 403
  - **Content:** `{"detail": "Not authorized to delete this comment"}`

## Models

The API uses the following models:

### BlogPost
- `id`: int
- `title`: str
- `content`: str
- `author`: int (user ID)
- `created_at`: datetime
- `updated_at`: datetime

### User
- `id`: int
- `username`: str
- `email`: str
- `password`: str (hashed)

### CommentIn
- `user_id`: int
- `post_id`: int
- `content`: str

### CommentOut
- `id`: int
- `user_id`: int
- `post_id`: int
- `content`: str

### CommentUpdate
- `content`: str (optional)

## Authentication

This API uses token-based authentication. The token should be included in the request headers for authenticated endpoints.

## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of requests. In case of errors, a JSON object with a `detail` or `message` field describing the error is returned.