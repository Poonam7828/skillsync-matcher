from django import forms
from .models import Candidate
from .ml_utils import get_page_count
import os

class ResumeUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume_file'].required = True

    class Meta:
        model = Candidate
        fields = ['resume_file']
        widgets = {
            'resume_file': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'resume_upload',
                'accept': '.pdf,.docx'
            }),
        }

    def clean_resume_file(self):
        resume_file = self.cleaned_data.get('resume_file')
        if not resume_file:
            return None

        # 1. Check extension
        ext = os.path.splitext(resume_file.name)[1].lower()
        if ext not in ['.pdf', '.docx']:
            raise forms.ValidationError("Only PDF and DOCX files are allowed.")

        # 2. Check page count
        pages = get_page_count(resume_file)
        if pages > 2:
            raise forms.ValidationError(f"Your resume has {pages} pages. Please upload a resume with 2 pages or less.")

        return resume_file
