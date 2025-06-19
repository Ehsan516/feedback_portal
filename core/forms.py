from django import forms#for html forms

class feedbackForms(forms.form):
    message = forms.CharField(widget=forms.Textarea(attrs={#used attrs for UI
        'rows':5, 'placeholder':'Enter your anonymous feedback'
    }))