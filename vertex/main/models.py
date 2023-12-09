from django.db import models
from django.utils.html import mark_safe


class Blog(models.Model):
    img = models.ImageField('Blog Image' , upload_to='media')
    title = models.CharField('Blog Title', max_length=100)
    describtion = models.TextField('Describtion')
    post_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "100"/>')

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blogs'

class OurServices(models.Model):

    service1 = models.TextField('First Service')
    service2 = models.TextField('Second Service')    

    def __str__(self) -> str:
        return "OurServices"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Gallery(models.Model):

    img = models.ImageField('Image', upload_to="media")
    img_display = models.ImageField("Large Image" , upload_to='media', null= True)
    title = models.CharField('Title', max_length=50)
    text = models.CharField('Text', max_length=50)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class ContactUs(models.Model):
    name = models.CharField('Name' , max_length=100)
    email = models.EmailField('Email')
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class HomeBG(models.Model):
    bg1 = models.ImageField('Back Ground Image', upload_to='media')
    bg2 = models.ImageField('Back Ground Image', upload_to='media')
    bg3 = models.ImageField('Back Ground Image', upload_to='media')
    bg4 = models.ImageField('Back Ground Image', upload_to='media')

    def __str__(self) -> str:
        return "BG"
    
    class Meta:
        verbose_name = 'Home BG'
        verbose_name_plural = 'Home BG'

class Icons(models.Model):
    icon = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self) -> str:
        return self.icon

    class Meta:
        verbose_name = "Icons"
        verbose_name_plural = "Icons"




class AboutUs(models.Model):
    t1 = models.TextField()
    t2 = models.TextField()
    t3 = models.TextField()

    def __str__(self) -> str:
        return 'About Us'
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'










