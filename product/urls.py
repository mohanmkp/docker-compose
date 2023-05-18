from django.urls import path
from .import views

urlpatterns = [
   path("", views.product_view.as_view()),

]


