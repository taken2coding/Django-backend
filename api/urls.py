from django.urls import path
from .views import UserProfileView, BookListAPIView, Home
from django.views.generic import TemplateView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('books/', BookListAPIView.as_view({'get': 'list'}), name='book_list'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]