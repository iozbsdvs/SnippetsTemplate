from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
                  path('', views.index_page, name="home"),
                  path('snippets/add', views.add_snippet_page, name="snippets-add"),
                  path('snippet/<int:snippet_id>/delete', views.snippet_delete, name="snippet-delete"),
                  path('snippets/list', views.snippets_page, name="snippets-list"),
                  path('snippets/list_user', views.snippets_user, name="snippets-user"),
                  path('snippet/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
                  path('login', views.login, name="login"),
                  path('logout', views.logout, name="logout"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
