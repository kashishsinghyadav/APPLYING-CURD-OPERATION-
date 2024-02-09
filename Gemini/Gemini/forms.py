from django import forms
from loginuser.models import Emp,Position


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Emp
        fields = ('firstname','mobile','empcode','pos')
        labels = {
            'firstname':'Full Name',
            'empcode':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['pos'].empty_label = "Select"
        self.fields['empcode'].required = False