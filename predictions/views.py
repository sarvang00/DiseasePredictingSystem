from django.http import request
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from .models import HistoricalData

from datetime import datetime

# Create your views here.
def input_data(request):
    symptoms=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    context = {
        'symptoms': symptoms,
    }

    return render(request, 'predictions/input_data.html', context=context)

def past_data(request):

    user_cases = HistoricalData.objects.all().filter(case_of=request.user.id).order_by('case_reg_date')

    context={
        'user_cases': user_cases,
    }

    return render(request, 'predictions/past_data.html', context=context)

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

        # predicted_disease=prediction
        predicted_disease = ''
        
        filed_case = HistoricalData(case_of=request.user, name=name, age=age, gender=gender, symptom_1=symptom1, symptom_2=symptom2, symptom_3=symptom3, symptom_4=symptom4, symptom_5=symptom5, predicted_disease=predicted_disease)
        filed_case.save()

        messages.success(request, 'Your filing has been submitted.')
        
        return redirect('input_data')