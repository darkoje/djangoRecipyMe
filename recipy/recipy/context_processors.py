from django.conf import settings


def root_url(request):
    return {'SITE_URL': settings.RECIPY_ROOT_URL}

