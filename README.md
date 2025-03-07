# AI-Powered Construction Task Manager

## Features
- Dynamic task generation using Gemini Pro
- Project lifecycle management
- Automatic task progression simulation
- SQLite database storage

## System Architecture
```
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│   FastAPI     │◄─────►│  SQLAlchemy   │◄─────►│  SQLite DB    │
│   Endpoints   │       │    ORM        │       │               │
└───────────────┘       └───────────────┘       └───────────────┘
       ▲
       │
       ▼
┌───────────────┐
│ Gemini Pro API│
└───────────────┘

## API Documentation

### Create Project
```http
POST /projects/
Content-Type: application/json

{
  "project_name": "Hospital",
  "location": "New York"
}
```

Response:
```json
{
  "id": 1,
  "project_name": "Hospital",
  "location": "New York",
  "status": "processing",
  "tasks": [
    {"name": "Site Survey", "status": "pending"},
    {"name": "Permit Acquisition", "status": "pending"}
  ]
}
```

### Get Project Status
```http
GET /projects/1
```

Response:
```json
{
  "id": 1,
  "project_name": "Hospital",
  "location": "New York",
  "status": "in_progress",
  "tasks": [
    {"name": "Site Survey", "status": "completed"},
    {"name": "Permit Acquisition", "status": "pending"}
  ]
}
```

## Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run with hot reload
uvicorn app.main:app --reload

# Run tests
pytest tests/
