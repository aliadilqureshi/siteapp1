from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('making_a_doc/', views.making_the_doc, name='doc'),
    path('making_the_document/', views.making_the_document, name='document'),

]
