from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShortenedLink
import random
import string
from django.shortcuts import redirect


@api_view(["POST"])
def create_shortened_link(request):
    url = request.data.get("original_url")
    if url:
        code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        shortened_link = ShortenedLink.objects.create(
            original_url=url, shortened_code=code
        )
        return Response({"shortened_url": f"http://127.0.0.1:8000/api/{code}/"})
    return Response({"error": "URL is required"}, status=400)


@api_view(["GET"])
def redirect_shortened_link(request, code):
    try:
        link = ShortenedLink.objects.get(shortened_code=code)
        return redirect(link.original_url)
    except ShortenedLink.DoesNotExist:
        return Response({"error": "Link not found"}, status=404)
