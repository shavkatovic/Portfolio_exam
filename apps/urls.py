from django.urls import path
from apps import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('service', views.ServiceView.as_view(), name='service'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('portfolio', views.PortfolioView.as_view(), name='portfolio'),
    path('price', views.PriceView.as_view(), name='price'),
    path('testimonial', views.TestimonialView.as_view(), name='testimonial')
]
