from app import *
import requests


def test_about():
	assert about() == "About us: Naser and the cool kids from CS321"


def test_add():
	url = 'http://127.0.0.1:5000/add'
	myobj = {'visitor': 'New person'}

	webpage = requests.post(url, data = myobj)

	assert "New person" in webpage.text