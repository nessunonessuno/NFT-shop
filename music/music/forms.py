from django import forms
type = [('.mp3', '.mp3'),('.mp4', '.mp4'),('.wav', '.wav'),('.vst', '.vst'),('.jpg', '.jpg'),('.png', '.png'), ('.aiff','.aiff'), ('.au', '.au') ]

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField()
    filetype = forms.CharField(label='Choose filetype', widget=forms.Select(choices=type))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    file = forms.FileField()
