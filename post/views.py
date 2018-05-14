from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


# Create your views here.
def get_post_by_num(num):
    # 类型转换
    num = int(num)
    page_posts = Paginator(Post.objects.order_by('-created'), per_page=1)
    # 返回当前页数据
    # 首先判断当前页是否越界
    if num <= 0:
        num = 1
    if num > page_posts.num_pages:
        num = page_posts.num_pages

    # 生成页码数
    # 起始数
    start = int((num - 1) / 10) * 10 + 1
    # 结尾数
    end = start + 10
    # 判断end是否越界
    if end > page_posts.num_pages:
        end = page_posts.num_pages + 1
    return page_posts.page(num), range(start, end)


def index_view(request, num='1'):
    # 查询第一页的数据
    page_posts, page_range = get_post_by_num(num)

    return render(request, 'index.html', {'page_posts': page_posts, 'page_range': page_range})


def get_post_by_id(postid):
    return Post.objects.get(id=postid)


def post_view(request, postid):
    post = get_post_by_id(postid)

    return render(request,'detail.html',{'post':post})
