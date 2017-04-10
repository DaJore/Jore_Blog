# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.core.paginator import Paginator


# Create your views here.


def home(request):                                         # 网站首页(显示最新更新的文章)
    article_num = Article.objects.all().count()
    if article_num >= 8:
        update_list = Article.objects.all().order_by('-date')[:8]
    else:
        update_list = Article.objects.all().order_by('-date')[:article_num]
    # send = {'title': post}
    # str1 = ("title = %s, tag = %s, date = %s, content = %s"
    #         % (post.title, post.tag, post.date, post.content))
    # str1 = post.title
    return render(request, "home.html", {'update_list': update_list})


def getpages():# 计算文章共多少页
    object_num = Article.objects.all().count()
    if object_num == 0:# 当数据库中没有文章时
        blog_pages = 1
    else:
        num = divmod(object_num, 6)
        if num[1] != 0 or object_num < 6:
            blog_pages = num[0]+1
        elif num[1] == 0 and object_num > 6:
            blog_pages = num[0]
    return blog_pages


def blog_paging(request, page):
    page = (1 if page == '' else int(page))                                    # 当前页码
    pages = [x for x in range(1, getpages()+1)]          # 所有页码列表
    end = pages[-1]
    if page > end:                                       # 当页码超出范围时
        return render(request, "page_not_exists.html")
    elif getpages() > 1:                                 # 文章是否多于6篇
        if page == end:#最后一页时对剩余的文章如何显示
            content_list = Article.objects.all().order_by('-date')[(page-1)*6:]
        else:
            content_list = Article.objects.all().order_by('-date')[(page - 1) * 6:page * 6]     # 从数据库选出文章
        return render(request, "blog_all_list.html", {'content_list': content_list, 'pages': pages,
                                                      'end': end, 'flag': 'yes', 'page': page})
    elif getpages() == 1 and Article.objects.all().count() == 0:# 数据库没有文章
        return render(request, 'zeroArticle.html')
    else:#有文章但少于6篇
        content_list = Article.objects.all().order_by('-date')[(page - 1) * 6:]
        return render(request, "blog_all_list.html", {'content_list': content_list, 'pages': pages,
                                                      'end': end, 'flag': 'no', 'page': page})


def blog_detail(request, a):# 每篇文章详细内容
    mark = int(a)
    want_show = Article.objects.get(id=mark)
    return render(request, "detail.html", {'want_show': want_show})


# def blog_search(request):                  # blog搜索
#     # if 'kw' in request.GET:
#     kw = request.GET['kw']
#     if kw == '':
#         return render(request, "result.html", {'flag': 'empty'})
#     else:
#         searched_blogs = Article.objects.filter(title__icontains=kw)
#         # return HttpResponse(len(searched_blogs))
#         geted_blog_num = len(searched_blogs)
#         return render(request, 'result.html', {'searched_blogs': searched_blogs,
#                                                'geted_blog_num': geted_blog_num})


# def test_request(request):                       # 检测request
#     response = request.META
#     response.sort()
#     html = []
#     for k, v in response:
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))
    # return HttpResponse(response)
