################################
# Digraph3 Tutorials
# R. Bisdorff 2020
# Url: https://www.spiegel.de/thema/studentenspiegel/
# Ref: Der Spiegel 48/2004 p.181
#######################################
from decimal import Decimal
from collections import OrderedDict
actions = OrderedDict([
('aa', {
'shortName': 'aa',
'name': 'Aa TH',
'comment': 'Higher Technical School',
'rank': 29,
}),
('ab', {
'shortName': 'ab',
'name': 'ab, U',
'comment': 'University',
'rank': 19,
}),
('ac', {
'shortName': 'ac',
'name': 'ac, U',
'comment': 'University',
'rank': 16,
}),
('ad', {
'shortName': 'ad',
'name': 'ad, U',
'comment': 'University',
'rank': 4,
}),
('ae', {
'shortName': 'ae',
'name': 'ae, TU',
'comment': 'Technical University',
'rank': 32,
}),
('af', {
'shortName': 'af',
'name': 'af, U',
'comment': 'University',
'rank': 40,
}),
('ag', {
'shortName': 'ag',
'name': 'ag, U',
'comment': 'University',
'rank': 36,
}),
('ah', {
'shortName': 'ah',
'name': 'ah, U',
'comment': 'University',
'rank': 16,
}),
('ai', {
'shortName': 'ai',
'name': 'ai, TU',
'comment': 'Technical University',
'rank': 32,
}),
('aj', {
'shortName': 'aj',
'name': 'aj, U',
'comment': 'University',
'rank': 36,
}),
('ak', {
'shortName': 'ak',
'name': 'ak, TU',
'comment': 'Technical University',
'rank': 23,
}),
('al', {
'shortName': 'al',
'name': 'al, U',
'comment': 'University',
'rank': 16,
}),
('am', {
'shortName': 'am',
'name': 'am, TU',
'comment': 'University',
'rank': 16,
}),
('an', {
'shortName': 'an',
'name': 'an, U',
'comment': 'University',
'rank': 36,
}),
('ao', {
'shortName': 'ao',
'name': 'ao, U',
'comment': 'University',
'rank': 41,
}),
('ap', {
'shortName': 'ap',
'name': 'ap, U',
'comment': 'University',
'rank': 24,
}),
('aq', {
'shortName': 'aq',
'name': 'aq, U',
'comment': 'University',
'rank': 32,
}),
('ar', {
'shortName': 'ar',
'name': 'ar, U',
'comment': 'University',
'rank': 2,
}),
('as', {
'shortName': 'as',
'name': 'as, U',
'comment': 'University',
'rank': 36,
}),
('at', {
'shortName': 'at',
'name': 'at, U',
'comment': 'University',
'rank': 25,
}),
('au', {
'shortName': 'au',
'name': 'au, U',
'comment': 'University',
'rank': 32,
}),
('av', {
'shortName': 'av',
'name': 'av, U',
'comment': 'University',
'rank': 36,
}),
('aw', {
'shortName': 'aw',
'name': 'aw, U',
'comment': 'University',
'rank': 7,
}),
('ax', {
'shortName': 'ax',
'name': 'ax, U',
'comment': 'University',
'rank': 14,
}),
('ay', {
'shortName': 'ay',
'name': 'ay, U',
'comment': 'University',
'rank': 29,
}),
('az', {
'shortName': 'az',
'name': 'bp, U',
'comment': 'University',
'rank': 12,
}),
('ba', {
'shortName': 'ba',
'name': 'ba, U',
'comment': 'University',
'rank': 25,
}),
('bb', {
'shortName': 'bb',
'name': 'bb, U',
'comment': 'University',
'rank': 4,
}),
('bc', {
'shortName': 'bc',
'name': 'bc, U',
'comment': 'University',
'rank': 12,
}),
('bd', {
'shortName': 'bd',
'name': 'bd, U',
'comment': 'University',
'rank': 3,
}),
('be', {
'shortName': 'be',
'name': 'be, U',
'comment': 'University',
'rank': 25,
}),
('bf', {
'shortName': 'bf',
'name': 'bf, U',
'comment': 'University',
'rank': 16,
}),
('bg', {
'shortName': 'bg',
'name': 'bg, U',
'comment': 'University',
'rank': 10,
}),
('bh', {
'shortName': 'bh',
'name': 'bh, U',
'comment': 'University',
'rank': 14,
}),
('bi', {
'shortName': 'bi',
'name': 'bi, U',
'comment': 'University',
'rank': 4,
}),
('bj', {
'shortName': 'bj',
'name': 'bj, U',
'comment': 'University',
'rank': 16,
}),
('bk', {
'shortName': 'bk',
'name': 'bk, U',
'comment': 'University',
'rank': 16,
}),
('bl', {
'shortName': 'bl',
'name': 'bl, U',
'comment': 'University',
'rank': 7,
}),
('bm', {
'shortName': 'bm',
'name': 'bm, U',
'comment': 'University',
'rank': 25,
}),
('bn', {
'shortName': 'bn',
'name': 'bn, U',
'comment': 'University',
'rank': 7,
}),
('bo', {
'shortName': 'bo',
'name': 'bo, TU',
'comment': 'Technical University',
'rank': 1,
}),
])
objectives = OrderedDict([
    ('HUM', {'name':'Humanities',
             'criteria': ['germ','pol','psy','soc'],
             'weight':4.0}),
    ('LEM', {'name':'Law, Economics & Management',
             'criteria': ['law','eco','mgt'],
             'weight':3.0}),
    ('LSM', {'name':'Life Sciences & Medicine',
             'criteria': ['bio','med'],
             'weight':2.0}),
    ('SCI', {'name':'Natural Sciences & Mathematics',
             'criteria': ['phys','chem','math'],
             'weight':3.0}),  
    ('SCI', {'name':'Technology',
             'criteria': ['info','elec','mec'],
             'weight':3.0}),  
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
NA = Decimal('-999.00')
evaluation = {
'mgt': {
'aa':Decimal("49.6"),
'ab':Decimal("54.3"),
'ac':Decimal("52.2"),
'ad':Decimal("55.5"),
'ae':Decimal("54.0"),
'af':Decimal("50.7"),
'ag':Decimal("-999.00"),
'ah':Decimal("-999.00"),
'ai':Decimal("53.4"),
'aj':Decimal("55.4"),
'ak':Decimal("52.7"),
'al':Decimal("-999.00"),
'am':Decimal("54.8"),
'an':Decimal("50.5"),
'ao':Decimal("47.5"),
'ap':Decimal("55.6"),
'aq':Decimal("52.0"),
'ar':Decimal("-999.00"),
'as':Decimal("51.2"),
'at':Decimal("52.6"),
'au':Decimal("49.8"),
'av':Decimal("-999.00"),
'aw':Decimal("-999.00"),
'ax':Decimal("56.2"),
'ay':Decimal("52.8"),
'ba':Decimal("54.6"),
'bb':Decimal("-999.00"),
'bc':Decimal("55.9"),
'bd':Decimal("54.6"),
'be':Decimal("53.1"),
'bf':Decimal("55.5"),
'bg':Decimal("59.7"),
'bh':Decimal("56.3"),
'bi':Decimal("57.5"),
'bj':Decimal("55.5"),
'bk':Decimal("52.2"),
'bl':Decimal("56.6"),
'bm':Decimal("52.8"),
'bn':Decimal("54.4"),
'bo':Decimal("68.0"),
'az':Decimal("52.8"),
},
'bio': {
'aa':Decimal("52.2"),
'ab':Decimal("-999.00"),
'ac':Decimal("51.6"),
'ad':Decimal("55.0"),
'ae':Decimal("-999.00"),
'af':Decimal("49.7"),
'ag':Decimal("48.0"),
'ah':Decimal("50.1"),
'ai':Decimal("53.1"),
'aj':Decimal("53.3"),
'ak':Decimal("-999.00"),
'al':Decimal("1.00"),
'am':Decimal("55.3"),
'an':Decimal("47.3"),
'ao':Decimal("-999.00"),
'ap':Decimal("51.8"),
'aq':Decimal("51.3"),
'ar':Decimal("55.4"),
'as':Decimal("50.4"),
'at':Decimal("50.5"),
'au':Decimal("52.7"),
'av':Decimal("53.8"),
'aw':Decimal("55.2"),
'ax':Decimal("52.7"),
'ay':Decimal("52.7"),
'ba':Decimal("51.8"),
'bb':Decimal("55.7"),
'bc':Decimal("50.8"),
'bd':Decimal("56.9"),
'be':Decimal("50.0"),
'bf':Decimal("53.2"),
'bg':Decimal("-999.00"),
'bh':Decimal("51.2"),
'bi':Decimal("50.4"),
'bj':Decimal("54.6"),
'bk':Decimal("-999.00"),
'bl':Decimal("57.1"),
'bm':Decimal("-999.00"),
'bn':Decimal("53.7"),
'bo':Decimal("53.6"),
'az':Decimal("53.0"),
},
'chem': {
'aa':Decimal("53.6"),
'ab':Decimal("-999.00"),
'ac':Decimal("57.4"),
'ad':Decimal("53.2"),
'ae':Decimal("52.0"),
'af':Decimal("54.2"),
'ag':Decimal("53.3"),
'ah':Decimal("53.1"),
'ai':Decimal("50.1"),
'aj':Decimal("-999.00"),
'ak':Decimal("-999.00"),
'al':Decimal("2.00"),
'am':Decimal("55.8"),
'an':Decimal("53.5"),
'ao':Decimal("52.8"),
'ap':Decimal("54.0"),
'aq':Decimal("55.5"),
'ar':Decimal("57.0"),
'as':Decimal("-999.00"),
'at':Decimal("53.9"),
'au':Decimal("54.2"),
'av':Decimal("53.6"),
'aw':Decimal("56.7"),
'ax':Decimal("57.8"),
'ay':Decimal("52.8"),
'ba':Decimal("54.0"),
'bb':Decimal("58.0"),
'bc':Decimal("54.6"),
'bd':Decimal("57.0"),
'be':Decimal("56.3"),
'bf':Decimal("57.8"),
'bg':Decimal("-999.00"),
'bh':Decimal("55.0"),
'bi':Decimal("58.1"),
'bj':Decimal("55.8"),
'bk':Decimal("56.2"),
'bl':Decimal("55.2"),
'bm':Decimal("-999.00"),
'bn':Decimal("57.5"),
'bo':Decimal("58.8"),
'az':Decimal("56.6"),
},
'elec': {
'aa':Decimal("57.2"),
'ab':Decimal("-999.00"),
'ac':Decimal("-999.00"),
'ad':Decimal("-999.00"),
'ae':Decimal("56.1"),
'af':Decimal("-999.00"),
'ag':Decimal("54.2"),
'ah':Decimal("-999.00"),
'ai':Decimal("54.5"),
'aj':Decimal("50.1"),
'ak':Decimal("57.5"),
'al':Decimal("-999.00"),
'am':Decimal("56.1"),
'an':Decimal("-999.00"),
'ao':Decimal("53.6"),
'ap':Decimal("55.9"),
'aq':Decimal("-999.00"),
'ar':Decimal("-999.00"),
'as':Decimal("-999.00"),
'at':Decimal("-999.00"),
'au':Decimal("-999.00"),
'av':Decimal("53.5"),
'aw':Decimal("-999.00"),
'ax':Decimal("-999.00"),
'ay':Decimal("54.2"),
'ba':Decimal("-999.00"),
'bb':Decimal("-999.00"),
'bc':Decimal("57.5"),
'bd':Decimal("-999.00"),
'be':Decimal("-999.00"),
'bf':Decimal("-999.00"),
'bg':Decimal("-999.00"),
'bh':Decimal("-999.00"),
'bi':Decimal("-999.00"),
'bj':Decimal("-999.00"),
'bk':Decimal("-999.00"),
'bl':Decimal("60.2"),
'bm':Decimal("-999.00"),
'bn':Decimal("-999.00"),
'bo':Decimal("58.2"),
'az':Decimal("-999.00"),
},
'germ': {
'aa':Decimal("53.3"),
'ab':Decimal("57.9"),
'ac':Decimal("54.7"),
'ad':Decimal("57.3"),
'ae':Decimal("51.4"),
'af':Decimal("51.4"),
'ag':Decimal("53.9"),
'ah':Decimal("54.1"),
'ai':Decimal("53.5"),
'aj':Decimal("56.9"),
'ak':Decimal("54.3"),
'al':Decimal("1.00"),
'am':Decimal("55.2"),
'an':Decimal("53.5"),
'ao':Decimal("50.6"),
'ap':Decimal("57.9"),
'aq':Decimal("51.7"),
'ar':Decimal("57.8"),
'as':Decimal("53.0"),
'at':Decimal("58.7"),
'au':Decimal("57.0"),
'av':Decimal("50.4"),
'aw':Decimal("61.4"),
'ax':Decimal("56.5"),
'ay':Decimal("51.9"),
'ba':Decimal("51.7"),
'bb':Decimal("56.9"),
'bc':Decimal("-999.00"),
'bd':Decimal("57.4"),
'be':Decimal("54.2"),
'bf':Decimal("53.6"),
'bg':Decimal("52.2"),
'bh':Decimal("55.4"),
'bi':Decimal("57.2"),
'bj':Decimal("54.8"),
'bk':Decimal("57.9"),
'bl':Decimal("52.5"),
'bm':Decimal("54.1"),
'bn':Decimal("57.9"),
'bo':Decimal("-999.00"),
'az':Decimal("56.9"),
},
'info': {
'aa':Decimal("54.6"),
'ab':Decimal("58.1"),
'ac':Decimal("54.9"),
'ad':Decimal("55.8"),
'ae':Decimal("55.4"),
'af':Decimal("55.8"),
'ag':Decimal("-999.00"),
'ah':Decimal("53.7"),
'ai':Decimal("52.6"),
'aj':Decimal("54.1"),
'ak':Decimal("57.7"),
'al':Decimal("3.00"),
'am':Decimal("56.2"),
'an':Decimal("-999.00"),
'ao':Decimal("56.8"),
'ap':Decimal("54.6"),
'aq':Decimal("52.4"),
'ar':Decimal("58.1"),
'as':Decimal("-999.00"),
'at':Decimal("-999.00"),
'au':Decimal("54.7"),
'av':Decimal("58.8"),
'aw':Decimal("-999.00"),
'ax':Decimal("57.2"),
'ay':Decimal("54.9"),
'ba':Decimal("-999.00"),
'bb':Decimal("59.7"),
'bc':Decimal("56.2"),
'bd':Decimal("3.00"),
'be':Decimal("-999.00"),
'bf':Decimal("55.6"),
'bg':Decimal("58.6"),
'bh':Decimal("57.7"),
'bi':Decimal("57.1"),
'bj':Decimal("-999.00"),
'bk':Decimal("57.6"),
'bl':Decimal("59.8"),
'bm':Decimal("52.3"),
'bn':Decimal("55.2"),
'bo':Decimal("58.2"),
'az':Decimal("55.9"),
},
'law': {
'aa':Decimal("-999.00"),
'ab':Decimal("45.6"),
'ac':Decimal("45.7"),
'ad':Decimal("48.8"),
'ae':Decimal("-999.00"),
'af':Decimal("41.9"),
'ag':Decimal("39.1"),
'ah':Decimal("47.2"),
'ai':Decimal("-999.00"),
'aj':Decimal("40.9"),
'ak':Decimal("-999.00"),
'al':Decimal("-999.00"),
'am':Decimal("44.0"),
'an':Decimal("44.9"),
'ao':Decimal("-999.00"),
'ap':Decimal("42.9"),
'aq':Decimal("41.9"),
'ar':Decimal("50.7"),
'as':Decimal("41.9"),
'at':Decimal("44.8"),
'au':Decimal("44.1"),
'av':Decimal("41.2"),
'aw':Decimal("51.1"),
'ax':Decimal("45.3"),
'ay':Decimal("45.1"),
'ba':Decimal("46.1"),
'bb':Decimal("48.3"),
'bc':Decimal("-999.00"),
'bd':Decimal("46.3"),
'be':Decimal("46.5"),
'bf':Decimal("40.3"),
'bg':Decimal("45.0"),
'bh':Decimal("46.4"),
'bi':Decimal("47.3"),
'bj':Decimal("46.1"),
'bk':Decimal("48.1"),
'bl':Decimal("-999.00"),
'bm':Decimal("46.3"),
'bn':Decimal("46.8"),
'bo':Decimal("-999.00"),
'az':Decimal("46.4"),
},
'mec': {
'aa':Decimal("54.4"),
'ab':Decimal("-999.00"),
'ac':Decimal("-999.00"),
'ad':Decimal("-999.00"),
'ae':Decimal("54.3"),
'af':Decimal("-999.00"),
'ag':Decimal("54.4"),
'ah':Decimal("-999.00"),
'ai':Decimal("55.2"),
'aj':Decimal("-999.00"),
'ak':Decimal("53.6"),
'al':Decimal("56.1"),
'am':Decimal("54.8"),
'an':Decimal("-999.00"),
'ao':Decimal("51.9"),
'ap':Decimal("55.1"),
'aq':Decimal("-999.00"),
'ar':Decimal("-999.00"),
'as':Decimal("-999.00"),
'at':Decimal("-999.00"),
'au':Decimal("-999.00"),
'av':Decimal("53.6"),
'aw':Decimal("-999.00"),
'ax':Decimal("-999.00"),
'ay':Decimal("-999.00"),
'ba':Decimal("-999.00"),
'bb':Decimal("-999.00"),
'bc':Decimal("56.3"),
'bd':Decimal("-999.00"),
'be':Decimal("-999.00"),
'bf':Decimal("-999.00"),
'bg':Decimal("-999.00"),
'bh':Decimal("-999.00"),
'bi':Decimal("-999.00"),
'bj':Decimal("-999.00"),
'bk':Decimal("-999.00"),
'bl':Decimal("57.8"),
'bm':Decimal("-999.00"),
'bn':Decimal("-999.00"),
'bo':Decimal("56.9"),
'az':Decimal("-999.00"),
},
'math': {
'aa':Decimal("58.6"),
'ab':Decimal("61.2"),
'ac':Decimal("-999.00"),
'ad':Decimal("57.9"),
'ae':Decimal("56.8"),
'af':Decimal("56.3"),
'ag':Decimal("57.6"),
'ah':Decimal("59.4"),
'ai':Decimal("54.7"),
'aj':Decimal("-999.00"),
'ak':Decimal("-999.00"),
'al':Decimal("59.4"),
'am':Decimal("57.8"),
'an':Decimal("-999.00"),
'ao':Decimal("51.6"),
'ap':Decimal("60.5"),
'aq':Decimal("57.0"),
'ar':Decimal("60.6"),
'as':Decimal("-999.00"),
'at':Decimal("63.1"),
'au':Decimal("54.9"),
'av':Decimal("56.6"),
'aw':Decimal("61.3"),
'ax':Decimal("-999.00"),
'ay':Decimal("-999.00"),
'ba':Decimal("56.5"),
'bb':Decimal("-999.00"),
'bc':Decimal("62.2"),
'bd':Decimal("-999.00"),
'be':Decimal("54.7"),
'bf':Decimal("-999.00"),
'bg':Decimal("-999.00"),
'bh':Decimal("56.9"),
'bi':Decimal("59.6"),
'bj':Decimal("59.2"),
'bk':Decimal("-999.00"),
'bl':Decimal("60.6"),
'bm':Decimal("60.7"),
'bn':Decimal("-999.00"),
'bo':Decimal("62.6"),
'az':Decimal("-999.00"),
},
'med': {
'aa':Decimal("49.5"),
'ab':Decimal("-999.00"),
'ac':Decimal("49.0"),
'ad':Decimal("52.3"),
'ae':Decimal("-999.00"),
'af':Decimal("-999.00"),
'ag':Decimal("49.8"),
'ah':Decimal("3.00"),
'ai':Decimal("-999.00"),
'aj':Decimal("-999.00"),
'ak':Decimal("-999.00"),
'al':Decimal("-999.00"),
'am':Decimal("49.2"),
'an':Decimal("50.5"),
'ao':Decimal("48.0"),
'ap':Decimal("49.3"),
'aq':Decimal("51.2"),
'ar':Decimal("54.2"),
'as':Decimal("50.0"),
'at':Decimal("48.9"),
'au':Decimal("49.2"),
'av':Decimal("-999.00"),
'aw':Decimal("55.5"),
'ax':Decimal("51.1"),
'ay':Decimal("49.6"),
'ba':Decimal("50.7"),
'bb':Decimal("-999.00"),
'bc':Decimal("-999.00"),
'bd':Decimal("51.5"),
'be':Decimal("49.2"),
'bf':Decimal("51.1"),
'bg':Decimal("-999.00"),
'bh':Decimal("52.8"),
'bi':Decimal("52.6"),
'bj':Decimal("50.9"),
'bk':Decimal("49.6"),
'bl':Decimal("-999.00"),
'bm':Decimal("-999.00"),
'bn':Decimal("52.1"),
'bo':Decimal("60.1"),
'az':Decimal("52.2"),
},
'phys': {
'aa':Decimal("59.1"),
'ab':Decimal("62.3"),
'ac':Decimal("61.6"),
'ad':Decimal("61.9"),
'ae':Decimal("58.9"),
'af':Decimal("53.9"),
'ag':Decimal("56.8"),
'ah':Decimal("59.9"),
'ai':Decimal("59.8"),
'aj':Decimal("59.7"),
'ak':Decimal("-999.00"),
'al':Decimal("62.5"),
'am':Decimal("59.9"),
'an':Decimal("-999.00"),
'ao':Decimal("54.6"),
'ap':Decimal("60.3"),
'aq':Decimal("62.1"),
'ar':Decimal("61.6"),
'as':Decimal("57.6"),
'at':Decimal("60.4"),
'au':Decimal("56.4"),
'av':Decimal("57.5"),
'aw':Decimal("60.9"),
'ax':Decimal("61.6"),
'ay':Decimal("59.7"),
'ba':Decimal("58.7"),
'bb':Decimal("59.9"),
'bc':Decimal("59.7"),
'bd':Decimal("62.2"),
'be':Decimal("60.8"),
'bf':Decimal("62.8"),
'bg':Decimal("-999.00"),
'bh':Decimal("55.2"),
'bi':Decimal("62.0"),
'bj':Decimal("60.5"),
'bk':Decimal("61.2"),
'bl':Decimal("61.5"),
'bm':Decimal("-999.00"),
'bn':Decimal("61.6"),
'bo':Decimal("62.8"),
'az':Decimal("60.2"),
},
'pol': {
'aa':Decimal("50.8"),
'ab':Decimal("54.3"),
'ac':Decimal("61.4"),
'ad':Decimal("58.5"),
'ae':Decimal("-999.00"),
'af':Decimal("-999.00"),
'ag':Decimal("-999.00"),
'ah':Decimal("57.3"),
'ai':Decimal("54.0"),
'aj':Decimal("55.5"),
'ak':Decimal("57.1"),
'al':Decimal("59.7"),
'am':Decimal("55.9"),
'an':Decimal("-999.00"),
'ao':Decimal("52.5"),
'ap':Decimal("55.1"),
'aq':Decimal("53.1"),
'ar':Decimal("60.5"),
'as':Decimal("59.0"),
'at':Decimal("56.3"),
'au':Decimal("60.2"),
'av':Decimal("52.8"),
'aw':Decimal("59.5"),
'ax':Decimal("55.8"),
'ay':Decimal("52.2"),
'ba':Decimal("57.6"),
'bb':Decimal("65.9"),
'bc':Decimal("-999.00"),
'bd':Decimal("60.4"),
'be':Decimal("57.9"),
'bf':Decimal("54.7"),
'bg':Decimal("57.2"),
'bh':Decimal("56.7"),
'bi':Decimal("60.1"),
'bj':Decimal("55.4"),
'bk':Decimal("-999.00"),
'bl':Decimal("58.4"),
'bm':Decimal("58.0"),
'bn':Decimal("57.7"),
'bo':Decimal("-999.00"),
'az':Decimal("56.0"),
},
'psy': {
'aa':Decimal("62.7"),
'ab':Decimal("-999.00"),
'ac':Decimal("59.8"),
'ad':Decimal("59.8"),
'ae':Decimal("57.7"),
'af':Decimal("54.4"),
'ag':Decimal("55.2"),
'ah':Decimal("60.3"),
'ai':Decimal("-999.00"),
'aj':Decimal("52.5"),
'ak':Decimal("60.8"),
'al':Decimal("58.6"),
'am':Decimal("60.6"),
'an':Decimal("57.5"),
'ao':Decimal("-999.00"),
'ap':Decimal("58.7"),
'aq':Decimal("58.0"),
'ar':Decimal("64.1"),
'as':Decimal("58.0"),
'at':Decimal("59.8"),
'au':Decimal("57.3"),
'av':Decimal("-999.00"),
'aw':Decimal("59.8"),
'ax':Decimal("58.5"),
'ay':Decimal("58.4"),
'ba':Decimal("58.9"),
'bb':Decimal("59.1"),
'bc':Decimal("-999.00"),
'bd':Decimal("62.4"),
'be':Decimal("56.9"),
'bf':Decimal("57.6"),
'bg':Decimal("61.1"),
'bh':Decimal("62.2"),
'bi':Decimal("60.9"),
'bj':Decimal("62.1"),
'bk':Decimal("56.5"),
'bl':Decimal("-999.00"),
'bm':Decimal("58.3"),
'bn':Decimal("58.4"),
'bo':Decimal("-999.00"),
'az':Decimal("59.8"),
},
'soc': {
'aa':Decimal("51.0"),
'ab':Decimal("54.8"),
'ac':Decimal("55.5"),
'ad':Decimal("59.2"),
'ae':Decimal("59.1"),
'af':Decimal("55.6"),
'ag':Decimal("-999.00"),
'ah':Decimal("56.0"),
'ai':Decimal("51.5"),
'aj':Decimal("54.5"),
'ak':Decimal("53.3"),
'al':Decimal("52.0"),
'am':Decimal("56.2"),
'an':Decimal("48.8"),
'ao':Decimal("47.9"),
'ap':Decimal("55.4"),
'aq':Decimal("51.5"),
'ar':Decimal("57.5"),
'as':Decimal("-999.00"),
'at':Decimal("53.5"),
'au':Decimal("53.6"),
'av':Decimal("49.9"),
'aw':Decimal("52.2"),
'ax':Decimal("52.8"),
'ay':Decimal("-999.00"),
'ba':Decimal("56.1"),
'bb':Decimal("54.7"),
'bc':Decimal("-999.00"),
'bd':Decimal("59.5"),
'be':Decimal("55.7"),
'bf':Decimal("59.8"),
'bg':Decimal("55.0"),
'bh':Decimal("56.3"),
'bi':Decimal("54.0"),
'bj':Decimal("-999.00"),
'bk':Decimal("-999.00"),
'bl':Decimal("-999.00"),
'bm':Decimal("54.9"),
'bn':Decimal("1.00"),
'bo':Decimal("-999.00"),
'az':Decimal("-999.00"),
},
'eco': {
'aa':Decimal("-999.00"),
'ab':Decimal("-999.00"),
'ac':Decimal("50.5"),
'ad':Decimal("59.5"),
'ae':Decimal("49.6"),
'af':Decimal("-999.00"),
'ag':Decimal("-999.00"),
'ah':Decimal("53.6"),
'ai':Decimal("-999.00"),
'aj':Decimal("-999.00"),
'ak':Decimal("-999.00"),
'al':Decimal("-999.00"),
'am':Decimal("56.7"),
'an':Decimal("-999.00"),
'ao':Decimal("-999.00"),
'ap':Decimal("-999.00"),
'aq':Decimal("53.5"),
'ar':Decimal("53.3"),
'as':Decimal("-999.00"),
'at':Decimal("53.6"),
'au':Decimal("52.1"),
'av':Decimal("-999.00"),
'aw':Decimal("54.4"),
'ax':Decimal("-999.00"),
'ay':Decimal("50.5"),
'ba':Decimal("56.1"),
'bb':Decimal("59.0"),
'bc':Decimal("-999.00"),
'bd':Decimal("-999.00"),
'be':Decimal("50.7"),
'bf':Decimal("-999.00"),
'bg':Decimal("57.0"),
'bh':Decimal("54.1"),
'bi':Decimal("55.8"),
'bj':Decimal("52.3"),
'bk':Decimal("-999.00"),
'bl':Decimal("-999.00"),
'bm':Decimal("52.8"),
'bn':Decimal("60.8"),
'bo':Decimal("-999.00"),
'az':Decimal("53.3"),
},
}