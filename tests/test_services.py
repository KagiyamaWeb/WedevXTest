from app.services import generate_construction_tasks
from unittest.mock import patch
import pytest

@patch('google.generativeai.GenerativeModel')
def test_task_generation_success(mock_model):
    mock_response = type('obj', (object,), {'text': 'Site survey, Obtain permits, Hire contractors'})
    mock_model.return_value.generate_content.return_value = mock_response
    
    tasks = generate_construction_tasks('Office', 'London')
    assert len(tasks) == 3
    assert all(t['status'] == 'pending' for t in tasks)

@patch('google.generativeai.GenerativeModel')
def test_task_generation_failure(mock_model):
    mock_model.return_value.generate_content.side_effect = Exception('API Error')
    
    with pytest.raises(Exception):
        generate_construction_tasks('Office', 'London')
