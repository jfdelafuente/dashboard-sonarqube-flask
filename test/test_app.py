   
from apps import app
import json

def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to my Flask app!' in response.data

def test_result():
    client = app.test_client()
    response = client.post('/result', data=dict(name='Alice', age='25'))
    assert response.status_code == 200
    assert b'Name: Alice' in response.data
    assert b'Age: 25' in response.data