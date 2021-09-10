
from django.urls import path
from core.views import(
    HomeView,
)

app_name ='core'

urlpatterns = [
    # Home
    path('', HomeView, name='home'),

]