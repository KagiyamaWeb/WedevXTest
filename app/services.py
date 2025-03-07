import os
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from app.database import get_db, SessionLocal
from app.models import models  # Import models

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-pro')

def generate_construction_tasks(project_name: str, location: str) -> list:
    prompt = f'''Generate a detailed construction task list for building a {project_name} in {location}.
    Include only construction-related tasks. Return as a comma-separated list.'''
    
    response = model.generate_content(prompt)
    tasks = [task.strip() for task in response.text.split(',') if task.strip()]
    return [{'name': task, 'status': 'pending'} for task in tasks]

async def simulate_task_processing():
    while True:
        await asyncio.sleep(10)  # Process tasks every 10 seconds
        db = SessionLocal()
        try:
            # Get first pending project
            project = db.query(models.Project).filter(
                models.Project.status.notin_(['completed', 'failed'])
            ).first()
            
            if project:
                try:
                    # Update project status
                    project.status = 'in_progress'
                    db.commit()
                    
                    # Complete random task
                    pending_tasks = [t for t in project.tasks if t.status == 'pending']
                    if pending_tasks:
                        task = pending_tasks[0]
                        task.status = 'completed'
                        db.commit()
                        
                        # Mark project as completed if all tasks done
                        if all(t.status == 'completed' for t in project.tasks):
                            project.status = 'completed'
                            db.commit()
                    
                except Exception as e:
                    db.rollback()
                    project.status = 'failed'
                    db.commit()
        finally:
            db.close()
