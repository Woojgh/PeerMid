from pyramid.response import Response
from PeerMid.data.cats import CATS
from pyramid.view import view_config
import io
import os

HERE = os.path.dirname(__file__)

def home_page(request):
    imported_text = io.open(os.path.join(HERE, 'home.html')).read()
    return Response(imported_text)

@view_config(route_name='home', renderer='../templates/cat_list.jinja2')
def list_view(request):
    """View for listing cats."""
    return {"cats": CATS}