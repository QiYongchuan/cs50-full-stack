from django.urls import path

from . import views

urlpatterns =[
  path("",views.index,name="index"),
  path("<str:name>",views.greet,name="greet"),
  path("Brain",views.Brain,name="Brain"),
  path("David",views.David,name="David"),
]