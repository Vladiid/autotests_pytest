import pytest

from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
    "NONE"
])
def test_something1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"

])
def test_something2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_something3(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('it_IT').set_number(15)
    ).build()
    print(object_to_send)


def test_something(get_player_generator):
    print(get_player_generator.build())
