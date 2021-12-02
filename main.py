from flask import Flask, json, jsonify
import wikipedia
import requests

app = Flask(__name__)

# function to obtain the wiki page
def get_wiki_page(title):

    # If title not found, use the closest article name
    try:
        page = wikipedia.page(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        title = e.options[0]
        page = wikipedia.page(title, auto_suggest=False)

    return page

# route to the main page
@app.route('/')
def index():
    return "Please navigate to /[title] to use this API"

# route to extract complete content of a page
@app.route('/<title>')
def article_content(title):

    # obtain title, url and content of the article page
    page = get_wiki_page(title)
    result = {"title": page.title, "url": page.url, "content": page.content}
    return (jsonify(result), 200)


# route to extract summary of the article
@app.route('/<title>/summary')
def article_summary(title):

    # obtain title, url and summary of the article page
    page = get_wiki_page(title)
    summary = wikipedia.summary(page.title, auto_suggest=False)
    result = {"title": page.title, "url": page.url, "summary": summary}
    return (jsonify(result), 200)

# route to obtain url of the main image of the article
@app.route('/<title>/image')
def article_image(title):

    # get the url to the main image of the article page
    page = get_wiki_page(title)
    WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='
    response = requests.get(WIKI_REQUEST + page.title)
    json_data = json.loads(response.text)
    img_link = list(json_data['query']['pages'].values())[0]['original']['source']

    # return title, article url and url of the image
    result = {"title": page.title, "url": page.url, "image_url": img_link}
    return (jsonify(result), 200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)