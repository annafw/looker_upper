import sys

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render

from .models import Product


class IndexView(ListView):
    model = Product
    template_name = 'looker_upper/index.html'


class FindView(ListView):
    model = Product
    template_name = 'looker_upper/results.html'


def find(request):
    product_name = request.POST["product_to_find"]
    print >> sys.stderr, product_name
    ingredients = [ "first ingredient", "second ingredient" ]
    return render(request, 'looker_upper/results.html',
                  {'ingredients': ingredients,
                   'product_name': product_name})
