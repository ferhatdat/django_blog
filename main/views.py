from django.http import HttpResponse

def home(request):
    return HttpResponse('This main home page......')