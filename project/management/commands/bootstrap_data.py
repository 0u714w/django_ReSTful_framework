from django.core.management.base import BaseCommand, CommandError
from project.serializers import ShoeTypeSerializer, ShoeColorSerializer
from project.models import ShoeType
from project.views import PostTypeAndColor
from rest_framework.views import APIView
from django.http import JsonResponse

class Command(BaseCommand):
    help = 'Submits data for shoe type and color'

    STYLES = [{'style': 'sneaker'}, {'style': 'boot'}, {'style': 'sandal'}, {'style': 'dress'}, {'style': 'other'}]
    COLORS = [{'color_name': 'orange'}, {'color_name': 'yellow'}, {'color_name': 'green'}, {'color_name': 'blue'}, {'color_name': 'indigo'}, {'color_name': 'violet'}, {'color_name': 'white'}, {'color_name': 'black'}]

    def handle(self, *args, **options):
        for s in self.STYLES:
            PostTypeAndColor.shoetype(APIView, s)

        for c in self.COLORS:
            PostTypeAndColor.shoecolor(APIView, c)
        

