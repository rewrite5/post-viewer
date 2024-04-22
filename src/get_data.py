# from bs4 import BeautifulSoup
# from requests import get
# from json import loads


# def get_data_from_username(username: str) -> str:
#     try:
#         url = f"https://imginn.com/{username}"
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654"
#         }
#         response = get(url, headers=headers, timeout=60)

#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             script_tag = (
#                 soup.find("script", type="application/ld+json")
#                 .text.replace("\n", "")
#                 .replace("\r", "")
#             )

#             data = loads(script_tag)
#             return data
#         elif response.status_code == 404:
#             return "User not found"
#         else:
#             return "Error in the request"
#     except Exception as e:
#         return str(e)


# from bs4 import BeautifulSoup
# from requests import get
# from json import loads
# from typing import Union


# def get_data_from_username(username: str) -> Union[str, dict]:
#     try:
#         url = f"https://imginn.com/{username}"
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654"
#         }
#         response = get(url, headers=headers, timeout=60)

#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "html.parser")
#             script_tag = (
#                 soup.find("script", type="application/ld+json")
#                 .text.replace("\n", "")
#                 .replace("\r", "")
#             )

#             data = loads(script_tag)
#             return data
#         elif response.status_code == 404:
#             return "User not found"
#         else:
#             return "Error in the request"
#     except Exception as e:
#         return str(e)


import httpx
from bs4 import BeautifulSoup
from json import loads
from typing import Union


async def get_data_from_username(username: str) -> Union[str, dict]:
    try:
        url = f"https://imginn.com/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=60)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = (
                soup.find("script", type="application/ld+json")
                .text.replace("\n", "")
                .replace("\r", "")
            )

            data = loads(script_tag)
            return data
        elif response.status_code == 404:
            return "Usuario no encontrado"
        else:
            return "Error en la solicitud"
    except Exception as e:
        return str(e)
