from django.urls import path
from .views import UserView, HomeView, EmailSent, AllEmails
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('email/',UserView.as_view(), name="email" ),
    path('success/<int:pk>/', EmailSent.as_view(),name="success"),
    path('everymail/', AllEmails.as_view(), name="every_mail")
]
