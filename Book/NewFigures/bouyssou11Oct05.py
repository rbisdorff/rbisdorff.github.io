# Saved digraph instance
from decimal import Decimal
from collections import OrderedDict
actions = OrderedDict([
('a',
{'shortName': 'a', 'name': 'random decision action'}),
('b',
{'shortName': 'b', 'name': 'random decision action'}),
('c',
{'shortName': 'c', 'name': 'random decision action'}),
('d',
{'shortName': 'd', 'name': 'random decision action'}),
])
valuationdomain = {'hasIntegerValuation': True, 'min': -1.0,'med': 0.0,'max': 1.0}
relation = {
'a': {
'a':0.0,
'b':1.0,
'c':1.0,
'd':-1.0,
},
'b': {
'a':-1.0,
'b':0.0,
'c':1.0,
'd':1.0,
},
'c': {
'a':-1.0,
'b':-1.0,
'c':0.0,
'd':1.0,
},
'd': {
'a':-1.0,
'b':-1.0,
'c':-1.0,
'd':0.0,
},

}
