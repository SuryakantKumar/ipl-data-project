import csv
from matches_played_per_year import compute_and_plot_matches_played_per_year
from matches_won_by_teams_per_year import compute_and_plot_matches_won_by_teams_per_year
from extra_runs_conceded_per_team_2016 import compute_and_plot_extra_runs_conceded_per_team
from top_economical_bowlers_2015 import compute_and_plot_top_economical_bowlers
from matches_won_after_toss_decision import compute_and_plot_matches_won_after_toss_decision


def read_matches(file):
    """Fetch the matches.csv data into ordered dictionary format"""
    with open('/Users/suryakantkumar/MountBlueSpace/2020.02.20/IPL-Data-Project/ipl/'+file) as f_matches:
        matches = csv.DictReader(f_matches)
        # Retuning list of dictionaries i.e, matches data
        return list(matches)


def read_deliveries(file):
    """Fetch the deliveries.csv data into ordered dictionary format"""
    with open('/Users/suryakantkumar/MountBlueSpace/2020.02.20/IPL-Data-Project/ipl/'+file) as f_deliveries:
        deliveries = csv.DictReader(f_deliveries)
        # Returning list of dictionaries i.e, deliveries data
        return list(deliveries)


def main():
    """Call all the main functions of each scenario"""
    matches = read_matches('matches.csv')
    deliveries = read_deliveries('deliveries.csv')
    compute_and_plot_matches_played_per_year(matches)
    compute_and_plot_matches_won_by_teams_per_year(matches)
    compute_and_plot_extra_runs_conceded_per_team(matches, deliveries)
    compute_and_plot_top_economical_bowlers(matches, deliveries)
    compute_and_plot_matches_won_after_toss_decision(matches)


if __name__ == "__main__":
    main()
