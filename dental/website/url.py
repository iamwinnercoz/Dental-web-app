from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("blogpost/", views.blogpost, name="blogpost"),
    path("pricing/", views.pricing, name="pricing"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
]
