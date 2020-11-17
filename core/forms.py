
from django import forms
from .models import *

class predict_files(forms.Form):

    class Meta:
        model = MyTrainedModel
        fields = "__all__"      