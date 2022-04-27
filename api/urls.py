from django.urls import path
from .views import AdminViewSet
from.views import BookDetails
from.import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api' 

urlpatterns = [
    path('',views.get_books),
    path('book/<int:id>/',BookDetails.as_view()),
    path('adminpanel/', AdminViewSet.as_view(), name="create_user"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    ]  