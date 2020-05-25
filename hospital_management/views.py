from django.shortcuts import render


# Create your views here.
def details_list(request):
    return render(request,'hospital_management/details_list.html',{})
