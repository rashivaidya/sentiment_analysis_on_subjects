from flask import Flask, render_template, request, jsonify
from src.data_generation import generate_data
from src.preprocess import preprocess_data
from src.analysis import analyze_sentiments
from src.visualization import create_visualizations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_entries = int(request.form.get('num_entries', 200))
    generate_data(num_entries=num_entries)
    return jsonify({"message": f"{num_entries} entries generated successfully!"})

@app.route('/preprocess', methods=['POST'])
def preprocess():
    preprocess_data()
    return jsonify({"message": "Data preprocessing completed successfully!"})

@app.route('/analyze', methods=['POST'])
def analyze():
    analyze_sentiments()
    return jsonify({"message": "Sentiment analysis completed successfully!"})

@app.route('/visualize', methods=['POST'])
def visualize():
    create_visualizations()
    return jsonify({"message": "Visualizations created successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
