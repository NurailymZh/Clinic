from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')
# Create your views here.
def calculate(request):
    number1 = request.POST.get("number1")
    number2 = request.POST.get("number2")
    
    result = None 
    
    if number1.isdigit() and number2.isdigit():
        result = int(number1) + int(number2)
        
    return render(request, 'myapp/index.html', { 'result':result})