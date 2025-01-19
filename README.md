# Links Shortener Microservice API

**Simple link shortener microservice**

## Stack
- **FastAPI**
- **SQLAlchemy**
- **SQLite + aiosqlite driver**

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/XCraiteX/tiny-link-microservice.git
```

### 2. Replace links in `settings.py`

```bash
# Redirected link when the code is unavailable
DEFAULT_LINK = 'https://google.com'
# Your host link or localhost for tests
SERVICE_LINK = 'http://localhost:8000/lnk/'
```

### 3. Run server

```bash
cd app
uvicorn api:app --port 3400  
```

### 4. Setup nginx 

```nginx
location /lnk/ {
    proxy_pass http://localhost:3400;
    proxy_http_version 1.1;
}
```

### 5. Use your API for your projects
<br>

# Using API

### 1. Create Link | `POST` - `service_link` `/api`

- **Parameters**

```json
{
    "link": "your_link_here" ,
    "limit": 5
}
```
  
> **The limit parameter is optional, but if you specify it, a traffic limit will be imposed on your link   
> (limit - max redirects)**

###  > Response

- Successfull

```json
{
    "status": "OK",
    "shorted": "received_link",
    "views": 6
}
```

- Error

```json
{
    "status": "Error",
    "details": "Invalid link"
}
```