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
        'security/fashion_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/fashion_customer_views.xml',
        'views/fashion_product_views.xml',
        'views/fashion_customer_menus.xml',
    ],
    # # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'views/traveler_views.xml',
    # ],
    'depends': [
      'base_setup',
      'mail',
    ],
    'license': 'LGPL-3',
}