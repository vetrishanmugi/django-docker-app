from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello from inside a Dockerized Django App!")

# Create your views here.
