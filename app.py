from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/weekend_plans.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest-plans', methods=['GET'])
def suggest_plans():
    location = request.args.get('location', '')
    
    if not location:
        return jsonify({'error': 'Location is required!'}), 400

    # Filter the data based on the provided location
    filtered_data = data[data['city'] == location]

    # Extracting the plan for the specific city and the description of the plan
    filtered_data_columns = filtered_data[['plan', 'description', 'reference']]
    filtered_data_list = filtered_data_columns.apply(lambda x: x.unique().tolist()).tolist()

    # Extract plans, descriptions, and links for the specific city
    suggested_plans = list(zip(filtered_data_list[0], filtered_data_list[1], filtered_data_list[2]))

    # Render the output on an HTML page
    return render_template('plans.html', suggested_plans=suggested_plans)

if __name__ == '__main__':
    app.run(debug=True)
