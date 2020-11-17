from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from accounts.views import (login_view, register_view, logout_view)
from articles.views import (featured_article)
from homepage.views import (homepage)

admin.site.site_header = 'Recipy.me Staff Area'
admin.site.site_title = 'Recipy.me'
admin.site.index_title = 'Staff Area'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),

    path('admin/', admin.site.urls),

    path('', homepage, name='index'),

    url(r'^articles/', include('articles.urls')),
    # url(r'^$', TemplateView.as_view(template_name='index.html'),
    #     name='homepage'),
    url(r'^recipes', TemplateView.as_view(template_name='recipes-list.html'),
        name='recipes'),
    url(r'^blog/', include('articles.urls')),

    url(r'^pro', TemplateView.as_view(template_name='pro.html'),
        name='pro'),

    # url(r'^login/', login_view, name="login"),
    # url(r'^register/', register_view, name="register"),

    url(r'^logout/', logout_view, name="logout"),

    # url(r'^logout/$', logout_view, {'next_page': '/'}, name='logout'),

    path('loginmodal/',
        # LoginView.as_view(template_name='loginmodal.html'),
        login_view,
        name="mysite_login"
    ),

    path('registermodal/', register_view,
        name="mysite_register"
    ),

    url(r'^test/$', featured_article, name="featured"),

    url(r'^tinymce/', include('tinymce.urls')),

]
