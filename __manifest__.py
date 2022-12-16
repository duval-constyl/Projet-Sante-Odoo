# -*- coding: utf-8 -*-
{
    'name': "HOPITAL BYC",  # Module title
    'summary': "Gestion d'une clinic",  # Module subtitle phrase
    'description': """
Ce module doit pouvoir gerer 
==============
les patients, personnels, pharmacies, inventaires, comptes, facture, chambres et les consultations.
    """,  # Supports reStructuredText(RST) format
    'author': "BYCTEAM",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base',
                'mail'],
    # This data files will be loaded at the installation (commented because file is not added in this example)
    'data': [
        'security/ir.model.access.csv',
        'views/clinic_patient.xml',
        'views/clinic_personnel.xml',
        'views/clinic_chambre.xml',
        'views/clinic_chirurgie.xml',
        'views/clinic_compte.xml',
        'views/clinic_consultation.xml',
        'views/clinic_pharmacie.xml',
        'views/clinic_inventaire.xml',
        'views/clinic_factures.xml'
     ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],

    'installable': True,
    'images': "icon.png",
    'application': True,
    'license': "LGPL-3",
    'sequence': -100
}
