from fastapi import FastAPI
from app.routes import router
from app.database import create_db_and_tables
from app.services import simulate_task_processing
import asyncio

app = FastAPI()
app.include_router(router)

@app.on_event('startup')
async def on_startup():
    create_db_and_tables()
    asyncio.create_task(simulate_task_processing())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
