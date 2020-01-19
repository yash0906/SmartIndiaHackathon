from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('addmissing/',views.missing, name='fir-addmissing'),
	path('stolen/',views.stolen, name='fir-stolen'),
	path('addsomething/',views.addsomething, name='fir-addsomething'),
	path('home/', views.home, name = 'fir-home'),
]