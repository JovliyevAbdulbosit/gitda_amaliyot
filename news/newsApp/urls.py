from django.urls import path
from .views import *


urlpatterns=[
    path('' , homeViews , name='home'),
    path('catgory/<slug>/', ctgViews , name='category'),
    path('view/<int:pk>/', newsViews , name='view'),
    path('qidiruv/',searchViews, name='qidiruv'),
    path('contact/' , contactViews , name='contact')
]










