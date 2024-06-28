from django.urls import path
from delete.views import delete
urlpatterns = [
    path('delete/<int:id>/', delete, name='delete'),
]  
