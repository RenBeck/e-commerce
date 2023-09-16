from django.shortcuts import render

context = {
    'title': 'Renato Beck | Home'
}

def home(request):
    return render(
        request,
        'home/index.html',
        context
    )
