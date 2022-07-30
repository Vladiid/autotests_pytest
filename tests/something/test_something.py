import pytest


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
    "NONE"
])
def test_something(status, get_player_generator):
    print(get_player_generator.build())
