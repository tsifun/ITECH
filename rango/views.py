from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse
<<<<<<< HEAD
from rango.forms import CategoryForm
=======
from rango.models import Category
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad

def add_category(request):
     form = CategoryForm()
     if request.method == 'POST':
	         form = CategoryForm(request.POST)
	         if form.is_valid():
                  form.save(commit=True)
	          return index(request)
	         else:
                  print(form.errors)
     return render(request, 'rango/add_category.html', {'form': form})			 
def index(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad
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

<<<<<<< HEAD
=======
=======
      category_list = Category.objects.order_by('-likes')[:5]
      context_dict = {'categories': category_list}
	
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
      return render(request, 'rango/index.html', context_dict)
>>>>>>> 9792bf7070101d72b8fa1095987834bacc148344
>>>>>>> ef14ed875835620051c6b4260340198a41e2c8ad

