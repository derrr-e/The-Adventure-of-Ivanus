from unittest.mock import patch
import gameplay


def test_game_goes_thought_all_locations():
    locs = {
        "a": {"key": "a"},
        "b": {"key": "b"},
        "g": {"key": "g"},
        "c": {"key": "c", "end": True},
    }

    with (
        patch("gameplay.locations", locs),
        patch("gameplay.ch_loc", side_effect=[locs["b"], locs["g"], locs["c"]]),
        patch("gameplay.triger_random_events", return_value={"status": "alive"}),
        patch("gameplay.handle_location_menu", return_value={"status": "alive"}),
        patch("gameplay.show_location") as m_show,
    ):

        result = gameplay.game(None, "a")
        arg_list = [x.args[0] for x in m_show.call_args_list]

        assert result["status"] == "completed"
        assert arg_list == ["a", "b", "g"]
