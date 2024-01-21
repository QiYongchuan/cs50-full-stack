from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,"hello/index.html")
# 直接渲染返回整个html文件
# 但需要注意，这一步需要在setting中设置templates的路径，这里视频没有讲
def Brain(request):
  return HttpResponse("Hello,Brain!")

def David(request):
  return HttpResponse("Hello,David!")

# def greet(request,name):
#   return HttpResponse(f"Hello,{name.capitalize()}!")

def greet(request,name):
  return render(request,"hello/greet.html",{
    "name":name.capitalize()
  })