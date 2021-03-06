from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import userInfoSerializers
import requests
from. models import userInfo
@api_view(['POST',])
def home(request):
    
    if request.method=='POST':
        serializer = userInfoSerializers(data=request.data)
        data = "SuccussFully record inserted."
        if serializer.is_valid():
            simpleForm = serializer.save()
            

        else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data)

def insertData(request):

    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        data = {'name':name, 'age':age, 'gender':gender, 'mobile':mobile, 'place':place }
        headers = {'Content-Type': 'application/json'}
        read = requests.post('http://localhost:8000/home/', json=data, headers=headers)
        return redirect('/viewdata/')
    else:
        return render(request,"userform.html")

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        result = userInfo.objects.all()
        serialize = userInfoSerializers(result, many=True)
        return Response(serialize.data)

def viewData(request):
    callapi = requests.get('http://localhost:8000/getdata/')
    data  = callapi.json()
    return render (request,"viewdata.html",{'data':data})

@api_view(['PUT', ])
def putdata(request,pk):
    u = userInfo.objects.get(pk=pk)
    if request.method=='PUT':
        serializer = userInfoSerializers(u, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("update successfully")

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def update(request,pk):
    d = userInfo.objects.get(pk=pk)
    
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        data = {'name':name, 'age':age, 'gender':gender, 'mobile':mobile, 'place':place }
        headers = {'Content-Type': 'application/json'}
        read = requests.put('http://localhost:8000/putdata/{}/'.format(pk), json=data, headers=headers)
        return redirect('/viewdata/')

    return render(request,'update.html',{'d':d})

@api_view(['DELETE', ])
def deletedata (request,pk):
    u = userInfo.objects.get(pk=pk)
    if request.method=='DELETE':
        operation = u.delete()
        if operation:
            return Response("Delete successfull")
        else:
            return Response("Delete Failure")

def delete(request,pk):
    d = userInfo.objects.get(pk=pk)
    read = requests.delete('http://localhost:8000/deletedata/{}/'.format(pk))
    return redirect('/viewdata/')
        