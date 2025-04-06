from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'groups/dashboard.html')

def create_group(request):
    return render(request,'groups/create_group.html')