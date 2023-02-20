from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET": #Хотим получить форму
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form
                   }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == "POST": # Хотим создать Снипет (данные от формы)
        # name = request.POST["name"]
        # lang = request.POST["lang"]
        # code = request.POST["code"]
        # snippet = Snippet(name=name, lang=lang, code=code)
        # snippet.save()
        #
        # return redirect('snippets-list')

        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snippets-list')



def snippets_page(request):
    snippets = Snippet.objects.all()

    context = {'pagename': 'Просмотр сниппетов',
               'snippets': snippets}

    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request):
    pass
