from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField()
    filetype = forms.CharField(max_length=15)
    quantity = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    file = forms.FileField()
