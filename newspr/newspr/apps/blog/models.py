from django.db import models
from PIL import Image
from users.models import CustomUser
# Create your models here.


class Post(models.Model):
    title = models.CharField('Заголовок',max_length=50)
    text = models.TextField('Текст',max_length=4000)
    pub_date = models.DateTimeField('Дата публикации',auto_now_add=True)
    image = models.ImageField('Фотография',upload_to='images/',blank=True)
    views = models.IntegerField('Просмотры',default=0)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,verbose_name='Категория',related_name='posts')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        app_label = 'blog'

class Category(models.Model):
    name = models.CharField('Имя категории',max_length=50)
    slug = models.SlugField('URL',max_length=50,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        app_label = 'blog'

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Пользователь')
    text = models.CharField('Текст комментария',max_length=400)
    pub_date = models.DateTimeField('Дата публикации',auto_now_add=True)
    post = models.ForeignKey('Post',verbose_name='Пост',on_delete=models.CASCADE,null=True)

    # def __str__(self):
    #     return str(self.user) + ' | ' + self.text[:20]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        app_label = 'blog'

    


    