from django.shortcuts import render, redirect
from .models import UploadedFile, ExcelData
from .forms import UploadFileForm, UploadExcelForm
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd  # Assuming pandas is installed

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()

            # Process the uploaded file (example using pandas to read Excel)
            excel_file = pd.ExcelFile(new_file.file.path)
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                # Example: Saving data to ExcelData model
                excel_data = ExcelData(file_name=sheet_name, file_content=new_file.file)
                excel_data.save()

        messages.success(request, 'Successfully Uploaded')
        return redirect('upload_success')
    
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})

def display_excel_data(request):
    excel_data = ExcelData.objects.all()
    context = {'excel_data': excel_data}
    return render(request, 'fileupload/main.html', context)

def upload_success(request):
    return render(request, 'fileupload/upload_success.html')

def file_uploaded(request, file_id):
    # Your view logic here
    return HttpResponse(f"File uploaded with ID: {file_id}")
# Create your views here.
