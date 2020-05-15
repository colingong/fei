from django.shortcuts import render, HttpResponse
from . import forms

# Create your views here.
def alive(request):
    return HttpResponse(request, 'alive - app_comments')

def leave_comments(request):
    if request.method == 'GET':
        form = forms.AnonymousCommentsForm()
        return render(request, 'app_comments/comments.html', {'form': form})
    elif request.method == 'POST':
        comments_form = forms.AnonymousCommentsForm(request.POST)
        if comments_form.is_valid():
            comments_form.save()
            return HttpResponse('谢谢！')