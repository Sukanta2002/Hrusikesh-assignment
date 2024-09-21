import requests
import os


def youtube_search(query):

    url = f"https://www.googleapis.com/youtube/v3/search"

    params = {
        "q": query,
        "key": os.getenv("GOOGLE_API_KEY"),
        "part": "snippet",
        "type": "video",
        "maxResults": 10,
    }

    response = requests.get(url, params=params)

    res = response.json()

    data = []

    for item in res["items"]:
        data.append(
            {
                "id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "thumb_url": item["snippet"]["thumbnails"]["default"]["url"],
                "channel": item["snippet"]["channelTitle"],
                "published_at": item["snippet"]["publishedAt"],
            }
        )

    return data
