import json

from src.models.constants import OperationKind
from src.models.operations import Operation
from tests.conftest import tmp, LOGGER


request_payload = {
    "date": "2022-09-11",
    "kind": "outcome",
    "amount": 99.9,
    "description": "hamburger"
}


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }


# GET all
def test_all_operation(client):
    response = client.get("/operations/",
                          headers={"kind": "outcome"}
                          )

    assert response.status_code == 200, response.text
    assert "outcome" in response.json()[0].get("kind")


# POST
def test_create_operation(client):
    response = client.post(
        "/operations/",
        json.dumps(request_payload)
    )
    tmp.operation_id = response.json().get("id")

    assert response.status_code == 200, response.text
    assert "id" in response.json()


# GET one
def test_one_operation(client):
    response = client.get("/operations/",
                          headers={"operation_id": str(tmp.operation_id)}
                          )

    assert response.status_code == 200, response.text
    assert "outcome" in response.json()[0].get("kind")


# PUT update
def test_update_operation(client):
    request_payload.update({"description": 'hot dog'})
    response = client.put(f"/operations/{tmp.operation_id}",
                          json.dumps(request_payload)
                          )

    assert response.status_code == 200, response.text
    assert "hot dog" in response.json().get("description")


# DELETE
def test_delete_operation(client):
    response = client.delete(f"/operations/{tmp.operation_id}")
    assert response.status_code == 204, response.text
