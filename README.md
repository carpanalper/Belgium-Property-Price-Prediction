# Belgium Property Price Prediction App

## Overview
This project is a Streamlit application designed to predict property prices in Belgium. Users can input various features of a property, and the app uses pre-trained machine learning models to estimate the property's market value.

## Live Demo
The application is deployed and can be accessed [here](https://belgium-property-price-prediction.onrender.com/).

## Features
- **Property Type**: Choose between House or Apartment.
- **Living Area**: Input the size of the living area in square meters.
- **Bedroom and Bathroom Count**: Specify the number of bedrooms and bathrooms.
- **Surface of Plot**: Enter the size of the plot in square meters.
- **Construction Year**: Select the year the property was constructed.
- **Kitchen Type**: Choose the type of kitchen (e.g., installed, semi-equipped).
- **Condition Rating**: Rate the condition of the property using emojis.
- **PEB Rating**: Select the PEB (Energy Performance Certificate) rating.
- **Location Details**: Choose the province and district of the property.
- **Amenities**: Indicate whether the property is furnished and if it has a garden, swimming pool, or terrace.

## How to Run the App

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/belgium-property-price-prediction.git
   cd belgium-property-price-prediction
   ```

2. **Install Dependencies**
   Make sure you have Python installed and then install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   You can run the Streamlit app using the following command:
   ```bash
   streamlit run app.py
   ```

4. **Access the App Locally**
   Open your web browser and go to `http://localhost:8501` to access the property price prediction app.

## Deployment
The application is deployed on Render, and you can access it using the following link: [Belgium Property Price Prediction App](https://belgium-property-price-prediction.onrender.com/).

## Model Details
The app uses the following models for prediction:
- **XGBoost Regressor**: The model is pre-trained and loaded into the application using `pickle`.

## Preprocessing
The input data is processed and scaled using a pre-trained `StandardScaler`. Additionally, some features undergo log transformation to improve model performance.

## Rank Dictionaries
The application uses various rank dictionaries to convert qualitative inputs into numerical representations, which include:
- Condition ranks
- PEB ranks
- Kitchen ranks
- District and province ranks

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any enhancements or bug fixes.

## Acknowledgments

- **BeCode Cohorts**: A special thank you to my coaches and classmates at BeCode for their invaluable support, guidance, and collaboration throughout this project. Your encouragement and teamwork have greatly enriched my learning experience.
- **Streamlit**: For providing a simple way to create web applications for machine learning.
- **Scikit-learn**: For the machine learning tools used in this project.
