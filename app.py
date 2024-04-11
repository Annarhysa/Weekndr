from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the data from a CSV file
data = pd.read_csv('data/weekend_plans.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_plans', methods=['POST'])
def suggest_plans():
    location = request.form['location']

    location_capital = location.title()
    
    #if not location:
        #return jsonify({'error': 'Location is required!'}), 400

    # Filter the data based on the provided location
    filtered_data = data[data['city'] == location_capital]

    # Extracting the plan for the specific city and the description of the plan
    filtered_data_columns = filtered_data[['plan', 'description', 'reference']]
    
    # Check for duplicates row by row
    has_duplicates = False
    for index, row in data.iterrows():
        if len(row) != len(set(row)):
            has_duplicates = True
            break

    # If duplicates exist, perform the action
    if has_duplicates:
        # Convert the DataFrame to a list of lists
        data_list = filtered_data_columns.values.tolist()

        # Remove duplicate values from each inner list
        filtered_data_list = [list(set(row)) for row in data_list]

    else:
        # No duplicates, just convert the DataFrame to a list of lists
        filtered_data_list = filtered_data_columns.values.tolist()

    # Render the output on an HTML page
    return render_template('plans.html', plans=filtered_data_list, location = location_capital)

if __name__ == '__main__':
    app.run(debug=True)
