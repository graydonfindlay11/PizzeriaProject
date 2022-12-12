from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'Pizzas'
#app_name = 'Pizza'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_pizza',views.new_pizza,name='new_pizza'),
    path('comment/<int:pizza_id>/',views.comment,name='comment'),
]

