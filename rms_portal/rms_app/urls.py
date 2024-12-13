from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('authors', authors_tab, name='authors'),
    path('authors/add', save_author),
    path('authors/edit/<int:author_id>', edit_author, name='edit_author'),
    path('authors/delete/<int:author_id>', delete_author, name='delete_author'),
    path('studies', studies_list, name='studies_list'),
    path('studies/add', add_study, name='add_study'),
    path('studies/edit/<int:study_id>', edit_study, name='edit_study'),
    path('studies/delete/<int:study_id>', delete_study, name='delete_study'),
    path('studies/detail/<int:study_id>', study_detail, name='study_detail'),  # Add this line for the detail view
]
