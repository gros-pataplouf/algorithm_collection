import pytest

from bfs_shortest_path import pilot_rocket

satellites = {
  'base': ['sat0'],
  'sat0': ['base', 'sat1', 'sat3', 'sat4'],
  'sat1': ['sat0', 'sat2'],
  'sat2': ['sat1', 'sat3', 'sat4'],
  'sat3': ['sat0', 'sat2', 'sat4'],
  'sat4': ['sat0', 'sat2', 'sat3', 'sat5'],
  'sat5': ['sat4', 'ship']
}

def test_shortest():
    assert pilot_rocket(satellites) == ['base', 'sat0', 'sat4', 'sat5', 'ship']