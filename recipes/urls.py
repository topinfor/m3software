from django.urls import path
from recipes.views import home, contato, sobre

#dominio/recipes/...
urlpatterns = [
    path('',home), #home
     path('contato/',contato), #contato
      path('sobre/',sobre), #sobre

]