from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression



# Create your views here.
def index(request):
    result = None
    model = LinearRegression()
    attendance = [[78],[60],[70],[50],[40],[20],[95],[80]]
    marks = [60,50,80,55,85,88,66,50]
    model.fit(attendance,marks)
    abc = {'result':result}
    if request.method == 'POST':
        attendance = int(request.POST.get('attendance'))
        result = model.predict([[attendance]])
        context = {'result':result,'attendance':attendance}
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',abc)
