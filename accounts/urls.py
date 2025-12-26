from django.urls import path
from .views import AccountListCreateView, AccountRetrieveUpdateDestroyView

urlpatterns = [
    path('list-create/', AccountListCreateView.as_view(), name='account-list-create'),
    path('update-delete/<int:pk>/', AccountRetrieveUpdateDestroyView.as_view(), name='account-detail'),
]