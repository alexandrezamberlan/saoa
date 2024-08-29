from __future__ import unicode_literals

from django.contrib import messages

from django.db.models import Q

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.urls import reverse

from utils.decorators import LoginRequiredMixin, CoordenadorRequiredMixin

from .models import Submissao

from .forms import BuscaSubmissaoForm, SubmissaoForm


class SubmissaoListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/submissao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaSubmissaoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().all()    
        if self.request.user.tipo == 'COORDENADOR' or self.request.user.tipo == 'COORDENADOR_SUPLENTE':  
            qs = qs.filter(Q(responsavel=self.request.user) | Q(evento__coordenador=self.request.user) | Q(evento__coordenador_suplente=self.request.user))  
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaSubmissaoForm()

        if form.is_valid():            
            situacao = form.cleaned_data.get('situacao')            
            pesquisa = form.cleaned_data.get('pesquisa')    
                
            if situacao:
                qs = qs.filter(status=situacao)        
                
            if pesquisa:
                qs = qs.filter(Q(evento__coordenador__nome__icontains=pesquisa) | Q(evento__nome__icontains=pesquisa) | Q(titulo__icontains=pesquisa) | Q(resumo__icontains=pesquisa) | Q(responsavel__nome__icontains=pesquisa))
                            
        return qs
    
    
class MinhaSubmissaoListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/minhas_submissao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dados filtrando
            context['form'] = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            context['form'] = BuscaSubmissaoForm()
        return context

    def get_queryset(self):                
        qs = super().get_queryset().filter(responsavel=self.request.user)  
        
        if self.request.GET:
            #quando ja tem dados filtrando
            form = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dados filtrando
            form = BuscaSubmissaoForm()

        if form.is_valid():            
            situacao = form.cleaned_data.get('situacao')            
            pesquisa = form.cleaned_data.get('pesquisa')    
                
            if situacao:
                qs = qs.filter(status=situacao)        
                
            if pesquisa:
                qs = qs.filter(Q(evento__coordenador__nome__icontains=pesquisa) | Q(evento__nome__icontains=pesquisa) | Q(titulo__icontains=pesquisa) | Q(resumo__icontains=pesquisa) | Q(responsavel__nome__icontains=pesquisa))
                            
        return qs
 

class SubmissaoCreateView(LoginRequiredMixin, CoordenadorRequiredMixin, CreateView):
    model = Submissao
    # fields = ['nome', 'tipo', 'instituicao', 'coordenador', 'coordenador_suplente', 'data_inicio', 'data_limite_trabalhos', 'modelo_artigo', 'arquivo_modelo', 'is_active']
    form_class = SubmissaoForm
    success_url = 'submissao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Submissão cadastrada com sucesso na plataforma!')
        return reverse(self.success_url)


class SubmissaoUpdateView(LoginRequiredMixin, CoordenadorRequiredMixin, UpdateView):
    model = Submissao
    # fields = ['nome', 'tipo', 'instituicao', 'coordenador', 'coordenador_suplente', 'data_inicio', 'data_limite_trabalhos', 'modelo_artigo', 'arquivo_modelo', 'is_active']
    form_class = SubmissaoForm
    success_url = 'submissao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Submissão atualizada com sucesso na plataforma!')
        return reverse(self.success_url) 

class SubmissaoDeleteView(LoginRequiredMixin, CoordenadorRequiredMixin, DeleteView):
    model = Submissao
    success_url = 'submissao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Submissão removida com sucesso na plataforma!')
        return reverse(self.success_url) 
    

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        #success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa submissão, permissão negada!')
        return redirect(self.success_url)

