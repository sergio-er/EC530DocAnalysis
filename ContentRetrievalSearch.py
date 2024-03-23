from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data store(will change with DB implementation)
documents = [
    {
        "id": "1",
        "text": "This is a positive sentence about environment.",
        "keywords": ["environment"],
        "sentiment": "positive"
    },
    {
        "id": "2",
        "text": "This is a neutral statement regarding politics.",
        "keywords": ["politics"],
        "sentiment": "neutral"
    },
]

@app.route('/search/keywords', methods=['GET'])
def search_by_keywords():
    keyword = request.args.get('keyword', '')
    #This would involve a database or search engine query.
    results = [doc for doc in documents if keyword in doc['keywords']]
    return jsonify(results)

@app.route('/search/sentiment', methods=['GET'])
def search_by_sentiment():
    sentiment = request.args.get('sentiment', '')
    # This would query data store or search engine.
    results = [doc for doc in documents if doc['sentiment'] == sentiment]
    return jsonify(results)

@app.route('/search/external', methods=['GET'])
def external_search():
    # This endpoint might integrate with external APIs from Open Data sources.
    keyword = request.args.get('keyword', '')
    source = request.args.get('source', '').lower()

    # Placeholder response to illustrate the concept.
    # Actual implementation would be very different
    results = {"message": "External search not implemented", "keyword": keyword, "source": source}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
