import pickle
import numpy as np
from flask import render_template,request
from main_app import app
# Helper function to get location code  
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
               'Amruthahalli': 461, 
               'Anagalapura Near Hennur Main Road': 51, 
               'Anekal City': 606, 
               'Anjanapura': 262, 
               'Ashok Nagar': 80, 
               'Attibele': 72, 
               'Avalahalli Oﬀ Sarjapur Road': 557, 
               'Badamanavarthekaval': 295, 
               'Banashankari': 489, 
               'Banaswadi': 335, 
               'Bannerughatta': 57, 
               'Begur': 239, 
               'Bellandur': 561, 
               'Bikasipura': 715, 
               'Bilekahalli': 457, 
               'Bommanahalli': 189, 
               'Bommasandra': 88, 
               'Brookefield': 71, 
               'BTM Layout': 375, 
               'Budigere Cross': 101, 
               'Carmelaram': 776, 
               'Chandapura': 420, 
               'Chikkagubbi on Hennur Main Road': 786, 
               'CV Raman Nagar': 505, 
               'Dasarahalli on Tumkur Road': 302, 
               'Devanahalli': 240, 
               'Doddanekundi': 319, 
               'Domlur': 159, 
               'Electronic City Phase 1': 821, 
               'Electronic City Phase 2': 252, 
               'Electronics City': 130, 
               'Gottigere': 296, 
               'Harlur': 345, 
               'Hebbal': 110, 
               'Hennur': 279, 
               'Horamavu': 748, 
               'Hosa Road': 590, 
               'Hulimavu': 369, 
               'ITPL': 777, 
               'J. P. Nagar': 277, 
               'Jakkur': 269, 
               'Jalahalli': 310, 
               'Jayanagar': 170, 
               'Jigani': 364, 
               'JP Nagar Phase 1': 155, 
               'JP Nagar Phase 3': 260, 
               'JP Nagar Phase 4': 259, 
               'JP Nagar Phase 6': 600, 
               'JP Nagar Phase 7': 726, 
               'JP Nagar Phase 8': 30, 
               'JP Nagar Phase 9': 211, 
               'Junnasandra': 478, 
               'K. Chudahalli': 477, 
               'Kadugodi Industrial Area': 607, 
               'Kadugodi': 261, 
               'Kanakapura Road Beyond Nice Ring Road': 227, 
               'Kannamangala': 822, 
               'Kasheli ': 744, 
               'Kasheli ': 813, 
               'Kengeri': 238, 
               'Kodigehalli': 246, 
               'Kogilu': 486, 
               'Konanakunte': 578, 
               'Koramangala': 231, 
               'Kothanur': 285, 
               'KPC Layout': 558, 
               'Krishnarajapura': 108, 
               'Kudlu': 734, 
               'Kumaraswamy Layout': 94, 
               'Kumbalgodu': 114, 
               'Marsur': 255, 
               'Muneshwara Nagar': 275, 
               'Nagarbhavi': 119, 
               'Narayanaghatta': 35, 
               'Narayanapura on Hennur Main Road': 356, 
               'Nelamangala': 48, 
               'Padmanabhanagar': 232, 
               'R T Nagar': 258, 
               'R.K. Hegde Nagar': 301, 
               'Rajajinagar': 815, 
               'Ramamurthy Nagar': 816, 
               'Richmond Town': 267, 
               'RMV Extension Stage 2': 365, 
               'RMV': 534, 
               'RR Nagar': 85, 
               'Sahakar Nagar': 284, 
               'Sanjaynagar': 113, 
               'Sarjapur Road Wipro To Railway Crossing': 560, 
               'Singasandra': 257, 
               'Subramanyapura': 256, 
               'Talaghattapura': 370, 
               'Thanisandra': 570, 
               'Uttarahalli Hobli': 129, 
               'Uttarahalli': 31, 
               'Varthur': 798, 
               'Vidyaranyapura': 188, 
                'Whitefield Hope Farm Junction': 187, 
                'Whitefield': 559, 
                'Yelahanka': 36, 
                'Yerthiganahalli': 62, 

    }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_bangalore.pkl", "rb") as f:
    model = pickle.load(f)
    # print("Loaded model:\n", model)
# Define route for index page

def bangalore():
    return render_template('bangalore.html')

# Handle prediction request

def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form['area'])
    if area > 9900 or area <200 :   
        return render_template("bangalore.html", alert = " Area should be between  range of 200-9900")
    bedrooms = int(request.form['bedrooms'])
    if bedrooms > 9 or bedrooms < 1:
        return render_template("bangalore.html",alert ="Bedrooms should be between range of 1-9")
    location = request.form['location']
    School = 1 if request.form['School'] == 'Yes' else 0
    rain_water_harvesting = 1 if request.form['rain-water-harvesting'] == 'Yes' else 0
    Staff_Quarter = 1 if request.form['Staff-Quarter'] == 'Yes' else 0
    Intercom = 1 if request.form['Intercom'] == 'Yes' else 0
    cafeteria = 1 if request.form['Cafeteria'] == 'Yes' else 0
    Lift_Available = 1 if request.form['Lift-Available'] == 'Yes' else 0
    Maintenance_Staff = 1 if request.form['Maintenance-Staff'] == 'Yes' else 0
    Gas_connection = 1 if request.form['Gas-connection'] == 'Yes' else 0
    Landscaped_Gardens = 1 if request.form['Landscaped-Gardens'] == 'Yes' else 0
    Vaastu_Compliant = 1 if request.form['Vaastu-Compliant'] == 'Yes' else 0
    Hospital = 1 if request.form['Hospital'] == 'Yes' else 0
    ATM = 1 if request.form['ATM'] == 'Yes' else 0
    Indoor_Games = 1 if request.form['Indoor-Games'] == 'Yes' else 0
    Washing_Machine = 1 if request.form['Washing-Machine'] == 'Yes' else 0
    Car_Parking = 1 if request.form['Car-Parking'] == 'Yes' else 0
    Shopping_Mall = 1 if request.form['Shopping-Mall'] == 'Yes' else 0
    Golf_Course = 1 if request.form['Golf-Course'] == 'Yes' else 0

    # Preprocess user input
    location_code = get_location_code(location)

    # Print received form data
    
    # Make prediction
    features = np.array([[area,bedrooms, Maintenance_Staff, Intercom, Indoor_Games,
                         School, Staff_Quarter, Lift_Available, Gas_connection,
                         Landscaped_Gardens, Vaastu_Compliant, Hospital, ATM,
                         Shopping_Mall, Golf_Course, location_code, 
                         Car_Parking, cafeteria, Washing_Machine , rain_water_harvesting]])
    # print("features: \n",features)
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('bangalore.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True)
