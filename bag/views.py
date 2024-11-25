from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to show all products, including sorting and search queries """

    return render(request, 'bag/bag.html')