from django.urls import path
from . views import index_vote,ShowAll, show_detail, ShowDetail
app_name = "vote"
urlpatterns = [
    path('', index_vote, name='index' ),
    path('questions/', ShowAll.as_view(), name='all' ),
    path('questions/vote/<pk>',ShowDetail.as_view(),name="show_detail" ),
    path('questions/<int:question_id>/', show_detail, name='detail'),

]
