from django.urls import path
from . views import index_vote
urlpatterns = [
    path('', index_vote )
]
