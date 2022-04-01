from django.urls import path

from translator.views import (projects, 
                              ProjectDetailView, 
                              ProjectListView, 
                              CreateProject,
                              create_project,
                              add_text,
                              text_detail,
                              text_edit,
                              edit_project,
                              translate_editor)

app_name = 'translator'

urlpatterns = [
    path('translate_editor/<slug:text_slug>/', translate_editor, name="translate_editor"),
    # path('create_project/', create_project, name="create_project"),
    # create view with generic class based view
    path('create_project/', CreateProject.as_view(), name="create_project"),
    path('', ProjectListView.as_view(), name="project_list"),
    path('<slug:slug>/', ProjectDetailView.as_view(), name="project_detail"),
    path('edit_project/<slug:project_slug>', edit_project, name="edit_project"),
    # path('projects/', projects, name="list"),
    path('add_text/<slug:project_slug>/', add_text, name="add_text"),
    path('edit_text/<slug:text_slug>/', text_edit, name="text_edit"),
    path('<slug:project_slug>/<slug:text_slug>/', text_detail, name="text_detail"),
]