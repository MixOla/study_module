from http import client

import pytest

@pytest.mark.django_db
def test_module_create(get_auth_client, module_factory):
    module = module_factory()

    data = {
        "category": category.pk,
        "title": "test goal",
    }


    response = client.post(
        "/modules/create/",
        data=data,
        content_type="application/json",
    )

    expected_response = {
        "id": response.data["id"],
        "title": "test goal",
        "category": category.id,
        "description": None,
        "due_date": None,
        "status": 1,
        "priority": 2,
        "created": response.data["created"],
        "updated": response.data["updated"],
    }

    assert response.status_code == 201
    assert response.data == expected_response