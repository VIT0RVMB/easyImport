from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'easyImport.views.home', name='home'),
    # url(r'^easyImport/', include('easyImport.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^aula6/(?P<id>\d+)/$', 'aula6.views.detail', name='aula6_detail'),
    url(r'^painel/$', 'appPainel.views.logar', name='appPainel_logar'),
    url(r'^$', 'appPainel.views.index', name='appPainel_index'),
    url(r'^home/$', 'appPainel.views.home', name='appPainel_home'),
    url(r'^logout/$', 'appPainel.views.sair', name='appPainel_sair'),
    url(r'^sync/$', 'appPainel.views.sincronizar', name='appPainel_sincronizar'),

)
