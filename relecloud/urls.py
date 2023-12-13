## APP (relecloud)
from django.urls import path 
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('destinations/',views.destinations, name='destinations'),
    path('destinations/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),
    path('cruise/<int:pk>', views.CruiseDetailView.as_view(), name='cruise_detail'),
    path('destinations/add',views.DestinationCreateView.as_view(), name='destination_form'),
    path('destinations/<int:pk>/update', views.DestinationUpdateView.as_view(), name='destination_form'),
    path('destinations/<int:pk>/delete', views.DestinationDeleteView.as_view(), name='destination_confirm_delete'),
    path('info_request', views.InfoRequestCreate.as_view(), name='info_request'),


]
