import requests
import time
import os
# from config import API_KEY 

API_KEY = os.environ.get("API_KEY")

NEWS_URL = "https://newsapi.org/v2/everything"

def get_news(query : str, limit : int = 5, language : str = "en",**kwargs) -> list[dict]:

    params = {
        'q' : query,
        "language" : language,
        "apiKey" : API_KEY,
        "sortBy" : 'publishedAt'
    }

    ALLOWED = {"pageSize", "from_", "to"} # sec check
     
    params.update({
        ("from" if k == "from_" else k):v 
        for k,v in kwargs.items() 
        if k in ALLOWED
        })

    try:
        response = requests.get(NEWS_URL, params=params, timeout=5)
        response.raise_for_status() # raise any HTTP request status error(400,401,404,500)
        data =response.json() # parses raw json into python list/dict

        if data["status"] == "error":
            raise RuntimeError(f"API_Key error: {data['message']}")

        return data.get("articles",[])[:limit] # returns articles[dict] or []

    except requests.exceptions.RequestException as e: # handles any network error
        if e.response is not None:
            print("STATUS CODE:", e.response.status_code)
            print("RESPONSE BODY:", e.response.text)
        raise RuntimeError("News API request failed") from e
    

def main():
    query = input("Enter a topic to search news: ").strip().lower()

    if query:
        t = time.localtime()
        to_time = time.strftime("%Y-%m-%dT%H:%M:%S",t)
        articles = get_news(query, pageSize=100, to=to_time)
    else: 
        print("error: Invalid query!")
        exit()

    print("\nTop Headlines:\n" + "-" * 40)
    for i, news in enumerate(articles,start = 1):
        print(f"{i}.Title: {news.get('title', 'No title')}")
        print(f" News: {news.get('description', 'No description available')}\n")

if __name__ == "__main__":
    main()


    
    





