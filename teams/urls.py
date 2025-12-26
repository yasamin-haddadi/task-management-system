from django.urls import path
from .views import TeamkListCreateRetrieveUpdateDestroyView

urlpatterns = [
    path('teams/', TeamkListCreateRetrieveUpdateDestroyView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamkListCreateRetrieveUpdateDestroyView.as_view(), name='team-detail'),
]