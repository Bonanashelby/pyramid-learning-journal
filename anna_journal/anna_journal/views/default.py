"""Views for Learning Journal."""
from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """The list of journal entries."""
    with io.open(os.path.join(HERE, '../templates/index.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def detail_view(request):
    """A single journal entry."""
    with io.open(os.path.join(HERE, '../templates/detail.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def create_view(request):
    """Creating a new view."""
    with io.open(os.path.join(HERE, '../templates/form.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def update_view(request):
    """Updating an existing view."""
    with io.open(os.path.join(HERE, '../templates/form_edit.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)
