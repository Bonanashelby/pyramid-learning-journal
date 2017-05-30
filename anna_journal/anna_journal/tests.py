from pyramid import testing
from pyramid.response import Response
import pytest
import io
import os

HERE = os.path.dirname(__file__)


@pytest.fixture
def list_response():
    """Return a response from the list page."""
    from anna_journal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    return response


@pytest.fixture
def detail_response():
    """Return a response from the list page."""
    from anna_journal.views.default import detail_view
    request = testing.DummyRequest()
    response = detail_view(request)
    return response


@pytest.fixture
def create_response():
    """Return a response from the list page."""
    from anna_journal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    return response


@pytest.fixture
def update_response():
    """Return a response from the update page."""
    from anna_journal.views.default import update_view
    request = testing.DummyRequest()
    response = update_view(request)
    return response


def test_list_view_returns_response(list_response):
    """List view respond."""
    assert isinstance(list_response, Response)


def test_list_view_status_ok(list_response):
    """Show 200 status ok on list view."""
    assert list_response.status_code == 200


def test_list_view_returns_proper_content(list_response):
    """Home view response has file content."""
    with io.open(os.path.join(HERE, './templates/index.html')) as the_file:
        imported_text = the_file.read()
    assert imported_text in list_response.text


def test_detail_view_returns_response(detail_response):
    """detail view respond."""
    assert isinstance(detail_response, Response)


def test_detail_view_status_ok(detail_response):
    """Show 200 status ok on detail view."""
    assert detail_response.status_code == 200


def test_detail_view_returns_proper_content(detail_response):
    """Home view response has file content."""
    with io.open(os.path.join(HERE, './templates/detail.html')) as the_file:
        imported_text = the_file.read()
    assert imported_text in detail_response.text


def test_create_view_returns_response(create_response):
    """create view respond."""
    assert isinstance(create_response, Response)


def test_create_view_status_ok(create_response):
    """Show 200 status ok on create view."""
    assert create_response.status_code == 200


def test_create_view_returns_proper_content(create_response):
    """Home view response has file content."""
    with io.open(os.path.join(HERE, './templates/form.html')) as the_file:
        imported_text = the_file.read()
    assert imported_text in create_response.text


def test_update_view_returns_response(update_response):
    """update view respond."""
    assert isinstance(update_response, Response)


def test_update_view_status_ok(update_response):
    """Show 200 status ok on update view."""
    assert update_response.status_code == 200


def test_update_view_returns_proper_content(update_response):
    """Home view response has file content."""
    with io.open(os.path.join(HERE, './templates/form_edit.html')) as the_file:
        imported_text = the_file.read()
    assert imported_text in update_response.text
