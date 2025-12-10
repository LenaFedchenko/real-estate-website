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
home.home.add_url_rule(
    rule='/register/', 
    view_func= home.render_register, 
    methods=['GET', 'POST']
    )
home.home.add_url_rule(
    rule='/login/', 
    view_func= home.render_login, 
    methods=['GET', 'POST']
    )
home.home.add_url_rule(
    rule= "/verify/",
    view_func= home.verify_code,
    methods=['GET', 'POST']
)