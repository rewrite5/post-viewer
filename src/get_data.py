from bs4 import BeautifulSoup
from requests import get
from json import loads


def get_data(username: str) -> str:
    url = f"https://imginn.com/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654"
    }
    response = get(url, headers=headers, timeout=60)

    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = (
        soup.find("script", type="application/ld+json")
        .text.replace("\n", "")
        .replace("\r", "")
    )

    data = loads(script_tag)
    return data
