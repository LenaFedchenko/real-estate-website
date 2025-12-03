import home


home.home.add_url_rule(
    rule= '/',
    view_func= home.render_home,
    methods=['GET', 'POST']
)
