from django.conf.urls import patterns, url

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

"""
This does not account for some edge cases. If sent malformed JSON or a view that isn't handled the client will receive a 500 server error response.
"""