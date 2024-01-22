import spacy
from flask import Flask, request, jsonify
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex


app = Flask(__name__)
nlp = spacy.load("en_coreference_web_trf")
#doc = nlp("""jhon bought a new fast 4-wheel car. He daily drives this car but the car is disturbing him.""")
# Modify tokenizer infix patterns
infixes = (
    LIST_ELLIPSES 
    + LIST_ICONS
    + [
        r"(?<=[0-9])[+\\-\\*^](?=[0-9-])",
        r"(?<=[{al}{q}])\\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        # ✅ Commented out regex that splits on hyphens between letters:
        # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    ]
)

infix_re = compile_infix_regex(infixes)
nlp.tokenizer.infix_finditer = infix_re.finditer

@app.route('/coreference_resolution', methods=['POST'])
def coreference_resolution():
    # Get the input text from the request
    input_text = request.json.get('document', '')

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



