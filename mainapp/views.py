from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={}
    context['a'] = "<a href=''>alert('hello')</a> <script>alert('hello')</script>"
    return render(request, 'index.html',context)