# AI-Powered Construction Task Manager

## Setup
1. Create `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the API:
```bash
uvicorn app.main:app --reload
```

## API Endpoints
- POST `/projects/` - Create new project
- GET `/projects/{project_id}` - Get project details
