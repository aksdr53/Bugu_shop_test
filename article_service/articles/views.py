from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Article, User
from .serializers import ArticleSerializer, RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class PublicArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer

class PrivateArticleListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(is_public=False)

class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if not self.request.user.is_author:
            self.permission_denied(self.request)
        return super().get_permissions()

class ArticleUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        article = self.get_object()
        if article.author != self.request.user:
            self.permission_denied(self.request)
        return super().get_permissions()