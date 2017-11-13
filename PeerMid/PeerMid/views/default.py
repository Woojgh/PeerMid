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

@view_config(route_name='cat_view', renderer='../templates/cat_view.jinja2', require_csrf=False)
def cat_view(request):
    """Detailed view for one journal cat based on it's id."""
    the_id = int(request.matchdict['id'])
    cat = request.dbsession.query(CATS).get(the_id)

    if not cat:
        raise HTTPNotFound

    if request.method == 'GET':
        return {
            'cat': cat
        }

    if request.method == 'POST':
        return HTTPFound(
            location=request.route_url('update_view', id=cat.id)
        )

    return {}

