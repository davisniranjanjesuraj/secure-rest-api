def test_profile(client):
    client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "password123"
    })

    login = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "password123"
    })

    token = login.json["access_token"]

    res = client.get("/api/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200
