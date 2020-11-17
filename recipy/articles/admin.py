from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):

    #def delete_button(self, obj):
        #return format_html('<a class="btn" href="/admin/articles/Article/{}/delete/">Delete</a>', obj.id)


    list_display = ('title', 'featured', 'image_tag', 'date')


admin.site.register(Article, ArticleAdmin)

