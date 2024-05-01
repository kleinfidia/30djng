from django.shortcuts import render

# Create your views here.


def zpol_list(requests):
    return render(request, 'zpol/zpol_list.html')