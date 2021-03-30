from odoo import api, fields, models
from odoo.exceptions import Warning

class book(models.Model):
	_name = 'bibliotheque.book'
	_description = 'book'
	_order = 'name, date_published desc'


	name = fields.Char('Title', required = True)
	isbn = fields.Char('ISBN')
	#notes = fields.Text('Internal Notes')
    #descr = fields.Html('Description')
    #copies = fields.Integer(default=1)
    #avg_rating = fields.Float('Average Rating', (3, 2))
    #price = fields.Monetary('Price', 'currency_id')
    #currency_id = fields.Many2one('res.currency')
	date_published = fields.Date()
	active = fields.Boolean('Active?', default = True)
	image = fields.Binary('Cover')

	publisher_id = fields.Many2one('res.partner',string='Publisher')
	author_ids = fields.Many2many('res.partner',string='Authors')

	@api.multi
	def _check_isbn(self):
		self.ensure_one()
		digits = [int(x) for x in self.isbn if x.isdigit()]
		if len(digits) == 13:
			product = (sum(int(ch) for ch in digits[::2])
				+ sum(int(ch)*3 for ch in digits[1::2]))
			return product % 10 == 0

	#@api.multi
	#def button_check_isbn(self):
		#for book in self:
			#if not book.isbn:
	    		#raise Warning('Please provide an ISBN for %s' % book.name)
	    	#if book.isbn and not book._check_isbn():
	    		#raise Warning('%s is an invalid ISBN' % book.isbn)
	    #return True
	    

	    		


