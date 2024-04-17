from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from seller.models import Food
def index(request):
    object_list = Food.objects.all()
    context = {
        'object_list':object_list
    }
    return render(request, 'home.html',context)

class UserCreateView(CreateView):
    template_name='registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name='registration/register_done.html'