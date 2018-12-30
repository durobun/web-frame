from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Django로 블로그를 만들어 봅시다.")

def get_extra1(request):
    return HttpResponse("extra1")

def get_extra2(request):
    return HttpResponse("extra2")