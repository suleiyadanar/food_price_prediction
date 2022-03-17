from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location/')
def get_location():
    response=jsonify({
        'locations':util.get_location()
    })
    response.headers.add
    return response
@app.route('/predict_price/', methods=['POST'])
def predict_price():
    location = request.form['location']
    commodity = int(request.form['commodity'])
    sales_category = int(request.form['category'])
    response = jsonify({
        'estimated_price':util.get_price_estimate(location,commodity,sales_category)
    })
if __name__ == "__main__":
    print("Starting Python ")
    app.run()
