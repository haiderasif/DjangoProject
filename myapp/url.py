from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('counter',views.counter,name='counter'),
    path('book',views.book,name='book'),
    path('data',views.data,name='data'),
]
