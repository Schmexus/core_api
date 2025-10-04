
def test_get_users(api_client):
    response = api_client.get("users?page=2", headers={"Accept": "application/json", "x-api-key": "reqres-free-v1"})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

# def test_without_api_key(api_client):
#     response = api_client.get("users?page=2", headers={"Accept": "application/json"})
#     print(response.text)
#     assert response.status_code == 401

def test_wrong_EP(api_client):
    response = api_client.get("test/users?page=2", headers={"Accept": "application/json", "x-api-key": "reqres-free-v1"})
    assert response.status_code == 404

def test_post(api_client):
    response = api_client.post("users", headers={"Accept": "application/json", "x-api-key": "reqres-free-v1"}, data={'name': 'John Doe', 'job': 'Developer'})
    assert response.status_code == 200 or response.status_code == 429