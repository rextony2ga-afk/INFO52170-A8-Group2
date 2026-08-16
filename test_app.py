from app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to Group 2" in response.data


def test_about_page():
    client = app.test_client()
    response = client.get("/about")

    assert response.status_code == 200
    assert b"About Our Cloud Application" in response.data