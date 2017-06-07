def includeme(config):
    config.add_static_view(
        'static',
        'anna_journal:static',
        cache_max_age=3600
    )
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/form')
    config.add_route('update_view', '/journal/{id:\d+}/form_edit')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('security', '/journal/security')
