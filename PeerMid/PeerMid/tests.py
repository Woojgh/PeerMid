from pyramid import testing
from pyramid.response import Response
from PeerMid.data.cats import CATS

def test_list_view_returns_dict():
    """Home view returns a Response object."""
    from PeerMid.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, dict)

def test_list_view_returns_proper_amount_of_content():
    """Home view response has file content."""
    from PeerMid.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert len(response['cats']) == len(CATS)
    
def test_home_view_returns_response():
    """Home view returns a Response object."""
    from PeerMid.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert isinstance(response, Response)

def test_home_view_is_good():
    """Home view response has a status 200 OK."""
    from PeerMid.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert response.status_code == 200

def test_home_view_returns_proper_content():
    """Home view response has html content."""
    from PeerMid.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert "Snorgle Cats" in response.text