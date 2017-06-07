"""Views for Learning Journal."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from anna_journal.models import Journals
from datetime import datetime


@view_config(route_name='list_view', renderer='../templates/index.jinja2')
def list_view(request):
    """Display list of journal entries."""
    JOURNALS = request.dbsession.query(Journals).all()
    return {
        'journals': JOURNALS
    }


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """View single journal entry."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journals).get(entry_id)
    return {
        'entry': entry
    }


@view_config(route_name='create_view', renderer='../templates/form.jinja2')
def create_view(request):
    """Create a new view."""
    if request.method == "POST" and request.POST:

        if request.POST['title'] and request.POST['body']:
            form_data = request.POST
            new_entry = Journals(
                title=form_data['title'],
                body=form_data['body'],
                creation_date=datetime.now(),
            )
            request.dbsession.add(new_entry)
            return HTTPFound(location=request.route_url('list_view'))

    return request.POST


@view_config(
    route_name='update_view',
    renderer='../templates/form_edit.jinja2'
)
def update_view(request):
    """Update an existing view."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Journals).get(entry_id)
    if not entry:
        return HTTPNotFound
    if request.method == "GET":
        return {
            'title': entry.title,
            'body': entry.body
        }
    if request.method == "POST":
            form_data = request.POST
            entry.title = form_data['title']
            entry.body = form_data['body']
            request.dbsession.flush()
            return HTTPFound(location=request.route_url('detail_view', id=entry_id))
