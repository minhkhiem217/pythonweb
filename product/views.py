from django.shortcuts import render
from django.views import View


# Create your views here.
class home(View):
    def get(self, request):
        return render(request, template_name='homepage/home.html')
