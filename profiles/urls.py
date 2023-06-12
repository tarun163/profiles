from django.urls import path
from profiles.views import ProfileCreateUpdateView

urlpatterns = [
    path('api/profiles/', ProfileCreateUpdateView.as_view(), name='profile-create-update'),
]
