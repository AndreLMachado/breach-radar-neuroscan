import httpx


HIBP_BREACHES_URL = "https://haveibeenpwned.com/api/v3/breaches"


def fetch_breaches() -> list[dict]:
    response = httpx.get(
        HIBP_BREACHES_URL,
        headers={
            "User-Agent": "breach-radar-neuroscan",
        },
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
