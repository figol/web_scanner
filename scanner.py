# -*- coding: utf-8 -*-
##############################################################################
#
#    Scanner Module for openerp 7.0
#    Copyright 2014 figol <figolliu@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = "sale.order"

    def get_order_detail(self, cr, uid, name):
        res = {
	    'state': True,
            'order': {},
            'order_lines': [],
	    'msg': ''
        }
	order_ids = self.search(cr, uid, [('name', '=', name)])
	if not order_ids:
	    res['state'] = False
	    res['msg'] = 'No order found.'
            return res
    	res['order'] = self.read(cr, uid, order_ids[0], ['partner_id', 'name', 'shop_id', 'date_order', 'order_line'])
	if res['order'].get('order_line'):
	    order_line_obj = self.pool.get('sale.order.line')
	    res['order_lines'] = order_line_obj.read(cr, uid, res['order']['order_line'], ['product_id', 'product_uom_qty', 'price_unit'])
	return res

sale_order()
