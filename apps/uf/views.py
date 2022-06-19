from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from uf.forms import UFForms
from uf.models import UF
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    """ Trás a listagem de todos os UFs (Estados) do sistema, utilizando paginação. """
    ufs = UF.objects.order_by('uf_name')
    paginator = Paginator(ufs, 10)
    page = request.GET.get('page')
    ufs_peer_page = paginator.get_page(page)
    data = {
        'ufs' : ufs_peer_page
    }

    return render(request, 'ufs/index.html', data)

def create_uf(request):
    """ Cadatra uma nova UF. """
    if request.method == 'POST':
        form = UFForms(request.POST)
        if(form.is_valid()):
            uf_name = form['uf_name'].value()
            uf_initials = form['uf_initials'].value()
            uf = UF.objects.create(uf_name= uf_name, uf_initials= uf_initials)
            uf.save()
            return redirect('ufs_index')
        else:
            form = UFForms()
            contexto = {
                'form' : form
            }
            return render(request, 'ufs/create.html', contexto)
    else:
        form = UFForms()
        contexto = {
            'form' : form
        }
        return render(request, 'ufs/create.html', contexto)

def delete_uf(request, uf_id):
    """ Exclui uma UF do sistema. """
    uf = get_object_or_404(UF, pk=uf_id)
    uf.delete()
    return redirect('ufs_index')


def edit_uf(request, uf_id):
    """ Envia dados para edição de uma UF. """
    uf = get_object_or_404(UF, pk=uf_id)
    form = UFForms()
    uf_edit = {
        'uf': uf,
        'form': form
    }
    return render(request, 'ufs/edit_uf.html', uf_edit)

def update_uf(request):
    """ Efetiva a alteraçào de uma UF no sistema. """
    if request.method == 'POST':
        form = UFForms(request.POST)
        if(form.is_valid()):
            uf_id = form['id'].value()
            uf = UF.objects.get(pk=uf_id)
            uf.uf_name = form['uf_name'].value()
            uf.uf_initials = form['uf_initials'].value()
            uf.save()
            return redirect('ufs_index')
        else:
            form = UFForms()
            contexto = {
                'form' : form
            }
            return render(request, 'ufs/edit_uf.html', contexto)
    else:
        form = UFForms()
        contexto = {
            'form' : form
        }
        return render(request, 'ufs/edit_uf.html', contexto)

