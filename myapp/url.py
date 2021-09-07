from django.urls import path
from . import views
urlpatterns=[
    path('',views.data,name="data"),
    path('index',views.index,name='index'),
]
