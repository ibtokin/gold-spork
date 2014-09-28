from django.conf.urls import patterns, url

urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api-root'),
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$'
        views.SnippetHighlight.as_view(),
        name = 'snippet-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view()
        name='user-detail')
))

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace= 'rest_framework')),