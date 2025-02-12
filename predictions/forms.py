
from django import forms

SYMPTOM_CHOICES = [
    ('Fever', 'Fever'), 
    ('Cough', 'Cough'), 
    ('Fatigue', 'Fatigue'), 
    ('Headache', 'Headache'), 
    ('Sore Throat', 'Sore Throat'),
    ('Shortness of Breath', 'Shortness of Breath'),
    ('Runny Nose', 'Runny Nose'),
    ('Loss of Taste or Smell','Loss of Taste or Smell'),
    ('Diarrhea','Diarrhea'),
    ('Nausea','Nausea'),
    ('Vomiting','Vomiting'),
    ('Chest Pain','Chest Pain'),
    ('Abdominal Pain','Abdominal Pain'),
    ('Joint Pain','Joint Pain'),
    ('Skin Rash','Skin Rash'),
    ('Swelling','Swelling'),
    ('High Blood Pressure','High Blood Pressure'),
    ('Low Blood Pressure','Low Blood Pressure'),
    ('Confusion','Confusion'),
    ('Vision Problems','Vision Problems'),
    ('Weight Loss','Weight Loss'),
    ('Muscle Pain','Muscle Pain'),


    
]

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=SYMPTOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select your symptoms"
    )
