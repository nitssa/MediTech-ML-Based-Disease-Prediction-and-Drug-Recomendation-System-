# MediTech: ML-Based Disease Prediction and Drug Recommendation System

## Overview

The **MediTech System** is a machine learning-based application designed to predict diseases based on user symptoms and provide appropriate drug recommendations. This system leverages advanced machine learning models to analyze input data and suggest relevant treatments.

## Features

- **Disease Prediction**: Uses trained machine learning models to predict potential diseases based on symptoms.
- **Drug Recommendation**: Provides suggested medications based on diagnosed conditions.
- **User-Friendly Web Interface**: Allows users to input symptoms easily.
- **Scalable and Extensible**: Can be expanded to include more diseases and medications.
- **Lightweight Deployment**: Built using Flask for seamless hosting and accessibility.

## Project Structure

```
├── data/                   # Dataset used for training and testing
├── notebooks/              # Jupyter notebooks for data analysis and model training
├── models/                 # Trained models
├── static/                 # Static assets for the web app
├── templates/              # HTML templates for the web interface
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies for the project
└── README.md               # Project documentation
```

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Flask
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn (for data visualization)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/nitssa/MediTech-ML-Based-Disease-Prediction-and-Drug-Recomendation-System.git
   cd MediTech-ML-Based-Disease-Prediction-and-Drug-Recomendation-System
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and visit `http://127.0.0.1:5000/` to use the application.

## Usage

1. Enter symptoms in the provided input form.
2. Click the "Predict" button to identify potential diseases.
3. Receive disease predictions along with recommended drugs.

## Model Details

- The prediction model is built using **Scikit-learn** and trained on a dataset of disease-symptom relationships.
- Utilizes classification techniques to identify potential diseases and their corresponding treatments.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them.
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or support, contact Me!
