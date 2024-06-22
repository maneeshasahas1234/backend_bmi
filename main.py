from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate',methods=['POST'])
def cal_bmi():
    data = request.get_json()
    weight = float(data['weight'])
    height = float(data['height'])/100
    bmi = weight/(height ** 2)
    return jsonify(bmi)

if __name__ == '__main__':
    app.run(debug=True)

