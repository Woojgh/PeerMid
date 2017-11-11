from pyramid.response import Response


def home_page(request):
    """View page for the Home ways"""
    return Response("This is my dumb view")