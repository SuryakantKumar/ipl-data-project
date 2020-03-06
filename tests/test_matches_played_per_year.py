from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_mock_matches
from ipl_analytics.csv.matches_played_per_year import matches_played_per_year

def test_matches_played_per_year():
    '''test case of matches_played_per_year() function for matches played per year'''

    expected_output = {2008: 1, 2009: 1, 2010: 1, 2011: 2, 2015: 2, 2016: 2, 2017: 6}

    mock_matches = read_mock_matches()
    output = matches_played_per_year(mock_matches)
    assert expected_output == output