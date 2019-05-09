from django.core.management.base import BaseCommand, CommandError
from project.serializers import ShoeTypeSerializer, ShoeColorSerializer
from project.models import ShoeType
from project.views import PostTypeAndColor
from rest_framework.views import APIView
from django.http import JsonResponse

class Command(BaseCommand):
    help = 'Submits data for shoe type and color'

    def handle(self, *args, **options):
        sneaker = {'style': 'sneaker'}
        boot = {'style': 'boot'}
        sandal = {'style': 'sandal'}
        dress = {'style': 'dress'}
        other = {'style': 'other'}
        red = {'color_name': 'red'}
        orange = {'color_name': 'orange'}
        yellow = {'color_name': 'yellow'}
        green = {'color_name': 'green'}
        blue = {'color_name': 'blue'}
        indigo = {'color_name': 'indigo'}
        violet = {'color_name': 'violet'}
        white = {'color_name': 'white'}
        black = {'color_name': 'black'}
        PostTypeAndColor.shoetype(APIView, sneaker)
        PostTypeAndColor.shoetype(APIView, boot)
        PostTypeAndColor.shoetype(APIView, sandal)
        PostTypeAndColor.shoetype(APIView, dress)
        PostTypeAndColor.shoetype(APIView, other)
        PostTypeAndColor.shoecolor(APIView, red)
        PostTypeAndColor.shoecolor(APIView, orange)
        PostTypeAndColor.shoecolor(APIView, yellow)
        PostTypeAndColor.shoecolor(APIView, green)
        PostTypeAndColor.shoecolor(APIView, blue)
        PostTypeAndColor.shoecolor(APIView, indigo)
        PostTypeAndColor.shoecolor(APIView, violet)
        PostTypeAndColor.shoecolor(APIView, white)
        PostTypeAndColor.shoecolor(APIView, black)

