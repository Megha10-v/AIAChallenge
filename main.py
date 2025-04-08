from fastapi import FastAPI
from database import get_all_news, search_news

app = FastAPI()

@app.get("/data")
def fetch_news():
    """API endpoint to fetch all news articles."""
    return {"articles": get_all_news()}

@app.get("/data")
def search_news_api(query: str):
    """API endpoint to search data by keyword."""
    return {"results": search_news(query)}
