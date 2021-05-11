from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        #model fields는 약속
        fields = ('description', 'document',)
