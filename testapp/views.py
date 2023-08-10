from django.shortcuts import render
import requests
import json

# Create your views here.


def testPro(request):
    return render(request,'login.html')

def testIndex1(request):
    return render(request,'index1.html')

def testIndex2(request):
    return render(request,'index2.html')

def testIndex3(request):
    return render(request,'index3.html')

def testIndex4(request):
    return render(request,'index4.html')

def apipost(request):
         print(request.method)
         if request.method == 'GET':
             return render(request,'index4.html')
         elif request.method == 'POST':
           username = request.POST.get("username")
           password = request.POST.get("password")
           datas={"username":username,
                "password":password
                 }
             # datas = request.POST.get('remark')
             # header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
           url= "https://openwhy.net/api/auth/login"
           r = requests.post(url,datas)
           res =r.text
           body = r.json()
           if body["code"] == "000000":
             token = body["datas"]["token"]
             return render(request,"index5.html", {'token': token})
           else:
             return render(request,"index5.html",{'token': res})