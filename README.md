## Overview

This project comprises three main components:

1. **Web Scraper (`scrapper.py`)**: A Python script that extracts data from specified website. I have used BeautifulSoup module to scrap data from website (https://www.artificialintelligence-news.com/) and I am storing the data scraped from website to PostgreSQL database.
2. **API Service (`main.py`)**: Provides endpoints to access the scraped data.
3. **Database Operations (`database.py`)**: PostgreSQL database is used.




## Installation

### Prerequisites

- Python 3.6 or higher
- pip
- PostgreSQL Database


### Setup Steps

1. **Clone the Repository**:

   ```
   https://github.com/Megha10-v/AIAChallenge.git
   ```

2. **Navigate to the Project Directory**:
   ```
   cd AIAChallenge/
   ```

3. **Create and Activate a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the web scarpper

To execute the scraper and collect data and store it in database:
```
python scrapper.py
```

### Starting the API Service

Launch the API server with:
```
uvicorn main:app --reload
```
The API will be accessible at http://localhost:8000/docs.

### API Endpoints
The API provides the following endpoints:

- GET /data : Retrieve all the data from the tabe
- GET /search?query=news : Retrieve the data based on keyword(here news included data is retrieved) from the table
  

## Live API Link 

https://aiachallenge-production.up.railway.app/docs


