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

sample_choice_view = SampleChoiceView.as_view()
