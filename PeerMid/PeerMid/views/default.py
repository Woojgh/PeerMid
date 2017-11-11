from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)

def home_page(request):
    imported_text = io.open(os.path.join(HERE, 'home.html')).read()
    return Response(imported_text)

