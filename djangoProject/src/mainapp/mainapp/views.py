from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome {}!</h1>".format(request.user))
