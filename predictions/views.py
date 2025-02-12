from django.shortcuts import render
import joblib
import torch
import torch.nn as nn
import numpy as np
import re
from django.template.defaulttags import register



stop_words = [
    'a', 'about', 'after', 'all', 'also', 'an', 'and', 'any', 'as', 'at',
    'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'does', 'did', 'done',
    'dont', 'even', 'find', 'first', 'for', 'from', 'get', 'give', 'go', 'have', 'has', 'had',
    'he', 'her', 'here', 'him', 'his', 'how', 'i', 'ive', 'im', 'if', 'in', 'into',
    'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many',
    'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one',
    'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she',
    'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them',
    'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those',
    'time', 'to', 'two', 'up', 'use', 'very', 'want', 'was', 'way', 'we', 'well',
    'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you',
    'your'
]

# Define the architecture of the drug recommendation model
class DrugRecommendationModel(nn.Module):
    def __init__(self):
        super(DrugRecommendationModel, self).__init__()
        self.fc1 = nn.Linear(75160, 100)
        self.dropout1 = nn.Dropout(0.25)
        self.fc2 = nn.Linear(100, 100)
        self.dropout2 = nn.Dropout(0.25)
        self.fc3 = nn.Linear(100, 3264)

    def forward(self, x):
        x = self.dropout1(torch.relu(self.fc1(x)))
        x = self.dropout2(torch.relu(self.fc2(x)))
        x = self.fc3(x)
        return x



# Custom symptoms list
custom_symptoms = [
    "fever", "cough", "headache", "nausea", "fatigue", "chills", "sore throat", 
    "loss of smell", "loss of taste", "muscle pain", "diarrhea", "rash", 
    "shortness of breath", "chest pain", "dizziness", "vomiting", "congestion", 
    "runny nose", "sneezing", "stiff neck", "blurred vision", "weight loss"
]



def predict_disease(request):
    disease = None
    drugs = []
    
    # Load models, vectorizer, and feature names here
    # Load the disease prediction model
    disease_model_path = 'predictions/Notebook/disease_prediction_model.pkl'
    disease_model = joblib.load(disease_model_path)

    # Load the drug recommendation model
    drug_model_path = 'predictions/Notebook/model.pt'

    # Load the vectorizer and feature names for drug recommendation
    vectorizer_path = 'predictions/Notebook/vectorizer.pkl' 
    feature_names_path = 'predictions/Notebook/feature_names.pkl' 
    vectorizer = joblib.load(vectorizer_path)
    feature_names = joblib.load(feature_names_path)

    drug_model = DrugRecommendationModel()
    drug_model.load_state_dict(torch.load(drug_model_path, map_location=torch.device("cpu")))
    drug_model.eval()

    if request.method == "POST":
        symptoms = [request.POST.get(f"symptom{i}") for i in range(1, 6)]
        selected_symptoms = [symptom for symptom in symptoms if symptom]

        # Server-side validation
        if len(selected_symptoms) < 5:
            return render(request, "predictions/predict.html", {
                "range": range(1,6),
                "symptom_choices": custom_symptoms,
                "error_message": "Kindly fill up 5 symptoms"
            })

        # Disease prediction
        input_features_disease = [1 if s in selected_symptoms else 0 for s in custom_symptoms]
        disease = disease_model.predict([input_features_disease])[0]

        # Drug recommendation processing
        input_text = ' '.join(selected_symptoms).lower()
        input_text = input_text.replace("&#039;", "'").replace("&amp;", ' ').replace("&quot;", ' ')
        input_text = re.sub(r'[^A-Za-z ]+', '', input_text)
        filtered_tokens = [word for word in input_text.split() if word not in stop_words]
        processed_text = ' '.join(filtered_tokens)

        # Vectorize
        input_features_drug = vectorizer.transform([processed_text])
        input_dense = input_features_drug.toarray()
        input_tensor = torch.tensor(input_dense, dtype=torch.float32)

        # Predict drugs
        with torch.no_grad():
            output = drug_model(input_tensor)
        probabilities = torch.softmax(output, dim=1)
        top_indices = torch.topk(probabilities, k=3).indices[0].numpy()
        drugs = [feature_names[idx] for idx in top_indices]

        return render(request, "predictions/result.html", {"disease": disease, "drugs": drugs})
    
    return render(request, "predictions/predict.html", {"range": range(1,6), "symptom_choices": custom_symptoms})
