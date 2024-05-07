from django.urls import path
from . import views

urlpatterns = [
    path('addresigterecompetition/', views.addRegisteredCompetition.as_view(), name = 'addregisteredcompetition'),
    path('updatebio/', views.updateBio.as_view(), name = 'updatebio'),
    path('updatebio/', views.updateBio.as_view(), name = 'updatebio'),
]