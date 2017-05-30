"""Init."""
from .default import list_view
from .default import detail_view
from .default import create_view
from .default import update_view


def includeme(config):
    """Viewing include."""
    config.add_view(list_view, route_name="list_view")
    config.add_view(detail_view, route_name="detail_view")
    config.add_view(create_view, route_name="create_view")
    config.add_view(update_view, route_name="update_view")
