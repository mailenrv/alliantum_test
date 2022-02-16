##############################################################################
#
#    OpenERP, Open Source Management Solution
#
##############################################################################

{
    'name': 'Alliantum Test',
    'version': '14.0.1.0.0',
    'author': 'Máilen Rojas',
    'maintainer': 'Máilen Rojas',
    'category': 'Sales',
    'summary': 'This module gives extra details to products marked as Burgers',
    'depends': ['sale_management'],
    'data': [
        #'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    'images': ['static/description/icon.png'],
}
