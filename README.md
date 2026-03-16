# Soybean Yield Prediction System (Bidar District)

A Machine Learning based system that predicts soybean crop yield using environmental and soil parameters. The model uses agricultural data from Bidar district, Karnataka to estimate expected yield and assist in better farming decisions.

---

## Project Overview

Agriculture plays a crucial role in India's economy, and accurate crop yield prediction can help farmers and planners make better decisions. This project focuses on predicting **soybean yield** using machine learning techniques based on various environmental and soil conditions.

The system analyzes parameters such as rainfall, temperature, soil nutrients, humidity, and location to estimate crop yield.

---

## Objectives

- Predict soybean crop yield using machine learning algorithms.
- Analyze the impact of environmental and soil parameters on crop production.
- Provide a simple system that can assist in agricultural planning.

---

## Dataset Features

The dataset used for training the model contains the following attributes:

- **Location** – Taluks in Bidar District
- **Area** – Area of cultivation
- **Rainfall (mm)** – Average rainfall
- **Temperature (°C)** – Average temperature
- **Soil Type** – Type of soil in the region
- **Nitrogen (N)** – Nitrogen content in soil
- **Phosphorus (P)** – Phosphorus content in soil
- **Potassium (K)** – Potassium content in soil
- **Humidity (%)** – Environmental humidity
- **Season** – Crop season
- **Yield** – Crop yield (target variable)

---

## Technologies Used

- **Python**
- **Flask** – Web framework for building the application
- **Machine Learning Algorithms**
- **Pandas & NumPy** – Data processing
- **Scikit-learn** – Model building
- **Matplotlib / Seaborn** – Data visualization
- **HTML / CSS / JavaScript** – Frontend interface

---

## System Workflow

1. Data collection and dataset preparation
2. Data preprocessing and feature selection
3. Training machine learning models
4. Evaluating model performance
5. Integrating the trained model with a Flask web application
6. Users enter input parameters through the web interface
7. The system predicts the soybean yield

---

## How to Run the Project

1. Clone the repository
git clone https://github.com/your-username/soybean-yield-prediction-bidar-ml.git

2. Navigate to the project folder
cd soybean-yield-prediction-bidar-ml

3. Install required dependencies
pip install -r requirements.txt

4. Run the Flask application
python app.py

5. Open the browser and go to
http://127.0.0.1:5000

---

## Future Improvements

- Use larger real-world agricultural datasets
- Integrate weather API for real-time predictions
- Deploy the system as a full web application
- Add support for multiple crops

---

## Author

**Srujan M S**  
MCA Student

---

## License

This project is developed for academic and research purposes.
