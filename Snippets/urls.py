from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
                  path('', views.index_page, name="home"),
                  path('snippets/add', views.add_snippet_page, name="snippets-add"),
                  path('snippet/<int:snippet_id>/delete', views.snippet_delete, name="snippet-delete"),
                  path('snippets/list', views.snippets_page, name="snippets-list"),
                  path('snippets/my', views.snippet_my, name="snippets-my"),
                  path('snippet/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
                  path('auth/register', views.create_user, name='register'),
                  path('comment/add', views.comment_add, name="comment_add"),
                  path('login', views.login, name="login"),
                  path('logout', views.logout, name="logout"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
