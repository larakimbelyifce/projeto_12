from django.shortcuts import render

# Chamar a url para renderizar a página html.
def home(request):
    return render(request, 'base.html', {})
