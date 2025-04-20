import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_posts_by_user(user_id):
    response = requests.get(f"{BASE_URL}/posts?userId={user_id}")
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        assert post["userId"] == user_id


def test_create_post():
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post["id"] == 101
    assert created_post["title"] == "foo"


def test_update_post():
    updated_data = {"title": "updated title"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=updated_data)
    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == "updated title"


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
