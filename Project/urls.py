import home, publish


home.home.add_url_rule(
    rule= '/',
    view_func= home.render_home,
    methods=['GET', 'POST']
)
publish.publish.add_url_rule(
    rule= '/publish',
    view_func= publish.render_publish,
    methods=['GET', 'POST']
)