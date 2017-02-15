from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse
from rango.models import Category

def index(request):
<<<<<<< HEAD
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

=======
      category_list = Category.objects.order_by('-likes')[:5]
      context_dict = {'categories': category_list}
	
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
      return render(request, 'rango/index.html', context_dict)
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344

