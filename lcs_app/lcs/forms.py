from django import forms
from .models import Stage
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class StageForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('submit', 'Crear Stage'))

    
    stage_choices = (
        (1, 'Subscriber'),
        (2, 'Lead'),
        (3, 'MQL'),
        (4, 'SQL'),
        (5, 'Opportunity'),
        (6, 'Customer'),
    )

    teams = (
        (1, 'Marketing'),
        (2, 'Sales'),
        (3, 'Customer Service'), 
    )

    stage_name = forms.ChoiceField(
        choices= stage_choices
        )
    stage_description = forms.CharField(max_length= 500)
    stage_tools = forms.CharField(max_length=200)
    stage_trigger = forms.CharField(max_length=100)
    # owner_team = forms.ChoiceField(
    #     choices= teams,
    #     widget= forms.RadioSelect()
    #     )

