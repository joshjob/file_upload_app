from django.shortcuts import render, redirect
from .models import UploadedFile, originaldata
from .forms import UploadFileForm
from django.contrib import messages
import pandas as pd
import sqlite3

def load_data(excel_file_path, sqlite_file_path, table_name, is_ug, report_name):
    df = pd.read_excel(excel_file_path)

    column_mapping = {
        'Exam Code': 'exam_code',
        'Student Batch Name': 'student_batch_name',
        'Batch Name': 'batch_name',
        'Class Name': 'class_name',
        'Student Name': 'student_name',
        'RegNo': 'reg_no',
        'Roll No': 'roll_no',
        'Exam Type': 'exam_type',
        'Subject Type': 'subject_type',
        'Subject Code': 'subject_code',
        'Subject Name': 'subject_name',
        'Semester': 'semester',
        'Obt Marks': 'obt_marks',
        'Max Marks': 'max_marks',
        'Obt Grade': 'obt_grade',
        'Is Backlog': 'is_backlog',
        'Is Pass': 'is_pass',
        'Backlog Attempt Number': 'backlog_attempt_number',
        'Credit Point Earned': 'credit_point_earned',
        'Credit Point Offered': 'credit_point_offered',
        'RV Marks': 'rv_marks',
        'RV Updated': 'rv_updated',
    }

    df.rename(columns=column_mapping, inplace=True)
    df['course_category'] = 'UG' if is_ug else 'PG'
    df['report_name'] = report_name

    conn = sqlite3.connect(sqlite_file_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()
            file_path = new_file.file.path

            course_category = request.POST.get('course_category')  # Correctly get course_category value from POST
            report_name = request.POST.get('report_name')

            # Ensure course_category is either 'UG' or 'PG'
            if course_category in dict(originaldata.COURSE_CATEGORIES):
                is_ug = (course_category == originaldata.UG)
            else:
                # Handle invalid case, default to False (PG)
                is_ug = False

            load_data(file_path, "db.sqlite3", "fileupload_originaldata", is_ug, report_name)

            messages.success(request, 'Successfully Uploaded')
            return redirect('main')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})


def display_excel_data(request):
    excel_data = originaldata.objects.all()
    context = {'excel_data': excel_data}
    return render(request, 'fileupload/main.html', context)

def upload_success(request):
    return render(request, 'fileupload/upload_success.html')

def file_uploaded(request, file_id):
    return HttpResponse(f"File uploaded with ID: {file_id}")

def home(request):
    return render(request, 'home.html')