from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches
from matches_won_by_teams_per_year import matches_won_by_team_per_year

def test_matches_won_by_team_per_year():
    expected_output = ({'Sunrisers Hyderabad': {2008: 0, 2009: 0, 2010: 0, 2011: 0, 2015: 0, 2016: 0, 2017: 1},
                        'Kolkata Knight Riders': {2008: 1, 2009: 0, 2010: 1, 2011: 0, 2015: 1, 2016: 1, 2017: 0},
                        'Mumbai Indians': {2008: 0, 2009: 1, 2010: 0, 2011: 0, 2015: 0, 2016: 0, 2017: 0},
                        'Chennai Super Kings': {2008: 0, 2009: 0, 2010: 0, 2011: 1, 2015: 1, 2016: 0, 2017: 0},
                        'Rajasthan Royals': {2008: 0, 2009: 0, 2010: 0, 2011: 1, 2015: 0, 2016: 0, 2017: 0},
                        'Rising Pune Supergiants': {2008: 0, 2009: 0, 2010: 0, 2011: 0, 2015: 0, 2016: 1, 2017: 0}},
                        [2008, 2009, 2010, 2011, 2015, 2016, 2017])

    mock_matches = read_matches('mock_matches.csv')
    output = matches_won_by_team_per_year(mock_matches)

    assert expected_output == output