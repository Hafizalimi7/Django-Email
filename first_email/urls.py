from django.urls import path
from .views import UserView, HomeView, EmailSent
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('email/',UserView.as_view(), name="email" ),
    path('success/', EmailSent.as_view(),name="success")
]
