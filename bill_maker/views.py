from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from django.contrib import messages


class Gatherer:
    def __init__(self):
        self.clicked_ids = []

    def append_id(self, id):
        self.clicked_ids.append(id)

    def clear_ids(self):
        self.clicked_ids.clear()

    def summary(self):
        return self.clicked_ids




gather = Gatherer()


def homepage(request):
    starters = Product.objects.filter(category = "starters")
    mains = Product.objects.filter(category = "mains")
    desserts = Product.objects.filter(category = "desserts")
    drinks = Product.objects.filter(category = "drinks")

    summary = []
    total = 0
    # get all the ordered items
    for id in gather.summary():
        summary.append(Product.objects.get(id = id))
        total = total + Product.objects.get(id = id).price


    return render(request, 'main/homepage.html',
                  context={'starters': starters,
                           'mains': mains,
                           'desserts': desserts,
                           'drinks': drinks,
                           'summary':summary,
                           'total':total,
                           }
                  )

def complete_order(request):
    gather.clear_ids()
    return redirect('main:homepage')


def add_item(request, id):
    Product.objects.get(id=id)
    messages.success(request, f"Added..")

    gather.append_id(id)

    return redirect('main:homepage')
    #eturn HttpResponse(gather.clicked_ids)
