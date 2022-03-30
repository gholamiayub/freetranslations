from django.urls import path
from django.views.generic import TemplateView

from user_account.views import user_github


app_name = 'user_account'

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='base.html'), name="home"),
    # path('home/', user_github, name="home"),
    path('editor/', TemplateView.as_view(template_name='md_editor.html')),
]