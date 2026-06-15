from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_breaches_returns_list():
    response = client.get(
        "/breaches",
        params={
            "page": 1,
            "page_size": 5,
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_get_breach_by_name_returns_breach():
    response = client.get("/breaches/000webhost")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "000webhost"
    assert data["domain"] == "000webhost.com"


def test_get_breach_by_name_not_found():
    response = client.get("/breaches/not-found-breach")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Breach not found"
    }


def test_get_breaches_filtered_by_domain():
    response = client.get(
        "/breaches",
        params={
            "domain": "000webhost",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "000webhost" in data[0]["domain"]


def test_get_breaches_filtered_by_verified():
    response = client.get(
        "/breaches",
        params={
            "is_verified": True,
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["is_verified"] is True


def test_get_breaches_filtered_by_data_class():
    response = client.get(
        "/breaches",
        params={
            "data_class": "passwords",
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        data_classes = [
            item.lower()
            for item in breach["data_classes"]
        ]

        assert "passwords" in data_classes


def test_get_breaches_filtered_by_min_pwn_count():
    response = client.get(
        "/breaches",
        params={
            "min_pwn_count": 10000000,
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["pwn_count"] >= 10000000


def test_get_breaches_filtered_by_added_date_range():
    response = client.get(
        "/breaches",
        params={
            "added_date_from": "2020-01-01T00:00:00",
            "added_date_to": "2020-12-31T23:59:59",
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["added_date"].startswith("2020")


def test_get_breaches_invalid_page_returns_400():
    response = client.get(
        "/breaches",
        params={
            "page": 0,
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "page must be greater than or equal to 1"
    }


def test_get_breaches_negative_pwn_count_returns_400():
    response = client.get(
        "/breaches",
        params={
            "min_pwn_count": -1,
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "min_pwn_count must be greater than or equal to 0"
    }


def test_get_breaches_pagination():
    first_page = client.get(
        "/breaches",
        params={
            "page": 1,
            "page_size": 2,
        },
    )

    second_page = client.get(
        "/breaches",
        params={
            "page": 2,
            "page_size": 2,
        },
    )

    assert first_page.status_code == 200
    assert second_page.status_code == 200

    first_data = first_page.json()
    second_data = second_page.json()

    assert len(first_data) == 2
    assert len(second_data) == 2

    assert first_data[0]["name"] != second_data[0]["name"]


def test_get_breaches_invalid_page_size_returns_400():
    response = client.get(
        "/breaches",
        params={
            "page_size": 0,
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "page_size must be greater than or equal to 1"
    }


def test_get_breaches_too_large_page_size_returns_400():
    response = client.get(
        "/breaches",
        params={
            "page_size": 101,
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "page_size must be less than or equal to 100"
    }


def test_get_breach_invalid_slug_returns_400():
    response = client.get("/breaches/Adobe;")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid breach name"
    }


def test_get_breach_invalid_slug_with_space_returns_400():
    response = client.get("/breaches/Adobe Test")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid breach name"
    }
