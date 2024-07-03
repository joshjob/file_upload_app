# fileupload/models.py

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.file.name

class ExcelData(models.Model):
    file_name = models.CharField(max_length=255)
    file_content = models.FileField(upload_to='excel_files/')

    def str(self):
        return self.file_name
    
class originaldata(models.Model):
    UG = 'UG'
    PG = 'PG'
    
    COURSE_CATEGORIES = [
        (UG, 'Undergraduate'),
        (PG, 'Postgraduate'),
    ]

    exam_code = models.CharField(max_length=100, null=True, blank=True)
    student_batch_name = models.CharField(max_length=255, null=True, blank=True)
    batch_name = models.CharField(max_length=255, null=True, blank=True)
    class_name = models.CharField(max_length=255, null=True, blank=True)
    student_name = models.CharField(max_length=255, null=True, blank=True)
    reg_no = models.CharField(max_length=50, null=True, blank=True)
    roll_no = models.CharField(max_length=50, null=True, blank=True)
    exam_type = models.CharField(max_length=100, null=True, blank=True)
    subject_type = models.CharField(max_length=100, null=True, blank=True)
    subject_code = models.CharField(max_length=100, null=True, blank=True)
    subject_name = models.CharField(max_length=255, null=True, blank=True)
    semester = models.CharField(max_length=50, null=True, blank=True)
    obt_marks = models.FloatField(null=True, blank=True)
    max_marks = models.FloatField(null=True, blank=True)
    obt_grade = models.CharField(max_length=2, null=True, blank=True)
    is_backlog = models.CharField(max_length=2, null=True, blank=True)
    is_pass = models.CharField(max_length=2, null=True, blank=True)
    backlog_attempt_number = models.IntegerField(null=True, blank=True)
    credit_point_earned = models.FloatField(null=True, blank=True)
    credit_point_offered = models.FloatField(null=True, blank=True)
    rv_marks = models.FloatField(null=True, blank=True)
    rv_updated = models.CharField(max_length=2, null=True, blank=True)

    course_category = models.CharField(
        max_length=2,
        choices=COURSE_CATEGORIES,
    )
    report_name = models.CharField(max_length=255, null=True, blank=True)

    def str(self):
        return f"{self.exam_code} - {self.student_name} - {self.subject_name}"