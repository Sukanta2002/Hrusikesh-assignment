import os
import requests


def google_search(query):

    url = f"https://www.googleapis.com/customsearch/v1"

    params = {
        "key": os.getenv("GOOGLE_API_KEY"),
        "cx": os.getenv("GOOGLE_CX"),
        "q": query,
        "num": 10,
    }

    response = requests.get(url, params=params)

    res = response.json()

    data = []
    for item in res["items"]:
        data.append(
            {
                "title": item["title"],
                "url": item["link"],
                "snippet": item["snippet"],
            }
        )

    return data
