from django.shortcuts import get_object_or_404, render, redirect
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