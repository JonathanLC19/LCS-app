from django import forms
from .models import Stage
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Stage

class StageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Crear Stage'))


    # stage_name = forms.ChoiceField(
    #     choices= Stage.StageChoices.choices
    #     )
    # owner_team = forms.ChoiceField(
    #     choices= teams,
    #     widget= forms.RadioSelect()
    #     )

    class Meta:
        model = Stage
        fields = '__all__'
