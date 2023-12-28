from drf_yasg import openapi
from api.serializers.test.show import HistoryShowSerializer


CREATE = {
    "operation_description": "Create History Object",
    "tags": ["history"],
    "manual_parameters": [
        openapi.Parameter(
            name="file",
            in_=openapi.IN_FORM,
            type=openapi.TYPE_FILE,
            description="file",
            required=False,
        ),
    ],
    "responses": {
        201: openapi.Response("Success", HistoryShowSerializer()),
    },
}


LIST = {
    "operation_description": "List of history objects",
    "tags": ["history"],
    "responses": {
        201: openapi.Response("Success", HistoryShowSerializer(many=True)),
    },
}