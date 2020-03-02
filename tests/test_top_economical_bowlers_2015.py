from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches, read_deliveries
from top_economical_bowlers_2015 import start_and_end_match_ids, top_economical_bowlers


def test_start_and_end_match_ids():
    expected_output = (518, 519)

    mock_matches = read_matches('mock_matches.csv')
    output = start_and_end_match_ids(mock_matches)

    assert expected_output == output
 

def test_top_economical_bowlers():
    expected_output = {6.0: 'DJ Muthuswami', 6.75: 'M Morkel', 7.5: 'UT Yadav', 8.57: 'NM Coulter-Nile', 12.0: 'JA Morkel'}

    mock_matches = read_matches('mock_matches.csv')
    mock_deliveries = read_deliveries('mock_deliveries.csv')
    start_id, end_id = start_and_end_match_ids(mock_matches)
    output = top_economical_bowlers(mock_deliveries, start_id, end_id)

    assert expected_output == output
