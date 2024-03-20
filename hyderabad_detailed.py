import pickle
import numpy as np
from flask import render_template, request
from main_app import app



# Helper function to get location code
def get_location_code(location):
    # Define the mapping of locations to integers
    location_mapping = {
                   'Abids': 4,       
                   'Adda Gutta':6,
                   'Adibatla': 7,
                   'Alapathi Nagar':13,
                   ' ALIND Employees Colony':2,
                   ' Alkapur township':14,
                   ' Allwyn Colony':15,
                   ' Almasguda':16,
                   ' Alwal':18,
                   ' Ambedkar Nagar':22,
                   ' Amberpet':25,
                   ' Ameenpur':26,
                   ' Ameerpet':27,
                   ' Aminpur':29,
                   ' Appa Junction Peerancheru':42,
                   ' Appa Junction':41,
                   ' Arvind Nagar Colony' :43,
                   ' AS Rao Nagar':3,
                   ' Ashok Nagar':45,
                   ' Attapur':47,
                   ' Aushapur':49,
                   ' Bachupally Road':60,
                   ' Bachupally':59,
                   ' Bachupaly Road Miyapur':61,
                   ' Bagh Amberpet':66,
                   ' Baghlingampally':67,
                   ' Balanagar':69,
                   ' Balapur':70,
                   ' Bandlaguda Jagir':73,
                   ' Banjara Hills Road Number 12':77,
                   ' Banjara Hills':76,
                   ' Barkatpura':80,
                   ' Basheer Bagh':81,
                   ' Beeramguda Road':83,
                   ' Beeramguda':82,
                   ' Begumpet': 84,
                   ' BHEL': 54,
                   ' BK Guda Internal Road':55,
                   ' BK Guda Road':56,
                   ' Boduppal':97,
                   ' Boiguda':98,
                   ' Bolarum':99,
                   ' Bollaram':100,
                   ' Bongloor':103,
                   ' Bowenpally':106,
                   ' Central Excise Colony Hyderabad':116,
                   ' Chaitanyapuri':117,
                   ' Chandanagar':118,
                   ' chandrayangutta':825,
                   ' Cherlapalli':126,
                   ' Chikkadapally':128,
                   ' Chintalakunta':131,
                   ' Chintalmet':132,
                   ' Chinthal Basthi':133,
                   ' Chintradripet':134,
                   ' Chititra Medchal':135,
                   ' D D Colony':143,
                   ' Dammaiguda':153,
                   ' Darga Khaliz Khan':154,
                   ' DD Colony':144,
                   ' Dilsukh Nagar':162,
                   ' Domalguda Road':166,
                   ' Domalguda':165,
                   ' Dr A S Rao Nagar Rd':171,
                   ' Dullapally':173,
                   ' East Marredpally':180,
                   ' ECIL Cross Road':178,
                   ' ECIL Main Road':179,
                   ' ECIL':177,
                   ' Film Nagar':190,
                   ' financial District':826,
                   ' Gachibowli':192,
                   ' Gajularamaram':193,
                   ' Gajulramaram Kukatpally':194,
                   ' Gandipet':195,
                   ' Ghansi Bazaar':199,
                   ' Gopal Nagar':205,
                   ' Gopanpally':207,
                   ' Habsiguda':221,
                   ' Hafeezpet':222,
                   ' Hakimpet':223,
                   ' Happy Homes Colony':224,
                   ' Hastinapur':228,
                   ' Himayat Nagar':233,
                   ' Hitech City':235,
                   ' Hitex Road':236,
                   ' HMT Hills':220,
                   ' Hyder Nagar':242,
                   ' hyderabad':828,
                   ' Hydershakote':243,
                   ' IDPL Colony':245,
                   ' Isnapur':249,
                   ' Jhangir Pet':268,
                   ' JNTU':253,
                   ' Jubilee Hills':273,
                   ' Kachiguda':283,
                   ' Kapra':303,
                   ' Karimnagar':306,
                   ' Karmanghat':307,
                   ' Kavuri Hills':317,
                   ' Khajaguda Nanakramguda Road':321,
                   'Khizra Enclave':328,
                   'Kismatpur':332,
                   'Kistareddypet':333,
                   'Kokapet':337,
                   'Kokapeta Village':338,
                   'Kollur Road':342,
                   'Kollur':341,
                   'Kompally':344,
                   'Kondakal':346,
                   'Kondapur':347,
                   'Kothaguda':355,
                   'Kothapet':357,
                   'Kowkur':361,
                   'KPHB':280,
                   'KRCR Colony Road':281,
                   'Krishna Reddy Pet':363,
                   'KTR Colony':282,
                   'Kukatpally':366,
                   'Kushaiguda':373,
                   'Lakdikapul':379,
                   'LB Nagar':376,
                   'Lingampalli':381,
                   'Macha Bolarum':386,
                   'Madhapur':388,
                   'Madhavaram Nagar Colony':390,
                   'Madhura Nagar':391,
                   'Madinaguda':393,
                   'Mailardevpally':403,
                   'Malkajgiri':407,
                   'Mallampet':408,
                   'Mallapur':409,
                   'Manikonda':413,
                   'manneguda':832,
                   'Mansoorabad':416,
                   'Masab Tank':421,
                   'Matrusri Nagar':423,
                   'Mayuri Nagar':426,
                   'Medchal':428,
                   'Meerpet':429,
                   'Mehdipatnam':430,
                   'Methodist Colony':432,
                   'Mettuguda':433,
                   'Miyapur Bachupally Road':440,
                   'Miyapur HMT Swarnapuri Colony':441,
                   'Miyapur':439,
                   'Moosapet':445,
                   'Moti Nagar':446,
                   'Moula Ali':447,
                   'Murad Nagar':458,
                   'muthangi':835,
                   'Nacharam':460,
                   'Nagole':462,
                   'Nallagandla Gachibowli':467,
                   'Nallagandla Road':468,
                   'Nallakunta':469,
                   'Nanakramguda':470,
                   'Nandagiri Hills':471,
                   'Narayanguda':479,
                   'Narsingi':481,
                   'Neknampur':488,
                   'Neredmet':491,
                   'New Maruthi Nagar':494,
                   'new nallakunta':837,
                   'nizampet road':838,
                   'Nizampet':496,
                   'NRSA Colony':459,
                   'Old Alwal':499,
                   'Old Bowenpally':500,
                   'Old Nallakunta':501,
                   'Padma Colony':504,
                   'Padmarao Nagar':506,
                   'Panchavati Colony Manikonda':517,
                   'Paramount Colony Toli Chowki':520,
                   'Patancheru Shankarpalli Road':524,
                   'Patancheru':523,
                   'Pati':525,
                   'Picket':537,
                   'Pocharam':540,
                   'Pragathi Nagar Kukatpally':549,
                   'Pragathi Nagar Road':550,
                   'Pragathi Nagar':548,
                   'Pragati Nagar':551,
                   'Puppalaguda':552,
                   'Quthbullapur':555,
                   'Qutub Shahi Tombs':556,
                   'raidurgam':841,
                   'Rajbhavan Road Somajiguda':566,
                   'Rajendra Nagar':567,
                   'Rakshapuram':568,
                   'Ramachandra Puram':569,
                   'Ramnagar Gundu':573,
                   'Residential Flat Machavaram':576,
                   'Rhoda Mistri Nagar':577,
                   'Ring Road':579,
                   'Safilguda':589,
                   'Sainikpuri':595,
                   'Saket':596,
                   'Sanath Nagar':598,
                   'Sangeet Nagar':599,
                   'Santoshnagar':603,
                   'Saroornagar':608,
                   'Secunderabad Railway Station Road':692,
                   'Serilingampally':696,
                   'Shadnagar':698,
                   'Shaikpet':700,
                   'Shamshabad':703,
                   'Shankarpalli':704,
                   'Sikh Village':712,
                   'Somajiguda':720,
                   'Sri Nagar Colony':724,
                   'Srisailam Highway':725,
                   'Suchitra':727,
                   'Sun City Padmasri Estates':729,
                   'Sun City':728,
                   'Tarnaka':739,
                   'Tellapur':740,
                   'TellapurOsman Nagar Road':741,
                   'Tilak Nagar':757,
                   'Tirumalgiri':758,
                   'Toli Chowki':761,
                   'Tolichowki':762,
                   'Trimalgherry':764,
                   'Tukkuguda Airport View Point Road':765,
                   'Uppal Kalan':771,
                   'Uppal':770,
                   'Uppalguda':772,
                   'Usman Nagar':774,
                   'Vanasthalipuram':783,
                   'Venkat Nagar Colony':796,
                   'Vidyanagar Adikmet':797,
                   'Vivekananda Nagar Colony':805,
                   'West Marredpally':810,
                   'west venkatapuram':848,
                   'Whisper Valley':814,
                   'Whitefields':817,
                   'Yapral':820,
                   'Zamistanpur':823,


    }
    # Return the integer code for the given location, or 0 if location not found
    return location_mapping.get(location, 0)


# Load the trained model
with open("models/best_xgb_hyderabad.pkl", "rb") as f:
    model = pickle.load(f)
# Print model information
# print("Loaded model:", model)
# Define route for index page

def hyderabad():
    return render_template('hyderabad.html')

# Handle prediction request

def predict():
    print("Prediction endpoint triggered")
    # Get user input from the form
    area = int(request.form['area'])
    if area >9900 or area < 200 :
        return render_template("hyderabad.html", alert ="Area should be between  range of 200-9900")
    bedrooms = int(request.form['bedrooms'])
    if bedrooms >9 or bedrooms<1:
        return render_template("hyderabad.html", alert ="Bedrooms should be between range of 1-9")
    location = request.form['location']
    club_house = 1 if request.form['club-house'] == 'Yes' else 0
    BED = 1 if request.form['BED'] == 'Yes' else 0
    Swimming_Pool = 1 if request.form['swimming-pool'] == 'Yes' else 0
    resale = 1 if request.form['resale'] == 'Yes' else 0
    cafeteria = 1 if request.form['Cafeteria'] == 'Yes' else 0
    Lift_Available = 1 if request.form['Lift-Available'] == 'Yes' else 0
    Maintenance_Staff = 1 if request.form['Maintenance-Staff'] == 'Yes' else 0
    School = 1 if request.form['School'] == 'Yes' else 0
    Landscaped_Gardens = 1 if request.form['Landscaped-Gardens'] == 'Yes' else 0
    ATM = 1 if request.form['ATM'] == 'Yes' else 0
    Multipurpose_Room = 1 if request.form['Multipurpose-Room'] == 'Yes' else 0
    AC = 1 if request.form['AC'] == 'Yes' else 0
    Indoor_Games = 1 if request.form['Indoor-Games'] == 'Yes' else 0
    Intercom = 1 if request.form['Intercom'] == 'Yes' else 0
    Car_Parking = 1 if request.form['Car-Parking'] == 'Yes' else 0
    Gas_Connection = 1 if request.form['Gas-connection'] == 'Yes' else 0
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
    features = np.array([[area, resale, BED, Swimming_Pool, club_house,
                         gymnasium, Car_Parking, Lift_Available, Landscaped_Gardens,
                         Indoor_Games, Multipurpose_Room, ATM, location_code,
                          Maintenance_Staff , School, cafeteria, bedrooms,
                            Gas_Connection, AC, Intercom]])
    predicted_price = model.predict(features)[0]
    print("Predicted Price:", predicted_price)

    # Return prediction result
    return render_template('hyderabad.html', predicted_price=predicted_price)


if __name__ == '__main__':

    app.run(debug=True)
