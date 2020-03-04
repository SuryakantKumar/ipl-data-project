from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches
from ipl_analytics.csv.matches_played_per_year import matches_played_per_year

def test_matches_played_per_year():
    expected_output = {2008: 1, 2009: 1, 2010: 1, 2011: 2, 2015: 2, 2016: 2, 2017: 6}

    mock_matches = read_matches('mock_matches.csv')
    output = matches_played_per_year(mock_matches)
    assert expected_output == output