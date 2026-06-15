from legacy.breach_matcher import domain_matches
from legacy.breach_matcher import paginate
from legacy.breach_matcher import within_breach_date


def test_domain_matches_is_case_insensitive():
    breach = {
        "Domain": "dropbox.com",
    }

    assert domain_matches(
        breach=breach,
        query="Dropbox",
    ) is True


def test_within_breach_date_includes_end_date():
    breach = {
        "BreachDate": "2019-12-31",
    }

    assert within_breach_date(
        breach=breach,
        date_from="2019-01-01",
        date_to="2019-12-31",
    ) is True


def test_paginate_returns_full_page_size():
    items = [1, 2, 3, 4, 5]

    assert paginate(
        items=items,
        page=1,
        page_size=2,
    ) == [1, 2]
