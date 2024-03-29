# Weekndr
An app that suggests weekend plans in your city.

## Problem Statement

Planning weekend activities can be time-consuming and overwhelming, especially in a bustling city with numerous options. People often struggle to find suitable activities that match their preferences and interests. Therefore, there is a need for an app that can efficiently suggest personalized weekend plans based on the user's location and preferences.

## Tech Stack

- **Frontend**: JavaScript (JS), HTML, CSS
- **Backend**: Python with Flask framework
- **Database**: SQLite or any preferred database for storing user data
- **Deployment**: Heroku or any preferred hosting platform

## Methodology

1. **User Input**: Users input their location and preferences, such as interests, budget, and group size, into the app.
  
2. **Backend Processing**: The backend server built with Python and Flask processes the user input and retrieves relevant data from the database.

3. **Algorithmic Recommendation**: An algorithm running on the backend analyzes the user input and generates personalized weekend plans based on factors like location, weather, time, and user preferences.

4. **Frontend Display**: The suggested weekend plans are displayed to the user through a user-friendly interface built with HTML, CSS, and JavaScript. Users can view details of each plan and make selections.

5. **Feedback Loop**: Users can provide feedback on suggested plans, helping the app refine future recommendations and improve user satisfaction.

## Use Case

Sarah, a busy professional living in a metropolitan city, wants to make the most of her weekends but often struggles to decide on activities. She downloads the "Weekend Explorer" app and inputs her location, interests, and budget preferences.

The app's backend processes Sarah's input and suggests a variety of weekend plans tailored to her preferences. Sarah receives recommendations for activities such as movie screenings, outdoor picnics, museum visits, and hiking trails within her city.

Impressed by the app's suggestions, Sarah selects a few plans that interest her and shares them with her friends through the app's social sharing feature. They collectively decide on a picnic at a nearby park and plan to visit a local museum afterward.

With the help of the "Weekend Explorer" app, Sarah and her friends enjoy a fun-filled weekend exploring their city's attractions without the stress of planning.

## Repository Usage

To use this repository, follow these steps:

1. **Clone the Repository**: 
    ```
    git clone <repository_url>
    ```
2. **Create a Virtual Environment** (Optional but recommended):
    ```
    python -m venv weekndr
    ```
3. **Activate the Virtual Environment**:
    - On Windows:
    ```
    weekndr\Scripts\activate
    ```
    - On Unix or MacOS:
    ```
    source weekndr/bin/activate
    ```
4. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```
5. **Run the Flask App**:
    ```
    python app.py
    ```
6. **Open the HTML File**:
    Open a web browser and navigate to (eg: `http://localhost:5000`) to view the frontend interface.
7. **Explore Weekend Plans**:
    Input your location and preferences into the app to receive personalized weekend plans.
8. **Enjoy Your Weekend!**





