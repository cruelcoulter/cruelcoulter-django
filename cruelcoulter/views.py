from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')
