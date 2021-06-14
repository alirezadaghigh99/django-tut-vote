from django.urls import path
from . views import index_vote, all_questions, show_detail
app_name = "vote"
urlpatterns = [
    path('', index_vote, name='index' ),
    path('questions/', all_questions, name='all' ),
    path('questions/<int:question_id>/', show_detail, name='detail'),

]
