# Saved linear voting profile: 
from collections import OrderedDict 
candidates = OrderedDict([
('c1', {'name': 'Candidate 1'}),
('c2', {'name': 'Candidate 2'}),
('c3', {'name': 'Candidate 3'}),
])
voters = OrderedDict([
('v1', {
'weight':2}),
('v2', {
'weight':3}),
('v3', {
'weight':1}),
('v4', {
'weight':5}),
('v5', {
'weight':4}),
])
linearBallot = {
'v1': [
'c2',
'c1',
'c3',
],
'v2': [
'c3',
'c1',
'c2',
],
'v3': [
'c1',
'c3',
'c2',
],
'v4': [
'c1',
'c2',
'c3',
],
'v5': [
'c3',
'c1',
'c2',
],
}
