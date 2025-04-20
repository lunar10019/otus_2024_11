import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1"


def test_get_breweries_list():
    response = requests.get(f"{BASE_URL}/breweries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.parametrize("state", ["california", "new_york", "texas"])
def test_get_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}/breweries?by_state={state}")
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        assert state.replace("_", " ").lower() in brewery["state"].lower()


def test_get_single_brewery():
    response = requests.get(f"{BASE_URL}/breweries/10-56-brewing-company-knox")
    assert response.status_code == 200
    brewery = response.json()
    assert brewery["id"] == "10-56-brewing-company-knox"
    assert brewery["name"] == "10-56 Brewing Company"


@pytest.mark.parametrize("per_page", [1, 5, 10])
def test_pagination(per_page):
    response = requests.get(f"{BASE_URL}/breweries?per_page={per_page}")
    assert response.status_code == 200
    assert len(response.json()) == per_page


def test_search_breweries():
    response = requests.get(f"{BASE_URL}/breweries/search?query=dog")
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        assert "dog" in brewery["name"].lower()
