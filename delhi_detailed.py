import pickle
import numpy as np
from flask import  render_template, request
from main_app import app


 
# Helper function to get location code
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
                     'Alaknanda': 11,
                     'Ashok Vihar': 46,
                     'Babarpur': 58,
                     'Bindapur': 96,
                     'Budh Vihar': 109,
                     'Burari': 111,
                     'Chattarpur': 120,
                     'Chittaranjan Park': 137,
                     'Dashrath Puri': 156,
                     'DLF Farms': 145,
                     'DLF Phase 5': 146,
                     'Dwarka Mor': 176,
                     'East of Kailash': 182,
                     'Govindpuri': 212,
                     'Greater kailash 1': 216,
                     'greater kailash Enclave 1': 827,
                     'Greater Kailash II': 215,
                     'Greater Kailash': 214,
                     'Green Park': 217,
                     'Hari Nagar': 225,
                     'Hauz Khas': 229,
                     'Jamia Nagar': 264,
                     'Jasola': 266,
                     'Kalkaji Extension': 287,
                     'Kalkaji': 286,
                     'Karol Bagh': 308,
                     'Katwaria Sarai': 315,
                     'Kaushambi': 316,
                     'Khanpur': 322,
                     'Khirki Extension': 327,
                     'Lajpat Nagar III': 378,
                     'Lajpat Nagar': 377,
                     'Mahavir Enclave': 401,
                     'Mahipalpur': 402,
                     'Mansa Ram Park': 415,
                     'Matiala': 422,
                     'Mayur Vihar II': 425,
                     'mayur vihar phase 1': 833,
                     'Mayur Vihar': 424,
                     'Mehrauli': 431,
                     'Mundka': 456,
                     'Nasirpur': 482,
                     'nawada': 836,
                     'Palam': 508,
                     'Paschim Vihar': 522,
                     'Patparganj': 527,
                     'Pitampura': 538,
                     'Pochanpur Colony': 539,
                     'Rohini Extension': 581,
                     'Rohini sector 24': 583,
                     'Rohini Sector 9': 582,
                     'Safdarjung Enclave': 588,
                     'Saidabad': 592,
                     'Sainik Farms': 594,
                     'Sarita Vihar': 605,
                     'Sarvodaya Enclave': 610,
                     'Sector 10 Dwarka': 613,
                     'Sector 11 Dwarka': 616,
                     'Sector 12 Dwarka': 619,
                     'Sector 13 Dwarka': 621,
                     'Sector 13 Rohini': 622,
                     'Sector 16B Dwarka': 625,
                     'Sector 17 Dwarka': 626,
                     'Sector 18A Dwarka': 631,
                     'Sector 18B Dwarka': 632,
                     'Sector 19 Dwarka': 633,
                     'Sector 2 Dwarka': 636,
                     'Sector 20 Rohini': 639,
                     'Sector 21 Dwarka': 640,
                     'Sector 22 Dwarka': 644,
                     'Sector 22 Rohini': 646,
                     'Sector 23 Dwarka': 647,
                     'Sector 23 Rohini': 648,
                     'Sector 23B Dwarka': 650,
                     'Sector 24 Rohini': 651,
                     'Sector 25 Rohini': 652,
                     'Sector 28 Rohini': 653,
                     'Sector 3 Dwarka': 654,
                     'Sector 4 Dwarka': 661,
                     'Sector 5 Dwarka': 663,
                     'Sector 6 Dwarka': 665,
                     'Sector 7 Dwarka': 666,
                     'Sector 9 Dwarka': 668,
                     'Sector 9 Rohini': 669,
                     'Sector-14 Rohini': 672,
                     'Sector-18 Dwarka': 673,
                     'Sector-8 Rohini': 681,
                     'Sector-D Vasant Kunj': 683,
                     'Sewak Park': 697,
                     'Shahdara': 699,
                     'Shakurbasti': 702,
                     'Shanti Park Dwarka': 705,
                     'Sheikh Sarai': 707,
                     'Sidhartha Nagar': 711,
                     'Siri Fort': 716,
                     'South Extension 2': 723,
                     'SULTANPUR': 587,
                     'Uttam Nagar': 775,
                     'Vasant Kunj': 790,
                     'West End': 809,
                     'West Sagarpur': 811,
               }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_delhi.pkl", "rb") as f:
    model = pickle.load(f)
# Print model information
# print("Loaded model:", model)
# Define route for index page

def delhi():
    return render_template('delhi.html')

# Handle prediction request

def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form["area"])
    if area > 9900 or area <200 :   
        return render_template("delhi.html", alert = " Area should be between  range of 200-9900")
    bedrooms = int(request.form["bedrooms"])
    if bedrooms > 9 or bedrooms < 1:
        return render_template("delhi.html",alert ="Bedrooms should be between range of 1-9")
    location = request.form["location"]
    Gas_connection = 1 if request.form["Gas-connection"] == 'Yes' else 0
    rain_water_harvesting = 1 if request.form["rain-water-harvesting"] == 'Yes' else 0
    Swimming_Pool = 1 if request.form["swimming-pool"] == 'Yes' else 0
    resale = 1 if request.form["resale"] == 'Yes' else 0
    Dining_Table = 1 if request.form["Dining-Table"] == 'Yes' else 0
    Lift_Available = 1 if request.form["Lift-Available"] == 'Yes' else 0
    Maintenance_Staff = 1 if request.form["Maintenance-Staff"] == 'Yes' else 0
    AC = 1 if request.form["AC"] == 'Yes' else 0
    Childrens_playarea = 1 if request.form["Children's- playarea"] == 'Yes' else 0
    Intercom = 1 if request.form["Intercom"] == 'Yes' else 0
    Power_Backup = 1 if request.form["Power-Backup"] == 'Yes' else 0
    Indoor_Games = 1 if request.form["Indoor-Games"] == 'Yes' else 0
    BED = 1 if request.form["BED"] == 'Yes' else 0
    Car_Parking = 1 if request.form["Car-Parking"] == 'Yes' else 0
    Sports_Facility = 1 if request.form["Sports-Facility"] == 'Yes' else 0
    Refrigerator = 1 if request.form["Refrigerator"] == 'Yes' else 0
    Microwave= 1 if request.form["Microwave"] == 'Yes' else 0

    # Preprocess user input
    location_code = get_location_code(location)

    
    # Make prediction
    features = np.array([[area, resale, location_code, Indoor_Games, AC,
                          Dining_Table, Intercom, BED,  bedrooms,
                         Childrens_playarea, Microwave, Car_Parking, rain_water_harvesting,
                         Lift_Available, Gas_connection,  Refrigerator,Power_Backup,
                         Maintenance_Staff, Swimming_Pool, Sports_Facility ]])
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('delhi.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True)
