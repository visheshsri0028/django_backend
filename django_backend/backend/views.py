from django.shortcuts import render
import axios
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def my_view(request):
    response = axios.get()
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to load data'}, status=response.status_code)

form = {
    'name': 'John',
    'username': 'JohnDoe',
    'password': 'JohnDoe',
    'address': 'Ballia',
    'number': '980569412',
    'email': 'tugrp@example.com',
    'gender': 'Male',
}