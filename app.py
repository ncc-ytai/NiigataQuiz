from flask import Flask, render_template, request, jsonify
import MeCab

app = Flask(__name__)

def segment_text(text):
    mecab = MeCab.Tagger('-Owakati')
    parsed_text = mecab.parse(text)
    words = parsed_text.split()
    output_text = ' '.join(words)
    return output_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    texts = data['texts']  # textsは複数のテキストのリスト
    segmented_texts = [segment_text(text) for text in texts]
    return jsonify({'segmented_texts': segmented_texts})

if __name__ == "__main__":
    app.run(debug=True)


