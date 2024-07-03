from django import forms
from .models import UploadedFile, ExcelData

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
        
class UploadExcelForm(forms.ModelForm):
    class Meta:
        model = ExcelData
        fields = ['file_name', 'file_content']