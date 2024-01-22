import spacy
from flask import Flask, request, jsonify


app = Flask(__name__)
nlp = spacy.load("en_coreference_web_trf")
#doc = nlp("""jhon bought a new fast 4-wheel car. He daily drives this car but the car is disturbing him.""")


@app.route('/coreference_resolution', methods=['POST'])
def coreference_resolution():
    # Get the input text from the request
    input_text = request.json.get('text', '')

    # Process the input text with spaCy
    doc = nlp(input_text)

    # Extract coreference clusters
    clusters = [
        val for key, val in doc.spans.items() if key.startswith("coref_cluster")
    ]

    # Build the result object
    result_object = {"clusters": []}
    for cluster in clusters:
        cluster_indices = []
        for span in cluster:
            cluster_indices.append([span.start, span.end])
        result_object["clusters"].append(cluster_indices)

    return jsonify(result_object)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



