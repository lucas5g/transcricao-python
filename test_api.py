import pytest
import requests

# import tempfile

api = "http://localhost:5000"


def test_get():
    res = requests.get(api)

    assert res.status_code == 200


def test_post_transcribe():

    with open("uploads/videoTeste.mp4", "rb") as file:
        files = {"file": file}

        res = requests.post(api + "/transcrever", files=files)

        print(res.json()["text"])

        assert (
            res.json()["text"]
            == "rapazes vamos começar a contar uma linda história parece que vai ser uma aventura e tanto diário de bordo fotos músicas e Animação coloque trecho para retrospectiva rico parece que temos um lindo trabalho para fazer vamos fazer uma linda retrospectiva animada é capaz do recruta não sobreviver simbora"
        )

@pytest.mark.only
def test_post_download():

    res = requests.post(
        api + "/download", json={"url": "https://www.youtube.com/shorts/Z7hzcwg0x8I"}
    )
    
    
    print(res)
