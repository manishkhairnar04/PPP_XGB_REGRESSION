import pickle
import numpy as np
from flask import Flask, render_template, request
from main_app import app


# Helper function to get location code
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
        'Baguiati': 68,
        'Barsat': 79,
        'Behala': 86,
        'Bhadreswar': 90,
        'Chkravarti Para': 138,
        'Dum Dum Park': 175,
        'Dum Dum': 174,
        'Garia': 197,
        'Gariahat': 198,
        'Hooghly Chinsurah': 237,
        'Hussainpur': 241,
        'Joka': 272,
        'Keshtopur': 320,
        'Konnagar': 348,
        'Kutighat': 374,
        'Lake Gardens': 380,
        'Madhyamgram': 392,
        'Madurdaha Hussainpur': 396,
        'Mukundapur': 450,
        'Narendrapur': 480,
        'New Alipore': 493,
        'New Town': 495,
        'Rajarhat': 565,
        'Santoshpur': 604,
        'Sarsuna': 609,
        'Sodepur': 719,
        'Sonarpur': 721,
        'south dum dum': 842,
        'Tangra': 737,
        'Tollygunge': 763,
        'Ultadanga': 768,
        'Uttarpara Kotrung': 778
    }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_kolkata.pkl", "rb") as f:
    model = pickle.load(f)
# Print model information
# print("Loaded model:", model)
# Define route for index page

def kolkata():
    return render_template('Kolkata.html')

# Handle prediction request

def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form['area'])
    if area > 9900 or area <200 :   
        return render_template("kolkata.html", alert = " Area should be between  range of 200-9900")
    bedrooms = int(request.form['bedrooms'])
    if bedrooms > 9 or bedrooms < 1:
        return render_template("kolkata.html",alert ="Bedrooms should be between range of 1-9")
    location = request.form['location']
    club_house = 1 if request.form['club-house'] == 'Yes' else 0
    rain_water_harvesting = 1 if request.form['rain-water-harvesting'] == 'Yes' else 0
    swimming_pool = 1 if request.form['swimming-pool'] == 'Yes' else 0
    resale = 1 if request.form['resale'] == 'Yes' else 0
    cafeteria = 1 if request.form['Cafeteria'] == 'Yes' else 0
    lift_available = 1 if request.form['LiftAvailable'] == 'Yes' else 0
    maintenance_staff = 1 if request.form['MaintenanceStaff'] == 'Yes' else 0
    jogging_track = 1 if request.form['JoggingTrack'] == 'Yes' else 0
    landscaped_gardens = 1 if request.form['LandscapedGardens'] == 'Yes' else 0
    vaastu_compliant = 1 if request.form['VaastuCompliant'] == 'Yes' else 0
    multipurpose_room = 1 if request.form['MultipurposeRoom'] == 'Yes' else 0
    power_backup = 1 if request.form['PowerBackup'] == 'Yes' else 0
    indoor_games = 1 if request.form['IndoorGames'] == 'Yes' else 0
    washing_machine = 1 if request.form['WashingMachine'] == 'Yes' else 0
    car_parking = 1 if request.form['CarParking'] == 'Yes' else 0
    sports_facility = 1 if request.form['SportsFacility'] == 'Yes' else 0
    gymnasium = 1 if request.form['Gymnasium'] == 'Yes' else 0

    # Preprocess user input
    location_code = get_location_code(location)

    # Print received form data
    '''
    print("Received Form Data:")
    print("Area:", area)
    print("Bedrooms:", bedrooms)
    print("Location:", location)
    print("Club House:", club_house)
    print("Rain Water Harvesting:", rain_water_harvesting)
    print("Swimming Pool:", swimming_pool)
    print("Resale:", resale)
    print("Cafeteria:", cafeteria)
    print("Lift Available:", lift_available)
    print("Maintenance Staff:", maintenance_staff)
    print("Jogging Track:", jogging_track)
    print("Landscaped Gardens:", landscaped_gardens)
    print("Vaastu Compliant:", vaastu_compliant)
    print("Multipurpose Room:", multipurpose_room)
    print("Power Backup:", power_backup)
    print("Indoor Games:", indoor_games)
    print("Washing Machine:", washing_machine)
    print("Car Parking:", car_parking)
    print("Sports Facility:", sports_facility)
    print("Gymnasium:", gymnasium)
    '''
    # Make prediction
    features = np.array([[area, swimming_pool, resale, club_house, rain_water_harvesting, cafeteria, lift_available,
                          maintenance_staff, location_code, jogging_track, landscaped_gardens, bedrooms,
                          vaastu_compliant, multipurpose_room, power_backup, indoor_games, washing_machine, car_parking,
                          sports_facility, gymnasium]])
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('kolkata.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True)
