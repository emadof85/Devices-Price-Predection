from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the model and scaler
svc_model = joblib.load('models/svc_best_model.pkl')
scaler = joblib.load('models/qt_scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['battery_power'], data['blue'], data['clock_speed'], data['dual_sim'],
                         data['fc'], data['four_g'], data['int_memory'], data['m_dep'], data['mobile_wt'],
                         data['n_cores'], data['pc'], data['px_height'], data['px_width'], data['ram'],
                         data['sc_h'], data['sc_w'], data['talk_time'], data['three_g'], data['touch_screen'],
                         data['wifi']]).reshape(1, -1)
    features = scaler.transform(features)
    prediction = svc_model.predict(features)
    return jsonify({'price_range': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
