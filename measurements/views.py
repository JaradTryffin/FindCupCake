from django.shortcuts import render
from .models import Measurements
from .forms import MeasurementForm
from geopy.geocoders import Nominatim,Photon
from geopy import distance
from geopy.distance import geodesic
from .utils import get_geo,get_center_coordinates,get_zoom,get_ip_address
import folium
# Create your views here.

def frontpage(request):
    start_point =None
    distance = None
    end_point = None
    cost =None
    time =None
    form = MeasurementForm(request.POST or None)
    geolocator =Photon(user_agent='measurements')

    # ip_ = get_ip_address(request)
    # print(ip_)
    # ip = '164.160.36.116'
    # country,city,lat,lon =get_geo(ip)
    # nowLocation = geolocator.geocode(city)
    # now_lat = lat
    # now_lon =lon
    # nowPoint = (now_lat,now_lon)
    m = folium.Map(width=800, height=500,location=get_center_coordinates(-28.579397200000002,24.086794125366062),zoom_start=3)
    folium.Marker([-28.579397200000002,24.086794125366062],tooltip="South Africa",icon=folium.Icon(color='purple')).add_to(m)
    
        

    if form.is_valid():
       
        instance = form.save(commit=False)
        start_point_ = form.cleaned_data.get('start_point')
        start_point = geolocator.geocode(start_point_)
        print(start_point)
        print(start_point.latitude)
        print(start_point.longitude)
        start_lat = start_point.latitude
        start_lon = start_point.longitude
        pointA =(start_lon,start_lat)

           

        end_point_ = form.cleaned_data.get('end_point')
        end_point = geolocator.geocode(end_point_)
        print(end_point)
        print(end_point.latitude)
        print(end_point.longitude)
        end_lat = end_point.latitude
        end_lon = end_point.longitude
        pointB = (end_lon,end_lat)

            
        distance = round(geodesic(pointA,pointB).km, 2)
        cost = form.cleaned_data.get('cost')
        time = form.cleaned_data.get('time')

        points=[
            [start_lat,start_lon],
            [end_lat,end_lon],
        ]

        m = folium.Map(location=get_center_coordinates(start_lat,start_lon,end_lat,end_lon),zoom_start=get_zoom(distance))
        folium.Marker([start_lat,start_lon],tooltip='click here for more',popup=start_point,icon=folium.Icon(color='purple')).add_to(m)
        folium.Marker([end_lat,end_lon],tooltip='click here for more',popup=end_point,icon=folium.Icon(color='red')).add_to(m)

        line = folium.PolyLine(points,weight=2,color='blue')
        m.add_child(line)
        # (start_lat,start_lon,end_lat,end_lon)



        instance.distance = distance
        instance.cost = instance.distance * instance.price_per_km
        instance.time = instance.distance / instance.price_per_hour
        instance.save()
    
    m=m._repr_html_()

    info = Measurements.objects.latest('id')
   


    

    

        



    context={'form':form,'m':m,'distance':distance,'start_point':start_point,'end_point':end_point,'info':info}
    return render(request,'measurements/index.html',context)
