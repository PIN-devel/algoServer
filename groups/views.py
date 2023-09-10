import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from .models import Group, Round
from .serializers import GroupSerializer, RoundSerializer, RoundDetailSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        leader_id = request.data.get('leader_id')
        leader = get_object_or_404(User, id=leader_id)

        group = Group(leader=leader, **request.data)
        group.save()

        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_round(request, group_id):
    data = request.data
    data["group"] = group_id
    serializer = RoundSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def get_or_patch_round(request, round_id):
    group_round = get_object_or_404(Round, id=round_id)
    if request.method == 'GET':
        serializer = RoundDetailSerializer(group_round)
        participants = serializer.data.get("participants")
        problems = serializer.data.get("problems")

        for problem in problems:
            for participant in participants:
                url = f"https://www.acmicpc.net/status?problem_id={problem.get('problem_id')}&user_id={participant.get('baekjoon_id')}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                }
                html = requests.get(url, headers=headers).text
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find(id="status-table")
                submitted_times = list(
                    map(lambda x: x.get("title"), table.find_all(class_="real-time-update show-date")))
                print(
                    submitted_times)

                if "submitted_data" in participant:
                    participant["submitted_data"].append(
                        {"problem": problem.get('problem_id'), "submitted_times": submitted_times})
                else:
                    participant["submitted_data"] = [
                        {"problem": problem.get('problem_id'), "submitted_times": submitted_times}]

        return Response(serializer.data)
    else:
        serializer = RoundSerializer(group_round, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
