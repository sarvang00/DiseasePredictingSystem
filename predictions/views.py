from django.http import request
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from .models import HistoricalData

from datetime import datetime

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def input_data(request):
    symptoms = ['back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine',
                'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach',
                'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation',
                'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs',
                'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool',
                'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs',
                'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails',
                'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips',
                'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints',
                'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness',
                'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine',
                'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)',
                'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain',
                'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum',
                'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion',
                'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen',
                'history of alcohol consumption', 'fluid overload', 'blood in sputum', 'prominent veins on calf',
                'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling',
                'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose',
                'yellow crust ooze']

    context = {
        'symptoms': symptoms,
    }

    return render(request, 'predictions/input_data.html', context=context)


@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def past_data(request):

    user_cases = HistoricalData.objects.all().filter(case_of=request.user.id).order_by('case_reg_date')

    context = {
        'user_cases': user_cases,
    }

    return render(request, 'predictions/past_data.html', context=context)


@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def test_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        symptom1 = request.POST['symptom1']
        symptom2 = request.POST['symptom2']
        symptom3 = request.POST['symptom3']
        symptom4 = request.POST['symptom4']
        symptom5 = request.POST['symptom5']

        # diseases
        import random
        diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine', 'Cervical spondylosis','Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'Hepatitis-A', 'Hepatitis-B', 'Hepatitis-C', 'Hepatitis-D', 'Hepatitis-E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis', 'Impetigo']
        
        # dummy logic for prediction
        pr1 = random.randint(0, (len(diseases)-1))
        pr2 = random.randint(0, (len(diseases)-1))
        pr3 = random.randint(0, (len(diseases)-1))
        
        # predicted_disease
        predicted_disease = diseases[pr1] + ', ' + diseases[pr2] + ', '+diseases[pr3]

        filed_case = HistoricalData(case_of=request.user, name=name, age=age, gender=gender, symptom_1=symptom1, symptom_2=symptom2,
                                    symptom_3=symptom3, symptom_4=symptom4, symptom_5=symptom5, predicted_disease=predicted_disease)
        filed_case.save()

        messages.success(request, 'Your filing has been submitted.')

        return redirect('input_data')
