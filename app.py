import streamlit as st
import pickle
import numpy as np

# Load the crop recommendation model
@st.cache_resource
def load_crop_model():
    model_path = "/Users/mac/Downloads/Model/model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

model = load_crop_model()

# Predict the most suitable crop using updated logic
def recommendation(N, P, K, temperature, humidity, ph, rainfall):
    input_arr = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    return model.predict(input_arr)  # Directly returns class label(s)

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Sidebar
st.sidebar.title("Crop Recommendation System")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Crop Recommendation"])

# Main Page
if app_mode == "Home":
    st.header("CROP RECOMMENDATION SYSTEM")
    st.markdown("""
    Welcome to the Crop Recommendation System! 🌾🔍
    
    Our mission is to help farmers and gardeners in selecting the most suitable crops based on soil and climate conditions. Enter the values for various features and our system will recommend the best crop to plant.

    ### How It Works
    1. **Enter Features:** Go to the **Crop Recommendation** page and enter the values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.
    2. **Analysis:** Our system will process the input using advanced algorithms to recommend the most suitable crop.
    3. **Results:** View the recommended crop and take action accordingly.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate crop recommendations.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Crop Recommendation** page in the sidebar to enter the features and get crop recommendations!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Crop Recommendation System
    This system is designed to assist farmers and gardeners in selecting the most suitable crop based on soil and climate conditions. By providing values for Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall, our model can accurately predict the best crop to plant.

    The model has been trained on a large dataset of soil and climate conditions with corresponding crop yields, ensuring high accuracy and reliability in its recommendations.
    """)

elif app_mode == "Crop Recommendation":
    st.header("Crop Recommendation")

    # Input features
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, max_value=400.0, value=0.0)
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, max_value=500.0, value=0.0)
    potassium = st.number_input("Potassium (K)", min_value=0.0, max_value=500.0, value=0.0)
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=900.0, value=100.0)

    if st.button("Recommend Crop"):
        predict = recommendation(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
        predicted_label = predict[0]

        if predicted_label in crop_dict:
            crop = crop_dict[predicted_label]
            st.success(f"{crop} is the best crop to be cultivated.")
        else:
            st.error("Sorry, we are not able to recommend a proper crop for this environment.")

