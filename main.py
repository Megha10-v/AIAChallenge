from fastapi import FastAPI
from database import get_all_news, search_news

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def fetch_news():
    """API endpoint to fetch all data."""
    return get_all_news()


@app.get("/search")
def search_news_api(query: str):
    """API endpoint to search data by keyword."""
    return search_news(query)
