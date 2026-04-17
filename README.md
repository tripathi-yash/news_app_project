# 📰 NewsPaps

A simple and clean **Flask-based news search web application** that fetches and displays the latest news using a public news API.

This project focuses on **backend fundamentals**, **clean UI**, and **real-world development practices**, without unnecessary complexity.

---

## 🚀 Features

- Search news by topic
- Filter by language
- Limit number of results
- Clean, responsive UI
- Server-side rendering using Flask & Jinja2
- Proper error handling

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (no frameworks), JavaScript
- **API:** News API
- **Templating:** Jinja2

---

## 📂 Project Structure
flask_news_app/
│
├── app.py
├── news_service.py
├── templates/
│   ├── base.html
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── .gitignore
└── README.md

---

## 🔧 Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/your-username/newspaps.git
cd newspaps

2. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set Environment Variables
Windows (PowerShell)
setx API_KEY "your_api_key_here"

Mac/Linux
export API_KEY="your_api_key_here"

⚠️ Restart terminal after setting environment variables

5. Run the Application
python app.py
Open in browser: http://127.0.0.1:5000

🌐 Deployment
Deployed on Railway
➡️ Live App: https://newsappproject-production.up.railway.app/

👤 Author

Yash
❤️ Built with pyhton & Flask  
