from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/sree")

    assert response.status_code == 200

# def test_login():
#     # First create a user
#     register_response = client.post(
#         "/auth/register",
#         json={
#             "email": "testlogin@example.com",
#             "password": "Password123",
#             "role": "patient"
#         }
#     )

#     assert register_response.status_code == 200

#     # Now login
#     login_response = client.post(
#         "/auth/login",
#         json={
#             "email": "testlogin@example.com",
#             "password": "Password123"
#         }
#     )

#     assert login_response.status_code == 200

#     data = login_response.json()

#     assert "access_token" in data
#     assert data["token_type"] == "bearer"    