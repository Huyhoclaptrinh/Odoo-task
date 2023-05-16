{
    'name': "Fashion",
    'version': '1.0',
    'depends': ['base'],
    'author': "Huy",
    'category': '',
    'description': """
    Description text
    """,
    # # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/fashion_customer_menus.xml',
        'views/fashion_customer_views.xml',
    ],
    # # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'views/traveler_views.xml',
    # ],
    'license': 'LGPL-3',
}