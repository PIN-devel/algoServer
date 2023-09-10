import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Problem
from .serializers import ProblemSerializer

# base_url = 'https://www.acmicpc.net/problem/'
base_url = 'https://solved.ac/search?query='

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def retrieve(self, request, pk=None):
        problem = Problem.objects.filter(problem_id=pk).first()
        if problem is None:
            html = requests.get(base_url + pk, headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')
            a_tags = soup.find_all('a', href=f"https://www.acmicpc.net/problem/{pk}")
            difficulty = a_tags[0].find('img').get('alt')
            title = a_tags[1].text
            data = {
                'problem_id': pk,
                'title': title,
                'difficulty': difficulty,
            }
            serializer = ProblemSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            serializer = ProblemSerializer(problem)
            return Response(serializer.data, status.HTTP_200_OK)
