
def get_data():
	return {
		'fieldname': 'prevdoc_docname',
		'non_standard_fieldnames': {
			'Payment Entry': 'cheque_',
		},
		'transactions': [
			{
				'items': ['Payment Entry']
			},
		]
	}
