# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Multiple Branchs/Units Operations for Manufacturing',
    'version': '1.0',
    'category' : 'Manufacturing',
    'depends': [
        'mrp',
        'odoo_multi_branch',
    ],
    'license': 'Other proprietary',
    'price': 10.0,
    'currency': 'EUR',
    'summary': """This app allow you to manage Odoo operations with Multiple Branches/Units setup for Manufacturing App""",
    'description': """
    - Added Branch in Manufacturing order
    - Set Branch to the Bill of material it will be set default user's branch
    - Branch will be passed to the Manufacturing Order from the Bill of Material
    - Pass Branch to the Workorder from the Manufacturing Order when create workorder.
    - After Done The Workorder It will be passed Branch on Finished Product.

Branch on BOM
Branch On MRP
Branch on WorkOrder
Branch on Manufacturing Orders
Branch on Applicant,
Branch on Employee,
Branch on Department,
Branch on Attendance,
Branch on Payslip
Branch on Contract,
Branch on Expense and Expense Sheet
Branch on Holidays
Passed Branch on Applicant to Employee,
Passed Branch on Expense to Expense Sheet
branch
multi branch
multi unit
branch operation
Unit operation
Multiple Branch  Management Module for single company
Multiple  Unit  Management Module for single company

different branch
Add multiple unit
Add multiple branch
branch manager
Branch wise Financial Statement
unit wise Financial Statement
odoo branch
odoo unit
odoo branch operation
res.branch
branch odoo
unit odoo
cost center odoo
Branch On Sales
Branch on Picking 
Branch on Delivery Order
Branch On Invoices
Branch On Purchase
Branch On Warehouse
Branch on Session
Branch on pos
pos branch
pos multi branch
point of sale multi branch
Branch on POS order
Branch on pos Receipt
Branch on Receipt
Branch on Payment
Branch Wise Accounting Report
Trial Balance Report
Partner Ledger Report
probuse
branch setup
branch configuration
branch configure
odoo multi branch
company branch
branch company
odoo by branch


Branch office
outlet of a company
company outlet
organization
branch organization
subsidiary 
company subsidiary 
branch subsidiary 
legal entity
main office
Branching
financial institutions
Branches are a part of the parent organization, which are opened to perform the same business operations as performed by the parent company, to increase their reach.
Head office
parent company
branch location
store location


    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'http://www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpg'],
    'live_test_url': 'https://youtu.be/IkdfT8_6oJI',

    'data':[
        'security/security.xml',
        'report/mrp_production_report_view.xml',
        'views/mrp_bom_view.xml',
        'views/mrp_production_view.xml',
        'views/mrp_workorder_view.xml',
        'views/stock_move_line.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
