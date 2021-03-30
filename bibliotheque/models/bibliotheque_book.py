from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError

class book(models.Model):
	_name = 'bibliotheque.book'
	_description = 'book'
	_order = 'name, date_published desc'


	name = fields.Char('Title', required = True)
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

	#@api.multi
	#def button_check_isbn(self):
		#for book in self:
			#if not book.isbn:
	    		#raise Warning('Please provide an ISBN for %s' % book.name)
	    	#if book.isbn and not book._check_isbn():
	    		#raise Warning('%s is an invalid ISBN' % book.isbn)
	    #return True

	publisher_country_id = fields.Many2one('res.country', 
		string='Publisher Country',
		compute='_compute_publisher_country',
		inverse='_inverse_publisher_country',
		search='_search_publisher_country',)

	@api.depends('publisher_id.country_id')
	def _compute_publisher_country(self):
		for book in self:
			book.publisher_country_id = book.publisher_id.country_id


	def _inverse_publisher_country(self):
		for book in self:
			book.publisher_id.country_id = book.publisher_country_id

	def _search_publisher_country(self, operator, value):
		return [('publisher_id.country_id', operator, value)]


	_sql_constraints = [('library_book_name_date_uq',
		'UNIQUE (name, date_published)',
		'Book title and publication date must be unique.'),
		('library_book_check_date',
		'CHECK (date_published <= current_date)',
		'Publication date must not be in the future.'),
	]

	@api.constrains('isbn')
	def _constrain_isbn_valid(self):
		def _constrain_isbn_valid(self):
			for book in self:
				if book.isbn and not book._check_isbn():
					raise ValidationError('%s is an invalid ISBN' % book.isbn)


	
	    

	    		


