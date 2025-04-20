import pytest
import requests

BASE_URL = "https://dog.ceo/api"


def test_get_random_dog_image():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "https://images.dog.ceo/breeds/" in response.json()["message"]


@pytest.mark.parametrize("breed", ["hound", "bulldog", "poodle"])
def test_get_breed_images(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)
    assert len(response.json()["message"]) > 0


def test_list_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    breeds = response.json()["message"]
    assert isinstance(breeds, dict)
    assert "bulldog" in breeds
    assert isinstance(breeds["bulldog"], list)


@pytest.mark.parametrize("count", [1, 3, 5])
def test_get_multiple_random_images(count):
    response = requests.get(f"{BASE_URL}/breeds/image/random/{count}")
    assert response.status_code == 200
    images = response.json()["message"]
    assert isinstance(images, list)
    assert len(images) == count


def test_get_sub_breeds():
    response = requests.get(f"{BASE_URL}/breed/hound/list")
    assert response.status_code == 200
    sub_breeds = response.json()["message"]
    assert isinstance(sub_breeds, list)
    assert "afghan" in sub_breeds
