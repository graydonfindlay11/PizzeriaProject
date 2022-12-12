from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime, date

# Create your views here.
def index(request):
    return render(request, 'Pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'all_pizzas':pizzas}

    return render(request, 'Pizzas/pizzas.html', context)

'''
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.all()
    comments = pizza.comment_set.all()


    context = {'Pizza':pizza, 'toppings':toppings, 'comments':comments}

    return render(request, 'Pizzas/pizza.html', context)   
'''

def pizza(request, pizza_id):

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    comments = Comment.objects.filter(pizza=pizza_id)

    if request.method == 'GET':                             
        image = pizza.image_set.all()

    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments, 'image':image}
    return render(request, 'Pizzas/pizza.html', context)


def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        print(request.POST)
        form =PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pizzas:pizzas')

    context = {'form':form}

    return render(request, 'Pizzas/new_pizza.html', context)



def comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    #comments = Comment.objects.filter(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
       #Comment.objects.create(post_id=post_id, username=request.user,text=comment,date_added=date.today())
    else:
        #print(request.POST)
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            form.save()

            return redirect('Pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza }

    return render(request, 'Pizzas/comment.html', context)

