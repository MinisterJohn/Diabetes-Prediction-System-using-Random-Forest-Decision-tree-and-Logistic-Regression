from django.shortcuts import render
from django.http import HttpResponse
import joblib
# Create your views here.
def home(request):
  return render(request, 'home.html')

def login(request):
  return render(request, 'login.html')

def result(request):
    cls = joblib.load('C:\\Users\\MINISTER JOHN\\DiabetesPredictionSystem\\LogisticRegressionModel.pickle')
    lis = []

    lis.append(request.GET['pregnancies'])
    lis.append(request.GET['glucose']) 
    lis.append(request.GET['bloodpressure'])  
    lis.append(request.GET['skinthickness'])  
    lis.append(request.GET['insulin'])  
    lis.append(request.GET['bmi'])
    lis.append(request.GET['diabetespedigreefunction'])
    lis.append(request.GET['age'])  

    ans = cls.predict([lis])
   

    return render(request, 'result.html', {'ans': ans})
