from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.docs.history import CREATE, LIST
from api.serializers.history.show import HistoryShowSerializer
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
import pytesseract
import cv2
from models_app.models import History
from pathlib import Path


class HistoryView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(**CREATE)
    def post(self, request, *args, **kwargs):

        file = request.FILES.get("file")
        history = History.objects.create()
        history.imported_file = file
        history.save()

        current_dir = Path(__file__).resolve().parent.parent.parent
        image = cv2.imread(f"{current_dir}{history.imported_file.url}")
        string = pytesseract.image_to_string(image)
        history.result = string
        history.save()
        return Response(
            HistoryShowSerializer(history).data,
            status=status.HTTP_201_CREATED,
        )

    @swagger_auto_schema(**LIST)
    def get(self, request, *args, **kwargs):
        history = History.objects.all().order_by("-id")
        return Response(
            HistoryShowSerializer(history, many=True).data,
            status=status.HTTP_200_OK,
        )
