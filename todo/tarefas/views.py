from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefa

# Create your views here.
@login_required
def nova_categoria(request):
    if(request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('tarefas:lista_categorias')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/lista-categorias.html', {'categorias': categorias})

@login_required
def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id).delete()
    return redirect('tarefas:lista_categorias')

@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if(request.method == 'POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if(form.is_valid()):
            form.save()
            return redirect('tarefas:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'tarefas/nova_categoria.html', {'form':form})

@login_required
def nova_tarefa(request):
    if(request.method == 'POST'):
        form = TarefaForm(request.POST)
        form.errors.as_json()
        if(form.is_valid()):
            form.save()
            return redirect('core')
        else:
            print(form.errors)
    else:
        form = TarefaForm()

    form.errors.as_json()
    return render(request, 'tarefas/nova_tarefa.html', {'form':form})

@login_required
def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id).delete()
    return redirect('core')

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if(request.method == 'POST'):
        form = TarefaForm(request.POST, instance=tarefa)
        if(form.is_valid()):
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'tarefas/nova_tarefa.html', {'form':form})
