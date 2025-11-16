from django.contrib import admin
from django.urls import path
from firstApp import views as fa
from quoteApp import views as qa


urlpatterns = [

    path('hello/', fa.display),
    path('datetime/',fa.displayDatetime),
    
]
