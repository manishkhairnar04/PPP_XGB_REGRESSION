import pickle
import numpy as np
from flask import  render_template, request
from main_app import app



# Helper function to get location code
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
                 '15th Road': 0,
                 '4 Bunglows':1,
                  'Airoli':9,
                  'Akurli Nagar':10,
                  'Almeida Park':17,
                  'Ambarnath':20,
                  'Ambernath East':23,
                  'Ambernath West':24,
                   'Andheri East':33,
                   'Andheri West':34,
                    'Andheri':32,
                    'Asangaon':44,
                   'azad nagar':824,
                   'Badlapur East':64,
                   'Badlapur West':65,
                   'Badlapur':63,
                   'Bandra East':74,
                   'Bandra West':75,
                   'Belapur':87,
                   'Bhandup West':91,
                   'Bhayandar East':92,
                   'Bhiwandi':93,
                   'Borivali East':104,
                   'Borivali West':105,
                   'Breach Candy':107,
                   'Central Avenue':115,
                   'Chembur East':123,
                   'Chembur Shell Colony':124,
                   'Chembur':122,
                   'Churchgate':142,
                   'Dadar East':148,
                   'Dahisar East': 150,
                  ' Dahisar W ': 151,
                   'Dahisar West':152,
                   'Dahisar':149,
                   'Dattapada':157,
                   'Deonar':158,
                   'Devidas Cross Lane':160,
                   'Diamond Market Road':161,
                   'DN Nagar Road':147,
                   'Dokali Pada':164,
                   'Dombivali East':168,
                   'Dombivali':167,
                   'Dombivli (West)':169,
                   'Dronagiri':172,
                  'Eastern Express Highway Vikhroli':183,
                   'Four Bungalows':191,
                   'Ganesh Nagar':196,
                  'Ghatkopar East':201,
                  'Ghatkopar West':202,
                  'Ghatkopar':200,
                 'Ghodbunder Road':203,
                 'Godrej Hill':204,
                 'Goregaon East':209,
                 'Goregaon West':210,
                 'Goregaon':208,
                 'Haridas Nagar':226,
                 'Haware City':230,
                'Hiranandani Meadows':234,
                 'I C Colony':244,
                 'Jankalyan Nagar':265,
                 'Jogeshwari East':270,
                 'Jogeshwari West':271,
                 'juhu tara':829,
                 'Juhu':274,
                 'Kalpataru':288,
                 'Kalwa':289,
                 'Kalyan East':291,
                'Kalyan West':292,
                 'Kalyan':290,
                 'Kamothe Sector 16':294,
                 'Kamothe':293,
                 'Kandivali East':298,
                 'Kandivali West':299,
                 'kandivali':830,
                 'Kanjurmarg':300,
                 'Karanjade':304,
                 'Kasar vadavali':309,
                 'KASHELI':278,
                 'Kasheli':311,
                 'Katrap':312,
                 'Khar':323,
                 'Kharegaon':324,
                 'Kharghar Sector 34C':326,
                 'Kharghar':325,
                 'Kolshet Road':343,
                 'kolshet':831,
                 'Kopar Khairane Sector 19A':349,
                 'Koparkhairane Station Road':350,
                 'Koper Khairane':351,
                 'Koproli':352,
                 'Kulupwadi':367,
                 'Kurla':372,
                 'Link Road':382,
                 'Lokhandwala Township':383,
                 'Lower Parel':384,
                 'Magathane':397,
                 'Mahalaxmi':398,
                 'Maharashtra Nagar':399,
                 'Mahatma Gandhi Road':400,
                 'Majiwada':404,
                 'Malad East':405,
                 'Malad West':406,
                 'Marol':419,
                 'MHADA Colony 20':385,
                 'Mira Bhayandar':435,
                 'Mira Road and Beyond':438,
                 'Mira Road East':437,
                 'Mira Road':436,
                 'Mulund West':452,
                 'Mulund':451,
                 'Mumbai Agra National Highway':453,
                 'Mumbai Highway':454,
                 'Mumbai Nashik Expressway':455,
                 'mumbai':834,
                 'Nahur':463,
                 'Naigaon East':464,
                 'Nala Sopara':465,
                 'Nalasopara West':466,
                 'Napeansea Road':476,
                 'Natakwala Lane':483,
                 'Navi Basti':485,
                 'Nerul':492,
                 'no 9':839,
                 'Off Shimpoli road':498,
                 'Palghar':510,
                 'Pali Hill':511,
                 'Palm Beach':514,
                 'Panch Pakhadi':516,
                 'Pant Nagar':518,
                 'Panvel':519,
                 'Parel':521,
                 'PARSIK NAGAR':502,
                 'Patlipada':526,
                 'Peddar Road':529,
                 'Petali':536,
                 'Pokharan Road':541,
                 'Pokhran 2':542,
                 'Powai Lake':545,
                 'Prabhadevi':547,
                 'raheja vihar':840,
                 'Ranjanpada':574,
                 'Rawal Pada':575,
                 'Roadpali':580,
                 'Rustomjee Global City':585,
                 'Rutu Enclave':586,
                 'Sahkar Nagar':591,
                 'Samata Nagar Thakur Village':597,
                 'Sanpada':601,
                 'Santacruz West':602,
                 'Seawoods':611,
                 'Sector 10 Khanda Colony':614,
                 'Sector 10':612,
                 'Sector 11 Belapur':615,
                 'Sector 11 Kamothe':617,
                 'Sector 12 A':618,
                 'Sector 12 Kharghar':620,
                 'Sector 15 Kharghar':624,
                 'Sector 15':623,
                 'Sector 17 Ulwe':627,
                 'Sector 18 Kamothe':629,
                 'Sector 18 Kharghar':630,
                 'Sector 18':628,
                 'Sector 19 Kamothe':634,
                 'Sector 19 Kharghar':635,
                 'Sector 20 Kamothe':637,
                 'Sector 20 Kharghar':638,
                 'Sector 21 Kamothe':641,
                 'Sector 21 Kharghar':642,
                 'Sector 21 Ulwe':643,
                 'Sector 22 Kamothe':645,
                 'Sector 23 Ulwe':649,
                 'Sector 30 Kharghar':656,
                 'Sector 30':655,
                 'Sector 35G':657,
                 'Sector 35I Kharghar':658,
                 'Sector 36 Kamothe':659,
                 'Sector 36 Kharghar':660,
                 'Sector 5 Ulwe':664,
                 'Sector 5':662,
                 'Sector 7 Kharghar':667,
                 'Sector-12 Kamothe':670,
                 'Sector12 Kamothe':684,
                 'Sector12 New Panvel':685,
                 'Sector13 Khanda Colony':686,
                 'Sector-13 Kharghar':671,
                 'Sector13 Kharghar':687,
                 'Sector16 Airoli':688,
                 'Sector-18 Ulwe':674,
                 'Sector-26 Taloja':675,
                 'Sector-3 Ulwe':676,
                 'Sector34 A Kharghar':689,
                 'Sector-34B Kharghar':677,
                 'Sector35D Kharghar':690,
                 'Sector-5 Kamothe':678,
                 'Sector-50 Seawoods':679,
                 'Sector-6A Kamothe':680,
                 'Sector-8 Ulwe':682,
                 'Sector9 Kamothe':691,
                 'Shakti Nagar':701,
                 'Shastri Nagar':706,
                 'Shimpoli':708,
                 'Shirgaon':709,
                 'Sindhi Society Chembur':713,
                 'Soniwadi Road':722,
                 'Sunil Nagar':730,
                 'taloja panchanand':843,
                 'Taloja':735,
                 'Tardeo':738,
                 'thakur village kandivali east':845,
                 'Thakurli':744,
                 'Thane West':747,
                 'Thane':746,
                 'Tolaram Colony':760,
                 'TPS Road':733,
                 'ulhasnagar 4':846,
                 'ULWE SECTOR 19':766,
                 'Ulwe':769,
                 'Vakola':780,
                 'Vangani':785,
                 'Vasai east':789,
                 'Vasai West':788,
                 'Vasai':787,
                 'vasant vihar thane west':847,
                 'Vasind':791,
                 'Virar East':801,
                 'Virar West':802,
                 'Virar':800,
                 'Vivek Vidyalaya Marg':804,
                 'Wadala East Wadala':807,
                 'Wadala':806,
                 'West Amardeep Colony':808,
                 'Western Express Highway Kandivali East':813,
                 'Worli South Mumbai':819,
                 'Worli':818,
      
    }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_mumbai.pkl", "rb") as f:
    model = pickle.load(f)
# Print model information
# print("Loaded model:", model)
# Define route for index page
    # @app.route('/')
    # def index():
    #     return render_template('index.html')

def mumbai():
    return render_template('mumbai.html')

# Handle prediction request

def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form['area'])
    if area >9900 or area < 200 :
        return render_template("mumbai.html", alert ="Area should be between  range of 200-9900")
    bedrooms = int(request.form['bedrooms'])
    if bedrooms >9 or bedrooms<1:
        return render_template("mumbai.html", alert ="Bedrooms should be between range of 1-9")
    location = request.form['location']
    Dining_Table = 1 if request.form['Dining-Table'] == 'Yes' else 0
    rain_water_harvesting = 1 if request.form['rain-water-harvesting'] == 'Yes' else 0
    Refrigerator = 1 if request.form['Refrigerator'] == 'Yes' else 0
    BED = 1 if request.form['BED'] == 'Yes' else 0
    Cafeteria = 1 if request.form['Cafeteria'] == 'Yes' else 0
    Microwave = 1 if request.form['Microwave'] == 'Yes' else 0
    Intercom = 1 if request.form['Intercom'] == 'Yes' else 0
    Jogging_track = 1 if request.form['Jogging-Track'] == 'Yes' else 0
    Staff_Quarter = 1 if request.form['Staff-Quarter'] == 'Yes' else 0
    Security = 1 if request.form['24X7-Security'] == 'Yes' else 0
    Multipurpose_Room = 1 if request.form['Multipurpose-Room'] == 'Yes' else 0
    Gas_connection = 1 if request.form['Gas-connection'] == 'Yes' else 0
    Indoor_Games= 1 if request.form['Indoor-Games'] == 'Yes' else 0
    Washing_Machine = 1 if request.form['Washing-Machine'] == 'Yes' else 0
    TV = 1 if request.form['TV'] == 'Yes' else 0
    AC = 1 if request.form['AC'] == 'Yes' else 0
    Gymnasium = 1 if request.form['Gymnasium'] == 'Yes' else 0

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
    features = np.array([[Dining_Table, Refrigerator, Jogging_track, BED, area,
                           AC, rain_water_harvesting, bedrooms, location_code,
                           Washing_Machine, Microwave, Intercom, Gymnasium , TV,
                              Staff_Quarter, Multipurpose_Room, Cafeteria, Indoor_Games,Gas_connection ,
                               Security ]])
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('mumbai.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True)
