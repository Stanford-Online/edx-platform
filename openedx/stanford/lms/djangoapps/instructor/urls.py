from django.conf.urls import url

import openedx.stanford.lms.djangoapps.instructor.views.api


urlpatterns = [
    url(
        r'delete_report_download',
        openedx.stanford.lms.djangoapps.instructor.views.api.delete_report_download,
        name='delete_report_download',
    ),
    url(
        r'^get_blank_lti$',
        openedx.stanford.lms.djangoapps.instructor.views.api.get_blank_lti,
        name='get_blank_lti',
    ),
    url(
        r'get_course_forums_usage',
        openedx.stanford.lms.djangoapps.instructor.views.api.get_course_forums_usage_view,
        name='get_course_forums_usage',
    ),
    url(
        r'get_ora2_responses/(?:(?P<include_email>\w+)/)?$',
        openedx.stanford.lms.djangoapps.instructor.views.api.get_ora2_responses_view,
        name='get_ora2_responses',
    ),
    url(
        r'get_student_forums_usage',
        openedx.stanford.lms.djangoapps.instructor.views.api.get_student_forums_usage_view,
        name='get_student_forums_usage',
    ),
    url(
        r'^get_student_responses$',
        openedx.stanford.lms.djangoapps.instructor.views.api.get_student_responses_view,
        name='get_student_responses',
    ),
    url(
        r'^graph_course_forums_usage',
        openedx.stanford.lms.djangoapps.instructor.views.api.graph_course_forums_usage,
        name='graph_course_forums_usage',
    ),
    url(
        r'^upload_lti$',
        openedx.stanford.lms.djangoapps.instructor.views.api.upload_lti,
        name='upload_lti',
    ),
]
