from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    available = Item.objects.filter(is_sold=False).order_by('-created_at')
    items = available[0:6]
    categories = list(Category.objects.all())

    # Newest items per category, so the home page can filter without reloading
    for category in categories:
        category.newest_items = available.filter(category=category)[0:6]
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })