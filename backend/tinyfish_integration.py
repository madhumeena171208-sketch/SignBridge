import os
import requests
from dotenv import load_dotenv

load_dotenv()

# TinyFish API configuration (Placeholder for hackathon submission)
TINYFISH_API_URL = "https://api.tinyfish.io/v1/search"  
TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY", "")

def fetch_tinyfish_context(query: str):
    """
    Fetches relevant context or public page data using TinyFish API 
    to assist users during the SignBridge video call.
    """
    headers = {
        "Authorization": f"Bearer {TINYFISH_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query
    }
    
    try:
        if not TINYFISH_API_KEY:
            return {"status": "success", "data": f"Mock context card for: {query}"}
            
        response = requests.post(TINYFISH_API_URL, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}