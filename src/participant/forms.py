from django import forms 
from .models import Participant
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'availability': 'Are you available on xx October, from xxh to xxh?',
            'experience': 'Do you have a past experience with coding?',
            'do_git': 'Do you want to attend the GIT Workshop?',
            'do_fest': 'Do you want to attend OpenFest?',
            'conduct': 'Do you agree with the Code of Conduct of Hacktoberfest?'
        }


    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)
        # Handle Empty Labels
        self.fields['conduct'].required = True

        # Handle Non Required Fields
        #self.fields['phone_number'].required = False