from django.db import models


# Create your models here.

# 用户类
class Admin(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True, null=False)
    password = models.CharField(verbose_name='密码', max_length=64, null=False)

    def __str__(self):
        return self.username

# 出版社类
class Publisher(models.Model):
    publisher_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=64, null=False, unique=True)
    date = models.DateField(verbose_name='创立日期', max_length=64, blank=True, null=True)
    introduction = models.TextField(verbose_name='简介', blank=True, null=True)

    def __str__(self):
        return self.name


# 作者类
class Author(models.Model):
    author_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=64, null=False, unique=True)
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, null=False)
    date = models.DateField(verbose_name='出生时间', max_length=64, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

# 插画师类
class Illustrator(models.Model):
    illustrator_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=64, null=False, unique=True)
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, null=False)
    date = models.DateField(verbose_name='出生时间', max_length=64, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

# 轻小说类型类：
class Type(models.Model):
    type_id = models.AutoField(verbose_name='ID', primary_key=True)
    type = models.CharField(verbose_name='类型', max_length=64, null=False, unique=True)

    def __str__(self):
        return self.type

# 轻小说类
class LightNovel(models.Model):
    book_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=64, null=False, unique=True)
    author = models.ForeignKey(verbose_name='作者', to=Author, to_field='author_id', on_delete=models.CASCADE, null=True)
    illustrator = models.ForeignKey(verbose_name='插画师', to=Illustrator, to_field='illustrator_id', on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(verbose_name='出版社', to=Publisher, to_field='publisher_id', on_delete=models.CASCADE, null=True)
    # type置空，其他级联删除
    type = models.ForeignKey(verbose_name='类型', to=Type, to_field='type_id', null=True, blank=True, on_delete=models.SET_NULL)
    count = models.CharField(verbose_name='卷数', max_length=64, null=True, blank=True)
    update_choices = (
        (1, "完结"),
        (0, "未完结")
    )
    update = models.SmallIntegerField(verbose_name='是否更新完', choices=update_choices, null=True, blank=True)
    date = models.DateField(verbose_name='出版日期', max_length=64, blank=True, null=True)
    introduction = models.TextField(verbose_name='简介', null=True, blank=True)
    image = models.FileField(verbose_name='封面', upload_to='image', default='image/default.png')
