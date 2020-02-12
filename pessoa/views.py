from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoasForm
from pessoa.models import Pessoa


def home(request):
    return render(request, 'home.html')

@login_required
def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'lista_pessoas.html',{'pessoas':pessoas})

@login_required
def incluir(request):
    form = PessoasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'form_pessoas.html', {'form':form})

@login_required
def alterar(request, id):
    pessoa = get_object_or_404(Pessoa,pk=id)
    form = PessoasForm(request.POST or None , request.FILES or None,
                       instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'form_pessoas.html', {'form':form})

@login_required
def excluir(request, id):
    pessoa = get_object_or_404(Pessoa,pk=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar')
    return render(request, 'exclusao_confirm.html', {'pessoa':pessoa})