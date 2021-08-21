from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django. You're at the Todo index.")
