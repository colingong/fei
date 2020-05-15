"""some global views"""

from django.shortcuts import HttpResponse, Http404, render, redirect


def favicon(request):
    """简单粗暴的提供一个favicon.ico

        显然用django来提从文件服务是低效的
        用nginx来处理这种文件服务更合适
    """
    try:
        with open('static/favicon.ico', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/x-icon")
    except:
        return Http404

def v2_root(request):
    urls = [
        '/v2/api1/',
        '/v2/api2/',
    ]
    return render(request, 'v2_apis.html', {'urls': urls})

from app_comments.forms import AnonymousCommentsForm

def site_root(request):
    """提供一个主页，在主页上提供文档、接口等等链接，作为本demo项目的客户入口
    """
    if request.method == 'GET':
        form = AnonymousCommentsForm()
        return render(request, "site_root.html", {'form': form})
    elif request.method == 'POST':
        form = AnonymousCommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('留言收到，谢谢！')
    else:
        return redirect('/')