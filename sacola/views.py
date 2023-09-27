from django.shortcuts import render

context = {
    'title': 'BS | Sacola'
}

def sacola(request):
    return render(
        request,
        'sacola/index.html',
        context
    )
