from django.urls import path
from . import views



urlpatterns = [
    path(
        "articles/<str:country>/<str:category>",
        views.ArticlesByCountryAndCategoryAPIView.as_view(),
    ),
]