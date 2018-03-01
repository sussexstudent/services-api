import rest_framework
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes, authentication_classes, \
    permission_classes
from rest_framework.parsers import BaseParser
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from graphene_django.views import GraphQLView
from wagtail.images.views.serve import ServeView

from falmer.schema.api import api_router
from falmer.auth import urls as auth_urls
from falmer.slack import urls as slack_urls
from falmer.launcher import urls as launcher_urls
from falmer.matte import urls as matte_urls
from falmer.search import urls as search_urls
from falmer.newsletters import urls as newsletters_urls
from falmer.frontend import urls as frontend_urls
from falmer.links import urls as links_urls


class DRFAuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super(GraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(GraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((AllowAny, ))(view)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = api_view(['GET', 'POST'])(view)
        return view

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),

    url(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(action=settings.IMAGE_SERVE_METHOD), name='wagtailimages_serve'),
    url(r'^content-api/v2/', api_router.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^pages/', include(wagtail_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^graphql', csrf_exempt(DRFAuthenticatedGraphQLView.as_view(graphiql=True))),
    url(r'^auth/', include(auth_urls)),
    url(r'^slack/', include(slack_urls)),
    url(r'^images/', include(matte_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^newsletters/', include(newsletters_urls)),
    url(r'^o/', include(links_urls)),

    url(r'^', include(launcher_urls)),
    url(r'^', include(frontend_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
