"""上传图片
"""

from .img_process.water_mark import CustEmoji
from django.conf import settings
import random
import time
import os
from app_drf.views_drf1 import full_user
from django import forms
from django.shortcuts import HttpResponse, render
from django.core.validators import FileExtensionValidator

class EmojiTextForm(forms.Form):
    emoji = forms.CharField(label='当前表情包')
    text = forms.CharField(max_length=250)

def get_random_src_img(img_list):
    return random.choice(img_list)


def emoji(request):
    src_img_list = [
            'panda_src.jpg', 
            'panda_src2.jpg', 
            'panda_src3.jpg', 
            'panda_src4.jpg', 
            'panda_src5.jpg', 
            'panda_src6.jpg', 
            ]

    if request.method == 'GET':
        src_img = random.choice(src_img_list)
        form = EmojiTextForm(initial={'emoji': src_img})
        form.fields['text'].label = '给个沙雕宣言吧'
        return render(request, 'app_img/emoji.html', {
            'form': form, 
            'emoji_src': form["emoji"].value()})

    elif request.method == 'POST':
        form = EmojiTextForm(request.POST)
        if form.is_valid():
            # img_list = ['panda_src.jpg', 'panda_src2.jpg', 'panda_src3.jpg',
            #             'panda_src4.jpg', 'panda_src5.jpg', 'panda_src6.jpg']
            input_text = str(form.cleaned_data['text'])[:12]

            save_to_dir = os.path.join(settings.BASE_DIR, 'collect_serve/emoji/')
            url_prefix = '/static/emoji/'
            # src_img = get_random_src_img(img_list)
            src_img = form.cleaned_data['emoji']
            print(f'===> {form.cleaned_data}')

            current_emoji = CustEmoji(
                folder=save_to_dir, url_prefix=url_prefix, src_img=src_img)
            current_emoji.water_mark(input_text)
            return HttpResponse(f'<img style="height: 50%; width: 50%; object-fit: contain" src="{current_emoji.emoji_url}">')
        else:
            print(f'-------> {form.errors}')
    return HttpResponse('error')
