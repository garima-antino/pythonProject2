import json
from django.shortcuts import render
from .models import Article
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer

# Create your views here.

class ArticlesByCountryAndCategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        country_name = self.kwargs["country"]
        category_name = self.kwargs["category"]

        #fetching data from api
        url = f"https://newsapi.org/v2/top-headlines?country={country_name}&category={category_name}&apiKey=ab0d3f9de358456889bd9595e8a8fb96"
        news_data = requests.get(url).json()
        article_detail = news_data['articles']

        #save Data
        for article in article_detail:
            title = article['title']
            description = article['description']
            published_at = article['publishedAt']
            if Article.objects.filter(title = title).exists()==False:
                Article.objects.create(title = title,description = description,published_at = published_at,category = category_name,country =country_name)

        #return data
        articles = Article.objects.filter(category = category_name,country = country_name)
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)


