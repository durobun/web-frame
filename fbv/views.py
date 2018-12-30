from django.http import HttpResponse
from django.shortcuts import render

def get_http_response(request):

    return HttpResponse('''
    <h1>HttpResonse</h1>
    <p>FBV HttpResponse 출력을 보고 있습니다.</p>''')

def get_render(request):
    return render(request, "test.html")

def get_render_pass_context_data(request):
    return render(request, "test_context_data.html"
                  , context={"title": "render를 통해서 context data 전달"})