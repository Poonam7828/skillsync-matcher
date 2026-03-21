from django import forms
from .models import Candidate

class ResumeUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume_file'].required = True

    class Meta:
        model = Candidate
        fields = ['resume_file']
        widgets = {
            'resume_file': forms.FileInput(attrs={'class': 'form-control', 'id': 'resume_upload'}),
        }
