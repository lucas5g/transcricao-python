import pytest 
import requests
# import tempfile

api = 'http://localhost:5000'

def test_get():
    res = requests.get(api)
    
    assert res.status_code == 200
    
@pytest.mark.only 
def test_post_transcribe():
        
    with open("uploads/olimpiadas.mp4", 'rb') as file:
        files = {"file": file}
        
        res = requests.post(api+'/transcrever', files=files )
    
        assert res.text == 'transcrever file'