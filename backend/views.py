from django.shortcuts import render
import joblib
import numpy as np

# ------------------- Rendering Pages -------------------------- #

def home(request):
    return render(request, 'index.html')
def diagnosis(request):
    return render(request,'diagnosis.html')
def liver(request):
    return render(request,'liver.html')
def kidney(request):
    return render(request,'kidney.html')
def heart(request):
    return render(request,'heart.html')
def diabetes(request):
    return render(request,'diabetes.html')
def service(request):
    return render(request,'service.html')


# ------------------- XXXXXXXXXXXXXX -------------------------- #


# ------------------- General Function for All Models -------------------------- #

def ValuePredictor(to_predict_list,size,model_name):
    mdname = str(model_name)
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        trained_model = joblib.load(rf'{mdname}_model.pkl')
        result = trained_model.predict(to_predict)
    return result[0]

# ------------------- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -------------------------- #






# ------------------- Liver Disease -------------------------- #

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


# ------------------- Disease End --------------------------- #







# ------------------- Kidney Disease ------------------------ #

def kdpredictor(request):
    mname = "kidney"
    klis = []
    klis = [request.POST.get(i, False) for i in ('Year', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc')]
 
    if(len(klis)==7):
            result = ValuePredictor(klis,7,mname)
 
    if(int(result)==1):
        return render(request,'risk.html')
    else:
        return render(request,'norisk.html')

# ------------------- Disease End ------------------------- #








# ------------------- Heart Disease ----------------------- #

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

def HeartPredictor(to_predict_list,size,model_name):
    heart = pd.read_csv('./MachineLearningModels/DataSets/heartdataNew.csv')
    labels = heart['target']
    features = heart.drop(['target'], axis = 1)
    features_train , features_test, labels_train, labels_test = train_test_split(features, labels, test_size= 0.3, random_state=2)
    logisticRegression = LogisticRegression( solver='lbfgs')
    logisticRegression.fit(features_train,labels_train)
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==7):
        result = logisticRegression.predict(to_predict)
    return result[0]

def hdpredictor(request):
    mname = "heart"
    hlis = []
    hlis = [request.POST.get(i, False) for i in ('cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang')]    
    if(len(hlis)==7):
        result = HeartPredictor(hlis,7,mname)
    
    if(int(result)==1):
        return render(request,'risk.html')
    else:
        return render(request,'norisk.html')

# ------------------- Heart End -------------------------- #







# ------------------- Diabetes Disease ----------------------- #

def dbpredictor(request):
    dblis = []
    dblis.append(request.POST['Pregnancies'])
    dblis.append(request.POST['Present_Price'])
    dblis.append(request.POST['BloodPressure'])
    dblis.append(request.POST['BMI']) 
    dblis.append(request.POST['DiabetesPedigreeFunction'])
    dblis.append(request.POST['Age'])   
    if(len(dblis)==6):
        result = DiabetesValuePredictor(dblis,6)
    
    if(int(result)==1):
        return render(request,'risk.html')
    else:
        return render(request,'norisk.html')


# Sample Machine Learning Code for diabetes prediction

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
diabetes_dataset = pd.read_csv('./diabetes.csv')

def DiabetesValuePredictor(to_predict_list,size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
    Y = diabetes_dataset['Outcome']
    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)
    X = standardized_data
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
    
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)
    
    # to_predict = np.array(to_predict_list).reshape(1,size)
    
    if(size==6):
        # trained_model = joblib.load(r'diabetes_model.pkl')
        # trained_model = pd.(r'diabetes_model.pkl')
        # result = trained_model.predict(to_predict)
        std_data = scaler.transform(to_predict)
        result = classifier.predict(std_data)
    return result[0]

# ------------------- Diabetes End ----------------------- #

 
