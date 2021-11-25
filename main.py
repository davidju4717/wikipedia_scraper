from flask import Flask, json, jsonify
import wikipedia
import requests

app = Flask(__name__)

# route to the main page
@app.route('/')
def index():
    return "Please navigate to /[title] to use this API"

# route to extract complete content of a page
@app.route('/<title>')
def article_content(title):
    # get the content of article. If not found, use the closest article name
    try:
        page = wikipedia.page(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        title = e.options[0]
        page = wikipedia.page(title, auto_suggest=False)

    # return title, url and content of the article
    result = {}
    result["title"] = page.title
    result["url"] = page.url
    result["content"] = page.content
    return (jsonify(result), 200)


# route to extract summary of the article
@app.route('/<title>/summary')
def article_summary(title):
    # get the summary of article. If not found, use the closest article name
    try:
        page = wikipedia.page(title, auto_suggest=False)
        summary = wikipedia.summary(title, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        title = e.options[0]
        page = wikipedia.page(title, auto_suggest=False)
        summary = wikipedia.summary(title, auto_suggest=False)

    # return title, url and summary of the article
    result = {}
    result["title"] = page.title
    result["url"] = page.url
    result["summary"] = summary
    return (jsonify(result), 200)


# route to obtain first x sentences from the summary of the article
@app.route('/<title>/summary/<sentences>')
def article_summary_sentences(title, sentences):
    # get the summary of article. If not found, use the closest article name
    try:
        page = wikipedia.page(title, auto_suggest=False)
        summary = wikipedia.summary(title, auto_suggest=False, sentences=int(sentences))
    except wikipedia.exceptions.DisambiguationError as e:
        title = e.options[0]
        page = wikipedia.page(title, auto_suggest=False)
        summary = wikipedia.summary(title, auto_suggest=False, sentences=int(sentences))

    # return title, url and summary of the article
    result = {}
    result["title"] = page.title
    result["url"] = page.url
    result["summary"] = summary
    return (jsonify(result), 200)

# route to obtain url of the main image of the article
@app.route('/<title>/image')
def article_image(title):

    # get the page of article. If not found, use the closest article name
    try:
        page = wikipedia.page(title, auto_suggest=False)
    except wikipedia.DisambiguationError as e:
        title = e.options[0]
        page = wikipedia.page(title, auto_suggest=False)

    # get the url to the main image of the article
    WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='
    response = requests.get(WIKI_REQUEST + title)
    json_data = json.loads(response.text)
    img_link = list(json_data['query']['pages'].values())[0]['original']['source']

    # return title, article url and url of the image
    result = {}
    result["title"] = page.title
    result["url"] = page.url
    result["image_url"] = img_link
    return (jsonify(result), 200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)