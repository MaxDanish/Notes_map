from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    template = 'notes/index.html'
    context = {
        'title': 'Ваййаааа',
        'text': 'Тут скоро такаааая пушка будет'
    }
    return render(request, template, context)
