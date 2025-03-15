from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and label encoders
gb_model = joblib.load("gradient_boosting_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Get dropdown options from the label encoders
locations = list(label_encoders["Location"].classes_)
soil_types = list(label_encoders["Soil_Type"].classes_)
seasons = list(label_encoders["Season"].classes_)

@app.route('/')
def home():
    return render_template('index.html', locations=locations, soil_types=soil_types, seasons=seasons)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        area = float(request.form['area'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        soil_type = request.form['soil_type']
        nitrogen = int(request.form['nitrogen'])
        phosphorus = int(request.form['phosphorus'])
        potassium = int(request.form['potassium'])
        humidity = float(request.form['humidity'])
        season = request.form['season']
        location = request.form['location']

        # Encode categorical values
        location_encoded = label_encoders["Location"].transform([location])[0]
        soil_type_encoded = label_encoders["Soil_Type"].transform([soil_type])[0]
        season_encoded = label_encoders["Season"].transform([season])[0]

        # Create DataFrame for prediction
        input_data = pd.DataFrame([[location_encoded, area, rainfall, temperature, soil_type_encoded,
                                    nitrogen, phosphorus, potassium, humidity, season_encoded]],
                                  columns=['Location', 'Area', 'Rainfall', 'Temperature', 'Soil_Type',
                                           'Nitrogen', 'Phosphorus', 'Potassium', 'Humidity', 'Season'])

        # Predict yield
        predicted_yield = gb_model.predict(input_data)[0]

        return render_template('index.html', prediction=f"🌾 Estimated Yield: {predicted_yield:.2f} kg/ha",
                               locations=locations, soil_types=soil_types, seasons=seasons)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}",
                               locations=locations, soil_types=soil_types, seasons=seasons)

if __name__ == '__main__':
    app.run(debug=True)
