# Saved digraph instance
from decimal import Decimal
from collections import OrderedDict
actions = OrderedDict([
('a1',
{'shortName': 'a1', 'name': 'random decision action'}),
('a2',
{'shortName': 'a2', 'name': 'random decision action'}),
('a3',
{'shortName': 'a3', 'name': 'random decision action'}),
('a4',
{'shortName': 'a4', 'name': 'random decision action'}),
('a5',
{'shortName': 'a5', 'name': 'random decision action'}),
])
valuationdomain = {'hasIntegerValuation': True, 'min': -1.0,'med': 0.0,'max': 1.0}
relation = {
'a1': {
'a1':-1.0,
'a2':-1.0,
'a3':1.0,
'a4':-1.0,
'a5':-1.0,
},
'a2': {
'a1':1.0,
'a2':-1.0,
'a3':-1.0,
'a4':1.0,
'a5':1.0,
},
'a3': {
'a1':1.0,
'a2':-1.0,
'a3':-1.0,
'a4':1.0,
'a5':-1.0,
},
'a4': {
'a1':1.0,
'a2':1.0,
'a3':1.0,
'a4':-1.0,
'a5':-1.0,
},
'a5': {
'a1':1.0,
'a2':1.0,
'a3':1.0,
'a4':-1.0,
'a5':-1.0,
},
}
