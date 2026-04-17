from flask import Flask, render_template, request, jsonify
import time
from datetime import datetime, timezone, timedelta
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

        today = datetime.now(timezone.utc)
        one_month_ago = today - timedelta(days=30)
        from_time = one_month_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
        to_time = today.strftime("%Y-%m-%dT%H:%M:%SZ")

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
        print("ERROR:", e)   # 👈 ADD THIS
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
