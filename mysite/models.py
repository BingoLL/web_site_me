from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


#from PIL import Image
#from io import StringIO
#from django.core.files.uploadedfile import SimpleUploadedFile
#from django_thumbs.db.models import ImageWithThumbsField

#from sorl.thumbnail import get_thumbnail

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'



class Tag(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'),)
    title=models.CharField(max_length=250,verbose_name='文章标题')
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    #thumb=ImageWithThumbsField(upload_to='photos/thumbs/%Y/%m/%d/',sizes=((200,90),))
    #post_thumb=get_thumbnail(upload_to='photos/thumbs/%Y/%m/%d/','186x90',corp='center',quality=99)
    category=models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,related_name='blog_posts')
    body=RichTextUploadingField(default='',verbose_name='正文')
    publish=models.DateTimeField(default=timezone.now,verbose_name='发布时间')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='published',verbose_name='文章状态')
    views=models.PositiveIntegerField(default=0)
    objects=models.Manager()
    published=PublishedManager()

    class Meta:
        ordering=('-publish',)
        verbose_name='文章'
        verbose_name_plural='文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mysite:post_detail',args=[self.publish.year,
                                                  self.publish.strftime('%m'),
                                                  self.publish.strftime('%d'),
                                                  self.slug])

    def views_count(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments')
    reader_name=models.CharField(max_length=80,null=True,verbose_name='读者名字')
    body=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    views=models.PositiveIntegerField(default=0)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created_time',)
        verbose_name='评论'
        verbose_name_plural='评论'

    def __str__(self):
        return '{}评论了文章《{}》'.format(self.reader_name,self.post)



#about.html,此页面四个选项卡
class AboutSite(models.Model):
    body=RichTextUploadingField(default='',verbose_name='关于本站正文')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('created_time',)
        verbose_name='关于本站'
        verbose_name_plural='关于本站'

class AboutMe(models.Model):
    body=RichTextUploadingField(default='',verbose_name='关于作者正文')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('created_time',)
        verbose_name='关于作者'
        verbose_name_plural='关于作者'

class FriendWeb(models.Model):
    logo_pic=models.ImageField(upload_to='photos/friend_log/%Y/%m/%d/',verbose_name='友情链接logo图片',help_text='请上传40*120像素logo')
    friend_web_name=models.CharField(max_length=80,verbose_name='网站名字')
    web_address=models.CharField(max_length=100,verbose_name='网址')
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created',)
        verbose_name='友情链接'
        verbose_name_plural='友情链接'

    def __str__(self):
        return self.friend_web_name

class MessageBoard(models.Model):
    name=models.CharField(max_length=80,null=True,verbose_name='昵称')
    body=models.TextField(verbose_name='欢迎留言')
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)
        verbose_name_plural='留言'
        verbose_name='留言'

