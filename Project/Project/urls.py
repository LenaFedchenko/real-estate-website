import home, publish, catalog


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
    rule="/edit/<int:id>", 
    view_func= home.edit, 
    methods=['GET', 'POST']
    )
home.home.add_url_rule(
    rule='/logout/', 
    view_func= home.logout, 
    methods=['GET', 'POST']
    )
home.home.add_url_rule(
    rule='/register/', 
    view_func= home.render_register, 
    methods=['GET', 'POST']
    )
home.home.add_url_rule(
    rule='/profile/', 
    view_func= home.render_profile, 
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
catalog.catalog.add_url_rule(
    rule="/catalog/",
    view_func= catalog.render_catalog,
    methods=['GET', 'POST']
)

catalog.catalog.add_url_rule(
    rule="/admin/",
    view_func= catalog.render_admin,
    methods=['GET', 'POST']
)
catalog.catalog.add_url_rule(
    rule="/delete/",
    view_func= catalog.delete_product
)
catalog.catalog.add_url_rule(
    rule="/catalog/<int:id>/",
    view_func= catalog.render_product_by_id,
    methods=['GET', 'POST']
)