## Overview

This project comprises two main components:

1. **Web Scraper (`scrapper.py`)**: A Python script that extracts data from specified websites.
2. **API Service (`main.py`)**: Provides endpoints to access the scraped data.


## Installation

### Prerequisites

- Python 3.6 or higher
- pip


### Setup Steps

1. **Clone the Repository**:

   ```
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. **Navigate to the Project Directory**:
   ```
   cd your-repo-name
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

To execute the scraper and collect data:
```
python scrapper.py
```

### Starting the API Service

Launch the API server with:
```
uvicorn main:app --reload
```
The API will be accessible at http://localhost:8000.

### API Endpoints
The API provides the following endpoints:

- GET /data : Retrieve all the data
- GET /data?query=news : Retrieve the data based on keyword(here news included data is retrieved)
  


