from pyramid import testing
from pyramid.response import Response


def test_home_view_returns_response():
    """Home view returns a Response object."""
    from expense_tracker.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert isinstance(response, Response)

def test_home_view_is_good():
    """Home view response has a status 200 OK."""
    from expense_tracker.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert response.status_code == 200

def test_home_view_returns_proper_content():
    """Home view response has html content."""
    from expense_tracker.views.default import home_page
    request = testing.DummyRequest()
    response = home_page(request)
    assert "Snorgle Cats" in response.text