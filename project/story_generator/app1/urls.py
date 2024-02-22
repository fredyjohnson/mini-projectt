from django.urls import path
from.import views

urlpatterns = [
    path('webpage/',views.webpage),
    path('login/',views.login0),
    path('signup/',views.register)
]