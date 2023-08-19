from django.urls import path

from customers.views import CreateTenantView


urlpatterns = [
    path('create/', CreateTenantView.as_view(), name='create-tenant'),
]