from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import InputForm
from .models import Names


def index(request):
    form = InputForm()

    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():

            all_names_from_form = dict(request.POST)
            all_names_from_form.pop('csrfmiddlewaretoken')
            all_names_from_form.pop('save')

            for name in all_names_from_form:
                all_names_from_form[name] = all_names_from_form[name][0]

            try:
                Names.objects.create(all_names=all_names_from_form)
                return redirect('index')

            except:
                form.add_error(None, 'Ошибка добавления данных')

    else:
        form = InputForm()

    form = InputForm()
    return render(request, 'dynamic_input_form/index.html', {'form': form})


class NamesView(ListView):
    model = Names
    template_name = 'dynamic_input_form/detail.html'


def detail(request):
    data = Names.objects.all()
    keys = {}
    for i in data:
        keys = i.all_names.values
    context = {'data': data, 'keys': keys}
    return render(request, 'dynamic_input_form/detail.html', context)


def delete_item(request, id):
    item = Names.objects.get(id=id)
    item.delete()
    return redirect('detail')
