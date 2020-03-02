from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches, read_deliveries
from extra_runs_conceded_per_team_2016 import start_and_end_match_id, extra_runs_conceded_per_team


def test_start_and_end_match_id():
    expected_output = (577, 578)

    mock_matches = read_matches('mock_matches.csv')
    output = start_and_end_match_id(mock_matches)

    assert expected_output == output

def test_extra_runs_conceded_per_team():
    expected_output = {'Kolkata Knight Riders': 1, 'Rising Pune Supergiants': 8}

    mock_matches = read_matches('mock_matches.csv')
    mock_deliveries = read_deliveries('mock_deliveries.csv')
    start_id, end_id = start_and_end_match_id(mock_matches)
    output = extra_runs_conceded_per_team(mock_deliveries, start_id, end_id)

    assert expected_output == output
