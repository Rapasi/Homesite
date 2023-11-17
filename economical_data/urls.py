from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('rates/', views.display_page, name='display_page'),
    path('rates/api/get_ECB_DF/', views.get_ECB_DF, name='get_ECB_DF'),
    path('rates/api/get_ECB_MLF/', views.get_ECB_MLF, name='get_ECB_MLF'),
    path('rates/api/get_ECB_MRO/', views.get_ECB_MRO, name='get_ECB_MRO'),
    path('search/', views.search_view, name='search'),
    path('info/', views.info_view, name='info'),
] 