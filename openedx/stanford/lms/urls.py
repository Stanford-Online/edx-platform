from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url

import openedx.stanford.lms.djangoapps.inline_analytics.answer_distribution
import openedx.stanford.djangoapps.sneakpeek.views


urlpatterns = [
    url(
        r'^course_sneakpeek/{}/$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        openedx.stanford.djangoapps.sneakpeek.views.setup_sneakpeek,
        name='course_sneakpeek',
    ),
    url(
        r'^get_analytics_answer_dist/',
        openedx.stanford.lms.djangoapps.inline_analytics.answer_distribution.get_analytics_answer_dist,
        name='get_analytics_answer_dist',
    ),
]
if settings.FEATURES.get('ENABLE_SUPERUSER_LOGIN_AS'):
    urlpatterns += [
        url(
            r'',
            include('openedx.stanford.djangoapps.superuser_login_as.urls'),
        ),
    ]
