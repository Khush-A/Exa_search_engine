# Exa Search Engine

A minimal web-based search engine built with Flask and Exa.
Users can enter a query, filter by domain, choose search modes (Web / TikTok / YouTube), and view results in a clean UI.

# Features

- Search the web using Exa’s API
- Optional domain filtering (e.g. tiktok.com)
- Mode selector (Web, TikTok, YouTube)
- Loading spinner

Simple Flask backend + HTML/CSS frontend

# Tech Stack
- Python
- Flask
- Exa (exa-py)
- HTML / CSS / JS

# How to Run Locally
git clone https://github.com/Khush-A/Exa_search_engine.git
cd Exa_search_engine

python3 -m venv venv
source venv/bin/activate

pip install flask exa-py
export EXA_API_KEY="your_api_key_here"

python3 app.py


Then open your browser at http://127.0.0.1:5000

# Requires
- Python 3.9+
- An Exa API key
