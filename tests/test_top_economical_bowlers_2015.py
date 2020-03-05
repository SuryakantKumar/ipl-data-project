from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from main import read_matches, read_deliveries
from ipl_analytics.csv.top_economical_bowlers_2015 import start_and_end_match_ids, top_economical_bowlers


def test_start_and_end_match_ids():
    '''test case of start_and_end_match_ids() function for top economical bowlers'''

    expected_output = (518, 519)

    mock_matches = read_matches('mock_matches.csv')
    output = start_and_end_match_ids(mock_matches)

    assert expected_output == output
 

def test_top_economical_bowlers():
    '''test case of top_economical_bowlers() function for top economical bowlers'''

    expected_output = {5.0: 'NM Coulter-Nile', 
                    6.0: 'JP Duminy', 
                    6.5: 'Imran Tahir', 
                    7.6: 'R Vinay Kumar', 
                    8.33: 'SL Malinga', 
                    8.5: 'DJ Muthuswami', 
                    9.5: 'Harbhajan Singh', 
                    11.0: 'JA Morkel', 
                    11.5: 'PP Ojha', 
                    12.67: 'JJ Bumrah'}

    mock_matches = read_matches('mock_matches.csv')
    mock_deliveries = read_deliveries('mock_deliveries.csv')
    start_id, end_id = start_and_end_match_ids(mock_matches)
    output = top_economical_bowlers(mock_deliveries, start_id, end_id)

    assert expected_output == output
