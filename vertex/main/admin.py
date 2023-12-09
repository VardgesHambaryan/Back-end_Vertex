from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_date' , 'img_preview']
    list_display_links = ['title', 'post_date' , 'img_preview']
    search_fields = ['title', 'post_date' , 'describtion']
    readonly_fields = ['img_preview']



admin.site.register(OurServices)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(HomeBG)
admin.site.register(AboutUs)
admin.site.register(Icons)




