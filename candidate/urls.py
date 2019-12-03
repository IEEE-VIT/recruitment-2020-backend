from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from candidate.views import CandidateViewSet, send_email_to_candidate
#
# candidate_list = CandidateViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# candidate_detail = CandidateViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('candidate/', candidate_list, name='candidate-list'),
#     path('candidate/<int:pk>/', candidate_detail, name='candidate-detail'),
#     path('candidate/<int:pk>/send_mail/', send_email_to_candidate, name='candidate-email')
# ])

from rest_framework import routers

from candidate.views import CandidateListViewset

CandidateRouter = routers.DefaultRouter(trailing_slash=False)


CandidateRouter.register(r'list', CandidateListViewset, "Candidate Lists")