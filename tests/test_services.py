import pytest

from app.services import generate_construction_tasks
from unittest.mock import patch


@patch('google.generativeai.GenerativeModel')
def test_task_generation_success(mock_model):
    mock_response = type('obj', (object,), {'text': '''1. Site preparation
    2. Foundation pouring
    3. Structural framing'''})
    mock_model.return_value.generate_content.return_value = mock_response
    
    tasks = generate_construction_tasks("House", "Seattle")
    assert all(t['status'] == 'pending' for t in tasks)
