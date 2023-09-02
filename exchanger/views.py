import json

from google_currency import convert

from django.shortcuts import render

from exchanger import forms


# Create your views here.

def home(request):
    res1 = {}
    natija = ""
    if request.method == 'POST':
        form = forms.Widget(request.POST)
        if form.is_valid():
            form.save()
            shu_dan = form.cleaned_data['value1']
            shu_ga = form.cleaned_data['value2']
            qiymat = form.cleaned_data['value']
            natija1 = convert(shu_dan, shu_ga, qiymat)
            res1 = json.loads(natija1)
            natija = res1.get("amount")
    else:
        form = forms.Widget()
    return render(request, 'exchanger/index.html', {'form': form, 'qiymat': natija})
