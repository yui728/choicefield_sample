from django.shortcuts import render
from django.views import View
from . import forms

class SampleChoiceView(View):
    def get(self, request):
        form = forms.SampleChoiceForm()
        context = {
            'form': form
        }

        return render(request, 'choice_sample.html', context)

class SampleChoiceAddView(View):
    def get(self, request):
        form = forms.SampleChoiceAddForm()
        form.fields['choice1'].choices = [
            ('1', '1番目'),
            ('2', '2番目'),
            ('3', '3番目'),
            ('4', '4番目'),
            ('5', '5番目'),
        ]
        context = {
            'form': form
        }

        return render(request, 'choice_sample.html', context)

sample_choice_view = SampleChoiceView.as_view()
sample_choice_add_view = SampleChoiceAddView.as_view()
