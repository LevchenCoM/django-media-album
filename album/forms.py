from django import forms
from .choices import FILETYPE_CHOICES
from .models import Media

class MediaAddForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title'}),max_length=64, required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Description'}),max_length=256, required=True)
    file_type = forms.ChoiceField(choices = FILETYPE_CHOICES, widget=forms.Select(attrs={'class' : 'custom-select', 'placeholder': 'Choose media type'}), required=True)
    file = forms.FileField(widget=forms.FileInput(attrs={'class' : 'custom-file', 'placeholder': 'Choose file to upload'}), required=True)
    class Meta:
        model = Media
        fields = ('file_type', 'file', 'title', 'description')

class MediaEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title'}),max_length=64, required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Description'}),max_length=256, required=True)
    file_type = forms.ChoiceField(choices = FILETYPE_CHOICES, widget=forms.Select(attrs={'class' : 'custom-select', 'placeholder': 'Choose media type'}), required=True)
    file = forms.FileField(widget=forms.FileInput(attrs={'class' : 'custom-file', 'placeholder': 'Change file'}), required=False)
    class Meta:
        model = Media
        fields = ('file_type', 'file', 'title', 'description')

class MediaLinkForm(forms.ModelForm):
    link = forms.URLField(label='Insta link', widget=forms.URLInput(attrs={'class' : 'form-control', 'placeholder': 'Write instagram post link first'}), required=True)

    class Meta:
        model = Media
        fields = ['link',]
