from mechanic_app.models import *
from django import forms

class ScheduledRepairForm(forms.ModelForm):
    class Meta:
        model = ScheduledRepair
        fields = '__all__'