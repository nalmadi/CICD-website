from app import *
import requests


website_path = "https://salty-river-43291.herokuapp.com/"
#website_path = "http://127.0.0.1:5000/"

def test_about():
	assert about() == "About us: Naser and the cool kids from CS321"


def test_add():
	url = website_path + '/add'
	myobj = {'visitor': 'New person'}

	webpage = requests.post(url, data = myobj)

	assert "New person" in webpage.text