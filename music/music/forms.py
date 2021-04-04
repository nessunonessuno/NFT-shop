from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    filetype = forms.CharField(max_length=15)
    quantity = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    file = forms.FileField()
