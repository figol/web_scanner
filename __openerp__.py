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

{
	"name" : 'Scanner',
	"version" : '0.1',
	"author" : 'figol',
	"website" : 'figo.github.io',
	"summary" : 'easy scanner',
	"description" : 'scan sales order!',
	"depends" : ['web', 'sale'],
	"data" : [
		'scanner_menu_view.xml',
	],
	"js": [
		'static/src/js/*.js',
	],
	"css": [
		'static/src/css/*.css',
	],
	"qweb": ['static/src/xml/*.xml'],
	"installable" : True,
}
