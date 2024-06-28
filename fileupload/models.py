from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.file.name

class ExcelData(models.Model):
    file_name = models.CharField(max_length=255)
    file_content = models.FileField(upload_to='excel_files/')

    def _str_(self):
        return self.file_name
# Create your models here.
