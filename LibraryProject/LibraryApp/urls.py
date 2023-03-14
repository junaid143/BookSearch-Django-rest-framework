from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home_view , name = 'home'),
    path('dashboard/' , views.dashboard_view , name = 'dashboard'),
    path('addbook/' , views.addbook_view , name = 'addbook'),
    path('updatebook/<int:id>/' , views.updatebook_view , name = 'updatebook'),
    path('book_api/' , views.book_view ),
    path('book_api/action/<int:id>/' , views.action_view ),
]