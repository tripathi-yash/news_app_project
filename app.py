from flask import Flask, render_template, request, jsonify
import time
from news_service import get_news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/news', methods=["GET"])
def news():
    try:
        query = request.args.get("q", type=str)
        if not query: 
            return jsonify({
                "error" : "Query parameter 'q' is requiured!" 
            }),400 #400-Bad request
        
        limit = request.args.get("limit", default=5, type=int)
        language = request.args.get("language", default="en", type=str)
        pageSize = request.args.get("pageSize", default=100, type=int)

        from_time = "2026-01-01"

        t=time.localtime()
        to_time = time.strftime("%Y-%m-%dT%H:%M:%S",t)

        articles = get_news(
            query, 
            limit=limit, 
            language=language, 
            from_=from_time, 
            to=to_time, 
            pageSize=pageSize)
        
        cleaned_articles = []
        for article in articles:
            cleaned_articles.append({
                "title": article.get("title", " "),
                "description": article.get("description", " ")
                })

        return render_template("index.html",articles = cleaned_articles), 200
    
    except RuntimeError as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run() 
