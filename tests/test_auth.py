def test_register(client):
    res = client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "password123"
    })
    assert res.status_code == 201


def test_login(client):
    client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "password123"
    })

    res = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "password123"
    })

    assert res.status_code == 200
    assert "access_token" in res.json
