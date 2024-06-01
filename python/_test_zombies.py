import pytest

from zombies import Survivor

def test_survivor_name():
    my_survivor = Survivor("kikolool")
    assert my_survivor.name and isinstance(my_survivor.name, str)


def test_survivor_0wounds_start():
    my_survivor = Survivor("kikolool")
    assert my_survivor.wounds == 0


def test_survivor_0wounds_start():
    my_survivor = Survivor("kikolool")
    my_survivor.gets_hurt(num_of_wounds=2)
    assert my_survivor.alive == False

def test_can_perform_3_actions_per_turn():
    my_survivor = Survivor("zombie_slayer")
    my_survivor.act()
    my_survivor.act()
    my_survivor.act()
    assert my_survivor.actions == 0

 
