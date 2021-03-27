# This file is part of commission_invoice_posted2draft module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import invoice

def register():
    Pool.register(
        invoice.Invoice,
        module='commission_invoice_posted2draft', type_='model')
