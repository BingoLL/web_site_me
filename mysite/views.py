from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Category,Tag,Post,Comment,AboutSite,AboutMe,FriendWeb,MessageBoard
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def get_categories():
    return Category.objects.all()

def post_list(request,tag_slug=None,cate_slug=None):
    object_list=Post.published.all()
    tag,cate=None,None
    re_htm='index.html'
    selected='index'
    host_posts=Post.published.order_by('views')[:15]
    recent_posts=Post.published.order_by('-publish')[:15]
    cates_list=Category.objects.all()

    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        object_list=object_list.filter(tags__in=[tag])

    if cate_slug:
        cate=get_object_or_404(Category,id=cate_slug)
        object_list=object_list.filter(category=cate).order_by('-publish')

    paginator=Paginator(object_list,4)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(pagenator.num_pages)
    return render(request,re_htm,{'page':page,
                                       'posts':posts,
                                       'tag':tag,
                                       'cate':cate,
                                       'section':selected,
                                       'host_posts':host_posts,
                                       'recent_posts':recent_posts,
                                       'cates_list':cates_list,
                                       })


