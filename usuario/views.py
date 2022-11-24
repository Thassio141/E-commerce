from django.shortcuts import redirect ,render , HttpResponseRedirect
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = 'registrar.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = 'Cadastrar'

        return context