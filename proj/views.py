import requests
from django.shortcuts import render
from .models import IP
from .forms import IPForm
from gmplot import gmplot
from django.http import JsonResponse

def index(request):
    getLocationUrl = "https://tools.keycdn.com/geo.json?host="  	# loction finder api
    form = IPForm()
    ipaddress = ''
    lat = ''
    long = ''
    city = ''
    if request.method == 'POST':
        form = IPForm(request.POST)
        if form.is_valid():
            ipaddress = form.cleaned_data['ipaddress']
            lat, long, city = get_city_from_ip(ipaddress)

    context = {'form' : form, 'value': ipaddress, 'lat': lat, 'long': long, 'city':city}
    return render(request, 'proj/proj.html', context)

def get_city(request,ipaddress):
    return JsonResponse({'foo':'bar'})

def get_city_from_ip(ipaddress):
    getLocationUrl = "https://tools.keycdn.com/geo.json?host="
    res = requests.get(getLocationUrl+ipaddress)		
    data = res.json()			
    geo = data['data']
    gdata = geo['geo']
    lat = gdata['latitude']
    long = gdata['longitude']
    city = gdata['city']
    return (lat, long, city)