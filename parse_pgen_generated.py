import pgen_runtime

actions = [{'nt': 1},
 {'IDENT': 4},
 {None: -9223372036854775807, 'nt': 1},
 {None: -1, 'nt': -1},
 {'{': 6},
 {None: -2, 'nt': -2},
 {'IDENT': 7, 'STR': 8, '}': 9},
 {';': -12, '?': -12, 'IDENT': -12, 'STR': -12},
 {';': -13, '?': -13, 'IDENT': -13, 'STR': -13},
 {None: -3, 'nt': -3},
 {';': -8, 'IDENT': -8, 'STR': -8},
 {';': -10, '?': 15, 'IDENT': -10, 'STR': -10},
 {';': 16, 'IDENT': 7, 'STR': 8},
 {'IDENT': -5, 'STR': -5, '}': -5},
 {'IDENT': 7, 'STR': 8, '}': 18},
 {';': -11, 'IDENT': -11, 'STR': -11},
 {'IDENT': -7, 'STR': -7, '}': -7},
 {';': -9, 'IDENT': -9, 'STR': -9},
 {None: -4, 'nt': -4},
 {'IDENT': -6, 'STR': -6, '}': -6}]

ctns = [{'grammar': 2, 'nt_def': 3},
 {},
 {'nt_def': 5},
 {},
 {},
 {},
 {'prod': 13, 'prods': 14, 'symbol': 11, 'term': 10, 'terms': 12},
 {},
 {},
 {},
 {},
 {},
 {'symbol': 11, 'term': 17},
 {},
 {'prod': 19, 'symbol': 11, 'term': 10, 'terms': 12},
 {},
 {},
 {},
 {},
 {}]

reductions = [
    ('grammar', 1, lambda x0: ('grammar', 0, [x0])),
    ('grammar', 2, lambda x0, x1: ('grammar', 1, [x0, x1])),
    ('nt_def', 4, lambda x0, x1, x2, x3: ('nt_def', 0, [x0, x1, x2, None, x3])),
    ('nt_def', 5, lambda x0, x1, x2, x3, x4: ('nt_def', 0, [x0, x1, x2, x3, x4])),
    ('prods', 1, lambda x0: ('prods', 0, [x0])),
    ('prods', 2, lambda x0, x1: ('prods', 1, [x0, x1])),
    ('prod', 2, lambda x0, x1: ('prod', 0, [x0, x1])),
    ('terms', 1, lambda x0: ('terms', 0, [x0])),
    ('terms', 2, lambda x0, x1: ('terms', 1, [x0, x1])),
    ('term', 1, lambda x0: ('term', 0, [x0])),
    ('term', 2, lambda x0, x1: ('term', 1, [x0, x1])),
    ('symbol', 1, lambda x0: ('symbol', 0, [x0])),
    ('symbol', 1, lambda x0: ('symbol', 1, [x0])),
    ('grammar_1', 1, lambda x0: ('grammar_1', 0, [x0])),
]

parse = pgen_runtime.make_parse_fn(actions, ctns, reductions, 0)