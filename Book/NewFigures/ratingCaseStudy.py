# Saved performance Tableau: 
from decimal import Decimal
from collections import OrderedDict
actions = OrderedDict([
('u1', {
'shortName': 'U1',
'name': 'U1, TU',
'comment': 'Technical University',
'rank': 32,
}),
('u2', {
'shortName': 'U2',
'name': 'U2, TU',
'comment': 'Technical University',
'rank': 32,
}),
('u3', {
'shortName': 'U3',
'name': 'U3, U',
'comment': 'University',
'rank': 40,
}),
('u4', {
'shortName': 'U4',
'name': 'U4, TH',
'comment': 'Higher Technical School',
'rank': 29,
}),
('u5', {
'shortName': 'U5',
'name': 'U5, U',
'comment': 'University',
'rank': 7,
}),
])
objectives = OrderedDict([
('HUM', {
'name': 'Humanities',
'criteria': ['germ', 'pol', 'psy', 'soc'],
'weight': Decimal('4.0'),
}),
('LEM', {
'name': 'Law, Economics & Management',
'criteria': ['law', 'eco', 'mgt'],
'weight': Decimal('3.0'),
}),
('LSM', {
'name': 'Life Sciences & Medicine',
'criteria': ['bio', 'med'],
'weight': Decimal('2.0'),
}),
('SCI', {
'name': 'Technology',
'criteria': ['info', 'elec', 'mec'],
'weight': Decimal('3.0'),
}),
])
criteria = OrderedDict([
('germ', {
'shortName': 'germ',
'name': 'German Studies',
'comment': 'Humanities',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('pol', {
'shortName': 'pol',
'name': 'Politology',
'comment': 'Humanities',
'weight': Decimal('1.0'),
'scale': (50.0, 70.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('psy', {
'shortName': 'psy',
'name': 'Psychology',
'comment': 'Humanities',
'weight': Decimal('1.0'),
'scale': (50.0, 70.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('soc', {
'shortName': 'soc',
'name': 'Sociology',
'comment': 'Humanities',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('law', {
'shortName': 'law',
'name': 'Law Studies',
'comment': 'Law, Economics & Management',
'weight': Decimal('1.0'),
'scale': (35.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('eco', {
'shortName': 'eco',
'name': 'Economics',
'comment': 'Law, Economics & Management',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('mgt', {
'shortName': 'mgt',
'name': 'Management',
'comment': 'Law, Economics & Management',
'weight': Decimal('1.0'),
'scale': (40.0, 80.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('bio', {
'shortName': 'bio',
'name': 'Life Sciences',
'comment': 'Life Sciences & Medicine',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('med', {
'shortName': 'med',
'name': 'Medicine',
'comment': 'Life Sciences & Medicine',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('phys', {
'shortName': 'phys',
'name': 'Physics',
'comment': 'Natural Sciences & Mathematics',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('chem', {
'shortName': 'chem',
'name': 'Chemistry',
'comment': 'Natural Sciences & Mathematics',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('math', {
'shortName': 'math',
'name': 'Mathematics',
'comment': 'Natural Sciences & Mathematics',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('info', {
'shortName': 'info',
'name': 'Computer Science',
'comment': 'Technology',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('elec', {
'shortName': 'elec',
'name': 'Electrical Engineering',
'comment': 'Technology',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
('mec', {
'shortName': 'mec',
'name': 'Mechanical Engineering',
'comment': 'Technology',
'weight': Decimal('1.0'),
'scale': (45.0, 65.0),
'preferenceDirection': 'max',
'thresholds': {'ind': (Decimal('0.1'), Decimal('0.0')), 'pref': (Decimal('0.5'), Decimal('0.0'))},
}),
])
NA = Decimal('-999')
evaluation = {
'germ': {
'u1':Decimal("51.40"),
'u2':Decimal("53.50"),
'u3':Decimal("51.40"),
'u4':Decimal("53.30"),
'u5':Decimal("61.40"),
},
'pol': {
'u1':Decimal("-999.00"),
'u2':Decimal("54.00"),
'u3':Decimal("-999.00"),
'u4':Decimal("50.80"),
'u5':Decimal("59.50"),
},
'psy': {
'u1':Decimal("57.70"),
'u2':Decimal("-999.00"),
'u3':Decimal("54.40"),
'u4':Decimal("62.70"),
'u5':Decimal("59.80"),
},
'soc': {
'u1':Decimal("59.10"),
'u2':Decimal("51.50"),
'u3':Decimal("55.60"),
'u4':Decimal("51.00"),
'u5':Decimal("52.20"),
},
'law': {
'u1':Decimal("-999.00"),
'u2':Decimal("-999.00"),
'u3':Decimal("41.90"),
'u4':Decimal("-999.00"),
'u5':Decimal("51.10"),
},
'eco': {
'u1':Decimal("49.60"),
'u2':Decimal("-999.00"),
'u3':Decimal("-999.00"),
'u4':Decimal("-999.00"),
'u5':Decimal("54.40"),
},
'mgt': {
'u1':Decimal("54.00"),
'u2':Decimal("53.40"),
'u3':Decimal("50.70"),
'u4':Decimal("49.60"),
'u5':Decimal("-999.00"),
},
'bio': {
'u1':Decimal("-999.00"),
'u2':Decimal("53.10"),
'u3':Decimal("49.70"),
'u4':Decimal("52.20"),
'u5':Decimal("55.20"),
},
'med': {
'u1':Decimal("-999.00"),
'u2':Decimal("-999.00"),
'u3':Decimal("-999.00"),
'u4':Decimal("49.50"),
'u5':Decimal("55.50"),
},
'phys': {
'u1':Decimal("58.90"),
'u2':Decimal("59.80"),
'u3':Decimal("53.90"),
'u4':Decimal("59.10"),
'u5':Decimal("60.90"),
},
'chem': {
'u1':Decimal("52.00"),
'u2':Decimal("50.10"),
'u3':Decimal("54.20"),
'u4':Decimal("53.60"),
'u5':Decimal("56.70"),
},
'math': {
'u1':Decimal("56.80"),
'u2':Decimal("54.70"),
'u3':Decimal("56.30"),
'u4':Decimal("58.60"),
'u5':Decimal("61.30"),
},
'info': {
'u1':Decimal("55.40"),
'u2':Decimal("52.60"),
'u3':Decimal("55.80"),
'u4':Decimal("54.60"),
'u5':Decimal("-999.00"),
},
'elec': {
'u1':Decimal("56.10"),
'u2':Decimal("54.50"),
'u3':Decimal("-999.00"),
'u4':Decimal("57.20"),
'u5':Decimal("-999.00"),
},
'mec': {
'u1':Decimal("54.30"),
'u2':Decimal("55.20"),
'u3':Decimal("-999.00"),
'u4':Decimal("54.40"),
'u5':Decimal("-999.00"),
},
}