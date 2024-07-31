from django.urls import path
from .views import RegisterView, LoginView, PublicArticleListView, PrivateArticleListView, ArticleCreateView, ArticleUpdateDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('articles/', PublicArticleListView.as_view(), name='public_articles'),
    path('articles/private/', PrivateArticleListView.as_view(), name='private_articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='create_article'),
    path('articles/<int:pk>/', ArticleUpdateDeleteView.as_view(), name='article_detail'),
]