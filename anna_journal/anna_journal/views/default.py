"""Views for Learning Journal."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from anna_journal.data.journals import JOURNALS


@view_config(route_name='list_view', renderer='../templates/index.jinja2')
def list_view(request):
    """Display list of journal entries."""
    return {
        'journals': JOURNALS
    }


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """View single journal entry."""
    entry_id = int(request.matchdict['id'])
    entry = JOURNALS[entry_id]
    return {
        'entry': entry
    }


@view_config(route_name='create_view', renderer='../templates/form.jinja2')
def create_view(request):
    """Create a new view."""
    return {}


@view_config(
    route_name='update_view',
    renderer='../templates/form_edit.jinja2'
)
def update_view(request):
    """Update an existing view."""
    return {}
