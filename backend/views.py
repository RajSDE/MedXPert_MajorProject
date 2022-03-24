from django.shortcuts import render
import joblib
import numpy as np

# Create your views here.

def home(request):
    return render(request, 'index.html')
def diagnosis(request):
    return render(request,'diagnosis.html')
def liver(request):
    return render(request,'liver.html')


def ValuePredictor(to_predict_list,size,model_name):
    mdname = str(model_name)
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        trained_model = joblib.load(rf'{mdname}_model.pkl')
        result = trained_model.predict(to_predict)
    return result[0]

def lpredictor(request):
    mname = "liver"
    llis = []
    llis = [request.POST.get(i, False) for i in ('Total Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio')]
 
    if(len(llis)==7):
            result = ValuePredictor(llis,7,mname)
 
    if(int(result)==1):
        return render(request,'risk.html')
    else:
        return render(request,'norisk.html')