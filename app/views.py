from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import test_model
from .forms import test_form
# Create your views here.

def test_view(request):
    if request.method == 'POST':
        form = test_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешный ответ')
        else:
            return HttpResponse('Неуспешный ответ')
    else:
        form = test_form()

    return render(request, 'test_template.html', {'form': form})
