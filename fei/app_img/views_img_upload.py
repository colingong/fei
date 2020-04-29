"""上传图片
"""

from django.conf import settings
import random
import time
import os
from app_drf.views_drf1 import full_user
from django import forms
from django.shortcuts import HttpResponse, render
from django.core.validators import FileExtensionValidator


class ImgUploadForm(forms.Form):
    给个沙雕宣言吧 = forms.CharField(max_length=50)
    上传个图片 = forms.FileField(
        validators=[FileExtensionValidator(['jpg', 'png', 'gif'])])


def process_file(uploaded_file, upload_to=None, url_prefix=None):
    _, file_extension = os.path.splitext(uploaded_file.name)
    image_to_save = os.path.join(settings.BASE_DIR, upload_to)
    filename = str(int(time.time())) + '_' + \
        str(random.randint(1, 9999)) + file_extension
    full_file = os.path.join(image_to_save, filename)
    print(f'===> saved to file: {full_file}')
    with open(full_file, 'wb+') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)
    return url_prefix + filename


def get_file_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext


def upload(request):
    if request.method == 'POST':
        UPLOAD_TO, URL_PREFIX = 'collect_serve/upload/', 'upload/'

        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            saved_file = process_file(
                request.FILES['上传个图片'],
                upload_to=UPLOAD_TO,
                url_prefix=URL_PREFIX
                )
            return HttpResponse(f'<img src="/static/{saved_file}" style="height: 50%; width: 50%; object-fit: contain">')
        else:
            print('---> form.is_valid FAILED!')
            print(form.errors)
            return HttpResponse('ERROR: ' + str(form.errors))
    else:
        form = ImgUploadForm()
        return render(request, 'app_img/upload.html', {'form': form})


def display_img(request):
    return render(request, 'app_img/display_img.html')
