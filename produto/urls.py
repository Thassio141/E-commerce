from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('deletar/<int:id>/', views.deletar, name="deletar"),
    path('atualizar/<int:id>/',views.atualizar, name='atualizar'),
    path('',views.index, name='index'),
    path('comprar/<int:id>', views.comprar, name='comprar')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)