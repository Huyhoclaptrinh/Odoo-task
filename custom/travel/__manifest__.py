{
    'name': "Travel",
    'version': '1.0',
    'depends': ['base'],
    'author': "Huy",
    'category': 'Tour',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        # 'security/riccha.csv',
        'security/travel_security.xml',
        'views/travel_menu.xml'
    ],
    # # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'views/traveler_views.xml',
    # ],
    'license': 'LGPL-3',
}