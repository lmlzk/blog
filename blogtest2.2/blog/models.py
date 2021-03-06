from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    avatar = models.ImageField(upload_to='static/images/avatar/%m', default='images/avatar/default.png', max_length=200, verbose_name="头像")
    qq = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="QQ号码")
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="电话号码")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


class Catagory(models.Model):
    name = models.CharField(max_length=30, verbose_name="分类名称")
    index = models.IntegerField(verbose_name="分类的排序")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="标签名称")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    img = models.ImageField(upload_to='static/images/img/%m', default='images/img/default.png',
                            max_length=200, verbose_name="图片")
    desc = models.CharField(max_length=50, verbose_name="文章描述")
    content = models.TextField(verbose_name="文章内容")
    click_count = models.IntegerField(default=0, verbose_name="点击次数")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    user = models.ForeignKey(User, verbose_name="用户")
    catagory = models.ForeignKey(Catagory, blank=True, null=True, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="广告标题")
    desc = models.CharField(max_length=200, verbose_name="广告描述")
    image = models.ImageField(upload_to='static/images/ad/%m', verbose_name="图片路径")
    callback_url = models.URLField(null=True, blank=True, verbose_name="回答url")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="排列顺序（从小到大）")

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title


class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=200, verbose_name="友情链接描述")
    callback_url = models.URLField(verbose_name="url地址")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="排列顺序（从小到大）")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    date_publish = models.DateField(auto_now_add=True, verbose_name="发布时间")
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name="父级评论")
    user = models.ForeignKey(User, blank=True, null=True, verbose_name="用户")
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name="文章")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)




