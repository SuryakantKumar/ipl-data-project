from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from ipl_analytics.postgres.problem_queries import (matches_played_per_year_sql,
                       matches_won_by_teams_per_year_sql,
                       extra_runs_conceded_per_team_2016_sql,
                       top_economical_bowlers_2015_sql,
                       matches_won_after_toss_decision)


def test_matches_played_per_year_sql():
    '''test case of matches_played_per_year_sql() function for sql query'''

    expected_output = {2017: 6, 
                        2016: 2, 
                        2010: 1, 
                        2015: 2, 
                        2009: 1, 
                        2008: 1, 
                        2011: 2}

    output = matches_played_per_year_sql(table='mock_matches')

    assert expected_output == output


def test_matches_won_by_teams_per_year_sql():
    '''test case of matches_won_by_teams_per_year_sql() function for sql query'''

    expected_output = {'Chennai Super Kings': {2011: 1, 2015: 1}, 
                        'Delhi Daredevils': {2017: 3}, 
                        'Kolkata Knight Riders': {2008: 1, 2010: 1, 2015: 1, 2016: 1, 2017: 1}, 
                        'Mumbai Indians': {2009: 1}, 
                        'Rajasthan Royals': {2011: 1}, 
                        'Rising Pune Supergiant': {2016: 1}, 
                        'Sunrisers Hyderabad': {2017: 2}}

    output = matches_won_by_teams_per_year_sql(table='mock_matches')

    assert expected_output == output


def test_extra_runs_conceded_per_team_2016_sql():
    '''test case of extra_runs_conceded_per_team_2016_sql() function for sql query'''

    expected_output = {'Kolkata Knight Riders': 1, 
                        'Rising Pune Supergiant': 4, 
                        'Rising Pune Supergiants': 4}

    output = extra_runs_conceded_per_team_2016_sql(
        table1='mock_matches', table2='mock_deliveries')

    assert expected_output == output


def test_top_economical_bowlers_2015_sql():
    '''test case of top_economical_bowlers_2015_sql() function for sql query'''

    expected_output = {'NM Coulter-Nile': 5.0, 
                        'JP Duminy': 6.0, 
                        'A Mishra': 6.0, 
                        'Imran Tahir': 6.5, 
                        'R Vinay Kumar': 7.6, 
                        'SL Malinga': 8.33, 
                        'DJ Muthuswami': 8.5, 
                        'Harbhajan Singh': 9.5, 
                        'JA Morkel': 11.0, 
                        'PP Ojha': 11.5}

    output = top_economical_bowlers_2015_sql(
        table1='mock_matches', table2='mock_deliveries')

    assert expected_output == output


def test_matches_won_after_toss_decision():
    '''test case of matches_won_after_toss_decision() function for sql query'''

    expected_output = {2011: {'bat': 1, 'field': 1}, 
                        2017: {'bat': 2, 'field': 3}}

    output = matches_won_after_toss_decision(table='mock_matches')

    assert expected_output == output
