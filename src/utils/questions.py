def ask(question, yes='y', no='n', default='yes'):
	res = 'none'
	y = yes.lower() if default == 'no' else yes.upper()
	n = no.lower() if default == 'yes' else no.upper()
	while res.lower() not in [yes, no, '']:
		res = input(f'{question} [{y}|{n}]: ')
	if not res:
		res = yes if default == 'yes' else no
	return res.lower() == yes.lower()


def ask_string(question, nullable=False):
	res = None
	while not res and not nullable:
		res = input(f'? {question}: ')
	return res


def ask_list(question, nullable=False):
	res = []
	r = None
	while r or not res:
		r = input(f'? {question}: ')
		if r:
			res.append(r)
		elif nullable:
			break
	return res


def ask_choice(question, choices):
	if not choices:
		return None
	res = ''
	clist = '[' + ', '.join(choices) + ']'
	while not res.lower() in choices:
		res = input(f'? {question} {clist.lower()}: ')
	return res


def ask_list_choices(question, choices, nullable=False):
	res = []
	if not choices:
		return res
	clist = '[' + ', '.join(choices) + ']'
	while not res:
		r = input(f'? {question} {clist}: ')
		if r and r in choices:
			res.append(r)
		elif not r and nullable:
			break
	return res