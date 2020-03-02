from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches
from matches_won_after_toss_decision import matches_won_after_toss_decision


def test_matches_won_after_toss_decision():
    expected_output = { 2008: {}, 
                        2009: {}, 
                        2010: {}, 
                        2011: {'bat': 1, 'field': 1}, 
                        2015: {'field': 1}, 
                        2016: {'field': 1}, 
                        2017: {}}

    mock_matches = read_matches('mock_matches.csv')
    output = matches_won_after_toss_decision(mock_matches)

    assert expected_output == output