import pickle
from flask import render_template,request
import numpy as np

from main_app import app


# Helper function to get location code
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
            'Adambakkam': 5,
            'Adyar': 8,
           'Alandur': 12,
           'Alwarpet': 19,
           'Ambattur': 21,
           'Aminjikarai': 28,
           'Anna Nagar': 37,
           'Annamalai Colony': 38,
           'Annanagar West': 40,
           'Annanagar': 39,
           'Avadi': 50,
           'Ayanambakkam': 52,
           'Ayapakkam': 53,
           'Besant Nagar': 89,
           'Chembarambakkam': 121,
           'Chengalpattu': 125,
           'Chetpet': 127,
           'Chitlapakkam': 136,
           'Cholambedu': 139,
           'Choolaimedu': 140,
           'Chromepet': 141,
           'CIT Nagar': 112,
           'East Tambaram': 181,
           'Egatoor': 184,
           'Egmore': 185,
           'Ekkatuthangal': 186,
           'Gopalapuram': 206,
           'Gowrivakkam': 213,
           'Guduvancheri': 218,
           'Guindy': 219,
           'Injambakkam': 247,
           'Irumbuliyur': 248,
           'Iyappanthangal': 250,
           'Iyyappanthangal': 251,
           'Jamalia': 263,
           'K K Nagar': 276,
           'Kanathur Reddikuppam':  297,
           'Karapakkam': 305,
           'Kattankulathur': 313,
           'Kattupakkam': 314,
           'Kelambakkam': 318,
           'Kil Ayanambakkam': 329,
           'Kilkattalai': 330,
           'Kilpauk': 331,
           'Kodambakkam': 334,
           'Kolapakkam': 339,
           'Kolathur': 340,
           'Korattur': 354,
           'Kotturpuram': 358,
           'Kovilambakkam': 359,
           'Kovur': 360,
           'Koyambedu': 362,
           'Kumananchavadi': 368,
           'Kundrathur': 371,
           'Madambakkam': 387,
           'Madhavaram': 389,
           'Madipakkam': 394,
           'Maduravoyal': 395,
           'Mambakkam': 410,
           'Manapakkam': 411,
           'Manikandan Nagar': 412,
           'Mannivakkam': 414,
           'Maraimalai': 417,
           'Medavakkam': 427,
           'Mevalurkuppam': 434,
           'Mogappair': 442,
           'Moolacheri': 443,
           'Moolakadai': 444,
           'Mudichur': 448,
           'Mugalivakkam': 449,
           'Nandambakkam': 472,
           'Nandanam': 473,
           'Nanganallur': 474,
           'Nanmangalam': 475,
           'Navallur': 484,
           'NehruNagar': 487,
           'Nenmeli': 490,
           'Nungambakkam': 497,
           'Padi': 503,
           'Padur': 507,
           'Palavakkam': 509,
           'Pallavaram': 512,
           'Pallikaranai': 513,
           'Pammal': 515,
           'Pazavanthangal': 528,
           'Peerakankaranai': 530,
           'Perambur': 531,
           'Periyapanicheri': 532,
           'Perumbakkam': 533,
           'Perungalathur': 534,
           'Perungudi': 535,
           'Poonamallee': 543,
           'Porur': 544,
           'Pozhichalur': 546,
           'Purasaiwakkam': 553,
           'Puzhal': 554,
           'Raja Annamalai Puram': 562,
           'Rajakilpakkam': 564,
           'Ramapuram': 571,
           'Ramavaram': 572,
           'Royapettah': 584,
           'Saidapet': 593,
           'Selaiyur': 693,
           'Sembakkam': 694,
           'Semmancheri': 695,
           'Sholinganallur': 710,
           'Singaperumal Koil': 714,
           'Siruseri': 717,
           'Sithalapakkam': 718,
           'Sunnambu Kolathur S Kolathur': 731,
           'T Nagar': 732,
           'Tambaram Sanatoruim': 736,
           'tambaram west': 844,
           'Teynampet': 742,
           'Thaiyur': 743,
           'Thalambur': 745,
           'Thatchoor': 749,
           'Thirumazhisai': 750,
           'Thirumullaivoyal': 751,
           'Thiruvanmiyur': 752,
           'Thiruverkadu': 753,
           'Thiruvidandhai': 754,
           'Thoraipakkam OMR': 756,
           'Thoraipakkam': 755,
           'Tiruvottiyur': 759,
           'Ullagaram': 767,
           'Urapakkam': 773,
           'Vadapalani': 779,
           'Valasaravakkam': 781,
           'Vanagaram': 782,
            'Vandalur': 784,
            'Velachery': 792,
           'Velappanchavadi': 793,
            'Vellakkal': 794,
           'Vengaivasal': 795,
            'Villivakkam': 799,
            'Virugambakkam': 803,
            'West Tambaram': 812,
           
    }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_chennai.pkl", "rb") as f:
    model = pickle.load(f)
# Print model information
# print("Loaded model:", model)
# Define route for index page

def chennai():
    return render_template('chennai.html')

# Handle prediction request
# @app.route('/', methods=['POST'])
def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form['area'])
    if area > 9900 or area <200:
        return render_template("chennai.html" , alert = "Area should be between  range of 200-9900")
    bedrooms = int(request.form['bedrooms'])
    if bedrooms > 9 or bedrooms < 1 :
        return render_template("chennai.html", alert ="Bedrooms should be betweem range of 1-9")
    location = request.form['location']
    club_house = 1 if request.form['club-house'] == 'Yes' else 0
    rain_water_harvesting = 1 if request.form['rain-water-harvesting'] == 'Yes' else 0
    Swimming_Pool = 1 if request.form['Swimming-Pool'] == 'Yes' else 0
    resale = 1 if request.form['resale'] == 'Yes' else 0
    Cafeteria = 1 if request.form['Cafeteria'] == 'Yes' else 0
    Refrigerator = 1 if request.form['Refrigerator'] == 'Yes' else 0
    Shopping_Mall = 1 if request.form['Shopping-Mall'] == 'Yes' else 0
    Jogging_Track = 1 if request.form['Jogging-Track'] == 'Yes' else 0
    Landscaped_Gardens = 1 if request.form['Landscaped-Gardens'] == 'Yes' else 0
    Vaastu_Compliant = 1 if request.form['Vaastu-Compliant'] == 'Yes' else 0
    Multipurpose_Room = 1 if request.form['Multipurpose-Room'] == 'Yes' else 0
    AC = 1 if request.form['AC'] == 'Yes' else 0
    Indoor_Games = 1 if request.form['Indoor-Games'] == 'Yes' else 0
    BED = 1 if request.form['BED'] == 'Yes' else 0
    Sofa = 1 if request.form['Sofa'] == 'Yes' else 0
    Sports_Facility = 1 if request.form['Sports-Facility'] == 'Yes' else 0
    Washing_Machine = 1 if request.form['Washing-Machine'] == 'Yes' else 0

    # Preprocess user input
    location_code = get_location_code(location)

    # Print received form data
    
    # Make prediction
    features = np.array([[area, Jogging_Track, Cafeteria,  rain_water_harvesting,
                          bedrooms, Multipurpose_Room, Refrigerator, Shopping_Mall,
                           Vaastu_Compliant, location_code, Sofa, Swimming_Pool,
                           Indoor_Games, Landscaped_Gardens, BED, club_house,
                            Sports_Facility, resale,Washing_Machine, AC]])
    
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('chennai.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True )
