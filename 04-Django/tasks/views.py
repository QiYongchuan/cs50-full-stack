# from audioop import reverse
from django.urls import reverse

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# tasks = []
# 增加session，储存用户的数据


class NewTaskForm(forms.Form):
  task =forms.CharField(label="New Task")
  priority = forms.IntegerField(label="Priority",min_value=1,max_value = 10)
def index(request):
  if "tasks" not in request.session:
    request.session["tasks"] = []
  return render(request,"tasks/index.html",{
   "tasks":request.session["tasks"]
  })
 
def add(request):
  
  if request.method == "POST":
    form = NewTaskForm(request.POST)
    if form.is_valid():
      task = form.cleaned_data["task"]
      # request.session["tasks"] +=[task]  下面的方法也可以
      request.session["tasks"].append(task)
      request.session.modified = True
      return HttpResponseRedirect(reverse("tasks:index"))
    else:
      return render(request,"tasks/add.html",{
        "form":form
      })
      
  return render(request,"tasks/add.html",{
    "form":NewTaskForm()
  })