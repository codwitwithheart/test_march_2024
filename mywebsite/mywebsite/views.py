from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Guys I have done deployment")