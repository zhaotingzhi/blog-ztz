from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=20,unique=True,verbose_name='类别名称')

    class Meta:
        db_table = 't_category'
        verbose_name_plural='类别'

    def __str__(self):
        return u'Category:%s'%self.cname

class Tags(models.Model):
    tname = models.CharField(max_length=20,unique=True,verbose_name='标签名称')

    class Meta :
        db_table = 't_tags'
        verbose_name_plural='标签'

    def __str__(self):
        return u'Tags:%s'%self.tname

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='标题')
    desc = models.TextField(verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    created = models.DateField(auto_now_add=True,verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    category = models.ForeignKey(Category,verbose_name='目录')
    tags = models.ManyToManyField(Tags,verbose_name='标签')

    class Meta:
        db_table = 't_post'
        verbose_name_plural='帖子'

    def __str__(self):
        return u'Post%s'%self.title