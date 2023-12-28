from rest_framework import serializers
from models_app.models import History


class HistoryShowSerializer(serializers.ModelSerializer):
    imported_file = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    def get_result(self, instance):
        if instance.result:
            return instance.result
            # return f"{BASE_DOMAIN}{instance.imported_file.url}"
        return "Empty"


    def get_imported_file(self, instance):
        if instance.imported_file:
            return f"https://76ac-82-140-201-204.ngrok-free.app{instance.imported_file.url}"
            # return f"{BASE_DOMAIN}{instance.imported_file.url}"
        return ""

    class Meta:
        model = History
        fields = "__all__"
