from fastapi import FastAPI

from utils.youtube import youtube_search
from utils.search import google_search
from utils.scolar import scolar_search
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/search")
def search(q: str):
    youtube_res = youtube_search(q)
    google_res = google_search(q)
    scholar_res = scolar_search(q)

    return {"youtube": youtube_res, "google": google_res, "scolar": scholar_res}
