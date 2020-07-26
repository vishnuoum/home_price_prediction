from flask import Flask, render_template,request,jsonify
import json
import joblib
import util


app = Flask(__name__)


@app.route('/')
def sessions():
    return render_template('client.html')




@app.route('/get_loc', methods=['POST'])
def get_loc():
    return json.dumps(util.get_loc())


@app.route('/estimate', methods=['POST'])
def estimate():
    if request.method=="POST":
        area=request.form.get('area')
        sqft=request.form.get('sqft')
        bed=request.form.get('bed')
        bath=request.form.get('bath')
        result=util.estimate([area,sqft,bed,bath])
    return result






if __name__ == '__main__':
    # socketio.run(app, debug=True,host="192.168.42.229")
    app.run()