# Crop Recommendation System

A web-based machine learning application to recommend the most suitable crop to cultivate based on soil and climate conditions. Built with **Streamlit** and powered by a **machine learning model** trained on agricultural data.

---

## Features

- Predicts the best crop using features like Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, and Rainfall.
- Easy-to-use web interface built with Streamlit.
- Instant prediction results.
- Model trained on real-world crop and environmental data.

---

## Tech Stack

- Python  
- Streamlit  
- scikit-learn / machine learning  
- NumPy  
- Pickle (for model serialization)  

---

## Project Structure

```
Crop-Recommendation-System/
├── model.pkl          # Trained ML model
├── app.py             # Streamlit web application
├── README.md          # Project documentation
```

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit 
   ```

   Or manually install required packages:
   ```bash
   pip install streamlit numpy scikit-learn
   ```

3. **Ensure your `model.pkl` file is placed correctly**:  
   Replace the `model_path` in `app.py` with the correct local path to your `model.pkl`.

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. Open the provided URL (usually `http://localhost:8501`) in your browser to use the app.


---

## 🔍 Input Parameters

| Feature       | Description                        |
|---------------|------------------------------------|
| Nitrogen (N)  | Nitrogen content in the soil       |
| Phosphorus (P)| Phosphorus content in the soil     |
| Potassium (K) | Potassium content in the soil      |
| Temperature   | In degrees Celsius                 |
| Humidity      | Percentage of air moisture         |
| pH            | Acidity/Alkalinity of the soil     |
| Rainfall      | In millimeters                     |

---

## Supported Crop Predictions

- Rice  
- Maize  
- Jute  
- Cotton  
- Coconut  
- Papaya  
- Orange  
- Apple  
- Muskmelon  
- Watermelon  
- Grapes  
- Mango  
- Banana  
- Pomegranate  
- Lentil  
- Blackgram  
- Mungbean  
- Mothbeans  
- Pigeonpeas  
- Kidneybeans  
- Chickpea  
- Coffee  

---

## 👨‍💻 Author

**Aman Singh Chauhan**  


---

## 🌟 Acknowledgments

- Dataset: [Kaggle Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- Inspired by precision agriculture needs and climate-based farming tools.
