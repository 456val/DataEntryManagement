from django.urls import path
from . import views  # Import views from the current app
from .views import add_inventory, add_production, add_currency


urlpatterns = [
    # Root URL (Homepage)
    path('', views.home_view, name='home'),  # Handles the root URL

    # Currency view URL
    path('currency/<int:currency_id>/', views.currency_view, name='currency_view'),

    # Production records view URL
    path('production/<int:production_id>/', views.production_view, name='production_view'),

    # Inventory view URL
    path('inventory/<int:inventory_id>/', views.inventory_view, name='inventory_view'),
    
    
    path('add_inventory/', add_inventory, name='add_inventory'),
    
    path('add_production/', add_production, name='add_production'),
    
    path('add_currency/', add_currency, name='add_currency'),


]

