from http import HTTPStatus

def test_foo_get_all_should_be_ok(client):
    expectedResult = []
    response = client.get("/api/foo")
    assert response.status_code == HTTPStatus.OK