from rest_framework import serializers
from .models import ShortenedLink

class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedLink
        fields = ['original_url', 'shortened_code']
