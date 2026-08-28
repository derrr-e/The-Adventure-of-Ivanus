from locations import locations

def test_no_enemies_means_zero_enemies_weight():
    for loc_name, loc_data in locations.items():
        if loc_data['enemies'] is None:
            assert loc_data['event_weights']['enemy'] == 0, \
                f'Локация {loc_name} без врагов, но с ненулевым шансом на бой'