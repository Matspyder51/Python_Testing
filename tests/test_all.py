import json

from flask.testing import FlaskClient
from flask.wrappers import Response

import pytest

from server import app, loadClubs, loadCompetitions

clubs = """[
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }
]"""

competitions = """[
    {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    },
    {
        "name": "Winter Land",
        "date": "2022-04-01 21:00:00",
        "numberOfPlaces": "57"
    }
]"""

class Tester:

    def setup_class(self):
        self.clubs = json.loads(clubs)
        self.competitions = json.loads(competitions)

    def test_clubs_loading(self):
        clubs = loadClubs()
        assert self.clubs == clubs

    def test_competitions_loading(self):
        comps = loadCompetitions()
        assert self.competitions == comps

    def test_home(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.get("/")
            assert response.status_code == 200

    def test_summary(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.post("/showSummary", data=dict(email='john@simplylift.co'))#{"email": "john@simplylift.co"}
            assert response.status_code == 200 or response.status_code == 302

    def test_purchase(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.get("/book/Fall Classic/Simply Lift")
            assert response.status_code == 200

    def test_purchase2(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.post("/purchasePlaces", data=dict(club='Simply Lift', competition='Fall Classic', places='10'))
            assert response.status_code == 200

    def test_purchase3(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.post("/purchasePlaces", data=dict(club='Simply Lift', competition='Fall Classic', places='21'))
            assert response.status_code == 200

    def test_board(self):
        with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.get("/board")
            assert response.status_code == 200

    def test_logout(self):
       with app.test_client() as client:
            tempClient: FlaskClient[Response] = client
            response: Response = tempClient.get("/logout")
            assert response.status_code == 302 #Redirect code