from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bangalore')
def banglore_view():
    from bangalore_detailed import bangalore
    return bangalore()
# import  and return bangalore is def function 

@app.route('/bangalore/predict', methods=['POST'])
def banglore_predict():
    from bangalore_detailed import predict as ban_pred
    return ban_pred()

@app.route('/chennai')
def chennai_view():
    from chennai_detailed import chennai
    return chennai()

@app.route('/chennai/predict', methods=['POST'])
def chennai_predict():
    from chennai_detailed import predict as chen_pred
    return chen_pred()

@app.route('/mumbai')
def mumbai_view():
    from mumbai_detailed import mumbai
    return mumbai()

@app.route('/mumbai/predict',methods =["POST"])
def  mumbai_predict():
    from mumbai_detailed import predict as mum_pred
    return mum_pred()

@app.route('/delhi')
def delhi_view():
    from delhi_detailed import delhi
    return delhi()

@app.route('/delhi/predict', methods =["POST"])
def  delhi_predict():
    from delhi_detailed import predict as del_pred
    return del_pred()

@app.route('/hyderabad')
def hyderabad_view():
    from hyderabad_detailed import hyderabad
    return hyderabad()

@app.route('/hyderabad/predict', methods =["POST"])
def hyderabad_predict():
    from hyderabad_detailed import predict as hyd_pred
    return hyd_pred()

@app.route('/kolkata')
def kolkata_view():
    from kolkata_detailed import kolkata
    return kolkata()

@app.route('/kolkata/predict', methods =["POST"])
def kolkata_predict():
    from kolkata_detailed import predict as kol_pred
    return kol_pred()



if __name__ == '__main__':

    app.run(debug=True,port=49252 )