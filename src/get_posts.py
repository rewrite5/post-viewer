from typing import List
from requests import get
from get_data import get_data


def get_posts(username: str) -> List:
    ID = get_data(username)["mainEntity"]["identifier"]
    data_total = []
    url = "https://imginn.com/api/posts/"

    querystring = {"id": f"{ID}", "username": f"{username}", "cursor": f"_{ID}"}

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654"
    }

    has_next = True

    while has_next:
        response = get(url, headers=headers, params=querystring, timeout=60)
        data = response.json()
        data_total.append(data)

        has_next = data.get("hasNext", False)

        if has_next:
            querystring["cursor"] = data["cursor"]

    return data_total
