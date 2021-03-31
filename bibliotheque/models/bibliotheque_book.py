from odoo import api, fields, models
from odoo.exceptions import ValidationError

class book(models.Model):
	_name = 'bibliotheque.book'
	_description = 'book'
	_order = 'name, date_published desc'


	name = fields.Char('Title')	
	isbn = fields.Char('ISBN')
	book_type = fields.Selection(
		[('paper','Paperback'),
		('hard','Hardcover'),
		('electronic','Electronic'),
		('other', 'Other')],
		'Type')
	notes = fields.Text('Internal Notes')
	descr = fields.Html('Description')
	copies = fields.Integer(default=1)
	avg_rating = fields.Float('Average Rating', (3, 2))
	price = fields.Monetary('Price', 'currency_id')
	currency_id = fields.Many2one('res.currency')
	date_published = fields.Date()
	last_borrow_date = fields.Datetime(
		'Last Borrowed On',
		default=lambda self: fields.Datetime.now())
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


	
	    

	    		


