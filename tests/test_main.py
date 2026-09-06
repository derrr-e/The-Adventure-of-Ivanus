from unittest.mock import patch
from main import main


def test_main_passes_correct_location():
    with patch('main.menu', return_value='forest'):
        with patch('main.game') as mock_game:
            main()
            
    mock_game.assert_called_once()
    call_args = mock_game.call_args
    assert call_args[0][1] == 'forest'
    
    
    