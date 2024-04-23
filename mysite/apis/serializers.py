from rest_framework import serializers
from apis.models import Poster, Template
from django.core.files.base import ContentFile
import requests
from django.db import transaction

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

    def download_and_store_file(self, url):
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    content = response.content
                    file_name = url.rsplit("/",1)[1]
                    return ContentFile(content), file_name
                return None, None
            except Exception as e:
                print(e)
                return None, None

    def save(self):
        with transaction.atomic():
            preview_image_file = self.validated_data["preview_image"]
            zip_file = self.validated_data["file_url"]
            instance = super().create(self.validated_data)
            if preview_image_file:
                preview_image_file_content,file_name = self.download_and_store_file(preview_image_file)
                if preview_image_file_content:
                    instance.preview_image_file.save(file_name, preview_image_file_content, save=True)
            if zip_file:
                zip_file_content,file_name = self.download_and_store_file(zip_file)
                if zip_file_content:
                    instance.zip_file.save(file_name, zip_file_content, save=True)
            return instance
