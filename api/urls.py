from django.urls import path
from .views import AdminViewSet
from.views import BookDetails
from.import views

app_name = 'api' 

urlpatterns = [
    path('',views.get_books),
    path('book/<int:id>/',BookDetails.as_view()),
    path('adminpanel/', AdminViewSet.as_view(), name="create_user"),

    ]