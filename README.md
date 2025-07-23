# Flask JWT Login Example

This project demonstrates a simple Flask backend with JWT-based authentication (login, logout, and protected route) using PyJWT.

## Prerequisites

- Python 3.x
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Running the App

```bash
python app.py
```

The server will start at `http://localhost:5000`.

## API Endpoints

### 1. Login

**POST** `/login`

- **Body (JSON):**
  ```json
  {
    "username": "admin",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "token": "<your_jwt_token>"
  }
  ```

#### Example (curl):
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password123"}'
```

For Windows CMD 
```
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d "{\"username\":\"admin\", \"password\":\"password123\"}"
```

### 2. Access Protected Route

**GET** `/protected`

- **Headers:**
  - `Authorization: <your_jwt_token>`

#### Example (curl):
```bash
curl http://localhost:5000/protected \
  -H "Authorization: <your_jwt_token>"
```

### 3. Logout

**POST** `/logout`

- **Headers:**
  - `Authorization: <your_jwt_token>`

#### Example (curl):
```bash
curl -X POST http://localhost:5000/logout \
  -H "Authorization: <your_jwt_token>"
```

## Testing with Postman or Thunder Client

- Set the request method and URL as above.
- For `/login`, use the Body tab (raw, JSON) to send credentials.
- For `/protected` and `/logout`, add the JWT token to the `Authorization` header.

## Notes
- The user/password is hardcoded as `admin`/`password123` for demo purposes.
- The JWT secret is set in `app.py` as `'your_secret_key_here'`.
- Tokens are blacklisted on logout (in-memory, not persistent). 