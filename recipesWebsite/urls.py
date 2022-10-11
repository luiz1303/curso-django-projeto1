from django.urls import path

from recipesWebsite.views import home

urlpatterns = [
    path('', home),
]
