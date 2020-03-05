from django.conf.urls import url
from mytest import views
from django.urls import path
urlpatterns=[
    path('index/',views.index),
    path('cnareas/',views.cnareas)

]