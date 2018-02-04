from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .models import Category,Tag,Post,Comment,AboutSite,AboutMe,FriendWeb,MessageBoard,WebSettings
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
from django.http import HttpResponse,JsonResponse

# Create your views here.

tags_color=['primary','secondary','success','warning','alert']*5
web_settings=WebSettings.objects.filter(active=True)

def get_categories():
    return Category.objects.all()

def post_list(request,tag_slug=None,cate_slug=None):
    object_list=Post.published.all()
    tag,cate=None,None
    re_htm='index.html'
    selected='index'
    host_posts=Post.published.order_by('-views')[:10]
    recent_posts=Post.published.order_by('-publish')[:10]
    cates_list=Category.objects.all()
    comments_last=Comment.objects.filter(active=True).order_by('-created_time',)[:10]
    tags_list=Tag.objects.all()

    if tag_slug:
        tag=get_object_or_404(Tag,id=tag_slug)
        object_list=object_list.filter(tags__in=[tag])

    if cate_slug:
        cate=get_object_or_404(Category,id=cate_slug)
        object_list=object_list.filter(category=cate).order_by('-publish')
    posts_count=object_list.count()
    paginator=Paginator(object_list,5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,re_htm,{'page':page,
                                       'posts':posts,
                                       'posts_count':posts_count,
                                       'tag':tag,
                                       'cate':cate,
                                       'section':selected,
                                       'host_posts':host_posts,
                                       'recent_posts':recent_posts,
                                       'cates_list':cates_list,
                                       'comments_last':comments_last,
                                       'tags_list':tags_list,
                                       'tags_color':tags_color,
                                       'web_settings':web_settings,})


def post_detail(request,year,month,day,slug,tag_slug=None,cate_slug=None):
    post=get_object_or_404(Post,
                           status = 'published',
                           publish__year = year,
                           publish__month = month,
                           publish__day = day,
                           id=slug,)
    post.views_count()
    comments=post.comments.filter(active=True)

    cc = None
    cc_name = None

    if request.method=='POST':
        cc_name = request.POST.get('cc_name')
        cc = request.POST.get('cc')
        if cc and cc_name:

            cc=Comment(post=post,reader_name=cc_name,body=cc)
            cc.save()

    host_posts=Post.published.order_by('-views')[:10]
    recent_posts=Post.published.order_by('-publish')[:10]
    cates_list=Category.objects.all()
    comments_last=Comment.objects.filter(active=True).order_by('-created_time',)[:10]
    tags_list=Tag.objects.all()
    test='test_detail'

    tag = None
    if tag_slug:
        tag=get_object_or_404(Tag,id=tag_slug)



    return render(request,'detail.html',{'post':post,
                                         'tag':tag,
                                         'host_posts':host_posts,
                                         'recent_posts':recent_posts,
                                         'cates_list':cates_list,
                                         'comments':comments,
                                         'comments_last':comments_last,
                                         'tags_list':tags_list,
                                         'tags_color':tags_color,
                                         'web_settings':web_settings,
                                         'test':test,})

def submit_comments(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method == 'POST':
        cc_name = request.POST.get('cc_name')
        cc = request.POST.get('cc')
        if cc and cc_name:
            cc = Comment(post=post, reader_name=cc_name, body=cc)
            cc.save()
    comments=post.comments.filter(active=True)
    test='test_submit'
    #if request.is_ajax():
    #return JsonResponse({'post':post,'comments':comments,})
    return render(request,'comments_list.html',{'comments':comments,
                                                'post':post,
                                                'test':test,})


def about(request):
    aboutsite_posts=AboutSite.objects.all()
    aboutme_posts=AboutMe.objects.all()
    messages=MessageBoard.objects.filter(active=True)
    paginator = Paginator(messages, 100)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    friend_web_list=FriendWeb.objects.filter(active=True)


    return render(request,'about.html',{'aboutsite_posts':aboutsite_posts,
                                        'aboutme_posts':aboutme_posts,
                                        'messages':messages,
                                        'friend_web_list':friend_web_list,
                                        'web_settings':web_settings,
                                        'posts':posts,})

def submit_message(request):
    if request.method == 'POST':
        message_name = request.POST.get('cc_name')
        message_body = request.POST.get('cc')
        if message_body and message_name:
            message = MessageBoard(name=message_name, body=message_body)
            message.save()

    messages=MessageBoard.objects.filter(active=True)

    return render(request,'comments_list.html',{'messages':messages,})