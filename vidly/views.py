

from django.shortcuts import render

def home(request):
    """
    Render the home page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')