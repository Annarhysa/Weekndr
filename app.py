from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Predefined activities and their corresponding locations
activities = {
    'Location': ['Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Mysore', 'Coorg'],
    'movies': ['Cinema Hall A', 'Cinema Hall B', 'Cinema Hall C', 'Cinema Hall D', 'Cinema Hall E', 'Cinema Hall F', 'Cinema Hall G'],
    'picnic': ['City Park', 'Lake Park', 'Forest Reserve', 'Beach', 'Hilltop Park', 'Nature Reserve', 'Botanical Garden'],
    'museum': ['Art Museum', 'History Museum', 'Science Museum', 'War Museum', 'Maritime Museum', 'Railway Museum', 'Space Museum'],
    'hiking': ['Mountain Trail', 'Hilltop Park', 'Nature Reserve', 'Forest Reserve', 'Botanical Garden', 'Lake Park', 'Beach'],
}

# Create a DataFrame from the activities dictionary
import pandas as pd
df = pd.DataFrame.from_dict(activities)

# Endpoint to suggest weekend plans
@app.route('/suggest-plans', methods=['GET'])
def suggest_plans():
    location = request.args.get('location', '')
    
    # Check if location is provided
    if not location:
        return jsonify({'error': 'Location is required!'}), 400

    # Generate suggested plans for the weekend
    suggested_plans = {}
    filtered_df = df.loc[df['Location'] == location]
    activities_in_location = filtered_df[['movies', 'picnic', 'museum', 'hiking']].values.tolist()[0]

    for column in df.columns[1:]:
        suggest_plans[column] = df.loc[0, column]

    return jsonify({'suggested_plans': suggested_plans})

if __name__ == '__main__':
    app.run(debug=True)
