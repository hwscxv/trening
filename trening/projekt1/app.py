from repositories.urls import save_command, fetch_categories, fetch_urls
from flask import Flask, jsonify, request

app = Flask(__name__)
 
 
@app.route("/add", methods = ['POST'])
def add():
    req = request.get_json()
    category = req['category']
    url = req['url']
    save_command(category, url)
    return {
        'status': 'ok'
    }

@app.route("/categories")
def get_categories():
    categories = fetch_categories()
    return jsonify([category[0]for category in categories])

@app.route("/category/<name>")
def get_category(name):
    urls = fetch_urls(name)
    # print(urls)
    return jsonify(urls)