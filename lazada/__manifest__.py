{
    'name': "Lazada",
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
        'views/lazada_order_views.xml',
        'views/lazada_menus.xml',
    ],
    # # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'views/traveler_views.xml',
    # ],
    'depends': [
        'sale',
    ],
    'license': 'LGPL-3',
}