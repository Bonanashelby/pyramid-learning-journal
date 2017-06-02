import pytest
from pyramid import testing
import transaction
# import io
# import os
import datetime 
from anna_journal.models import (
        Journals,
        get_tm_session
)
from anna_journal.models.meta import Base
from faker import Faker
import random


# HERE = os.path.dirname(__file__)
FAKE_FACTORY = Faker()
CATEGORIES = ["rent", "utilities", "groceries", "food", "netflix", "booze"]
JOUNRAL_LIST = [Journals(
    title=random.choice(CATEGORIES),
    body=FAKE_FACTORY.text(50),
    creation_date=datetime.datetime.now(),
) for i in range(5)]


@pytest.fixture(scope="session")
def configuration(request):
    """Set up a Configurator instance.

    This Configurator instance sets up a pointer to the location of the
        database.
    It also includes the models from your app's model package.
    Finally it tears everything down, including the in-memory SQLite database.

    This configuration will persist for the entire duration of your PyTest run.
    """
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres:///test_journals'
    })
    config.include("anna_journal.models")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a session for interacting with the test database.

    This uses the dbsession_factory on the configurator instance to create a
    new database session. It binds that session to the available engine
    and returns a new session for every call of the dummy_request object.
    """
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session.
    This is a function-level fixture, so every new request will have a
    new database session.
    """
    return testing.DummyRequest(db_session=db_session)


def test_model_gets_added(db_session):
    assert len(db_session.query(Journals).all()) == 0
    model = Journals(
        title=u"Fake Category",
        body=u"Some description text",
        creation_date=datetime.datetime.now(),
    )
    db_session.add(model)
    assert len(db_session.query(Journals).all()) == 1


def test_list_view_returns_dict(dummy_request):
    """Home view returns a dictionary of values."""
    from anna_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_count_matching_database(dummy_request):
    """Home view response matches database count."""
    from anna_journal.views.default import list_view
    response = list_view(dummy_request)
    query = dummy_request.db_session.query(Journals)
    assert len(response['journals']) == query.count()


@pytest.fixture
def add_models(dummy_request):
    """Add a bunch of model instances to the database.

    Every test that includes this fixture will add new random expenses.
    """
    dummy_request.db_session.add_all(JOUNRAL_LIST)


# @pytest.fixture
# def list_response():
#     """Return a response from the list page."""
#     from anna_journal.views.default import list_view
#     request = testing.DummyRequest()
#     response = list_view(request)
#     return response


# @pytest.fixture
# def detail_response():
#     """Return a response from the list page."""
#     from anna_journal.views.default import detail_view
#     request = testing.DummyRequest()
#     response = detail_view(request)
#     return response


# @pytest.fixture
# def create_response():
#     """Return a response from the list page."""
#     from anna_journal.views.default import create_view
#     request = testing.DummyRequest()
#     response = create_view(request)
#     return response


# @pytest.fixture
# def update_response():
#     """Return a response from the update page."""
#     from anna_journal.views.default import update_view
#     request = testing.DummyRequest()
#     response = update_view(request)
#     return response


# def test_list_view_returns_dict():
#     """List view respond."""
#     from anna_journal.views.default import list_view
#     request = testing.DummyRequest()
#     assert isinstance(list_response, dict)


# def test_list_view_status_ok(list_response):
#     """Show 200 status ok on list view."""
#     assert list_response.status_code == 200


# def test_list_view_returns_proper_content(list_response):
#     """Home view response has file content."""
#     with io.open(os.path.join(HERE, './templates/index.html')) as the_file:
#         imported_text = the_file.read()
#     assert imported_text in list_response.text


# def test_detail_view_returns_response(detail_response):
#     """detail view respond."""
#     assert isinstance(detail_response, dict)


# def test_detail_view_status_ok(detail_response):
#     """Show 200 status ok on detail view."""
#     assert detail_response.status_code == 200


# def test_detail_view_returns_proper_content(detail_response):
#     """Home view response has file content."""
#     with io.open(os.path.join(HERE, './templates/detail.html')) as the_file:
#         imported_text = the_file.read()
#     assert imported_text in detail_response.text


# def test_create_view_returns_response(create_response):
#     """create view respond."""
#     assert isinstance(create_response, dict)


# def test_create_view_status_ok(create_response):
#     """Show 200 status ok on create view."""
#     assert create_response.status_code == 200


# def test_create_view_returns_proper_content(create_response):
#     """Home view response has file content."""
#     with io.open(os.path.join(HERE, './templates/form.html')) as the_file:
#         imported_text = the_file.read()
#     assert imported_text in create_response.text


# def test_update_view_returns_response(update_response):
#     """update view respond."""
#     assert isinstance(update_response, dict)


# def test_update_view_status_ok(update_response):
#     """Show 200 status ok on update view."""
#     assert update_response.status_code == 200


# def test_update_view_returns_proper_content(update_response):
#     """Home view response has file content."""
#     with io.open(os.path.join(HERE, './templates/form_edit.html')) as the_file:
#         imported_text = the_file.read()
#     assert imported_text in update_response.text
