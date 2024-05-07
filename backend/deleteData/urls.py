from django.urls import path
from . import views

urlpatterns = [
    path('deleteprofileimage/', views.deleteProfileImage.as_view(), name='deleteprofileimage'),
    path('deletecompetitionfile/', views.deleteCompetitionFile.as_view(), name='deletecompetitionfile'),
]