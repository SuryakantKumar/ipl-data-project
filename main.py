import csv
from matches_played_per_year import *
from matches_won_by_teams_per_year import *
from extra_runs_conceded_per_team_2016 import *
from top_economical_bowlers_2015 import *
from matches_won_after_toss_decision import *


def read_matches():
    with open('/Users/suryakantkumar/MountBlueSpace/2020.02.20/IPL-Data-Project/ipl/matches.csv') as f_matches:
        matches = csv.DictReader(f_matches)
        # Retuning list of dictionaries i.e, matches data
        return list(matches)


def read_deliveries():
    with open('/Users/suryakantkumar/MountBlueSpace/2020.02.20/IPL-Data-Project/ipl/deliveries.csv') as f_deliveries:
        deliveries = csv.DictReader(f_deliveries)
        # Returning list of dictionaries i.e, deliveries data
        return list(deliveries)


def main():
    matches = read_matches()
    deliveries = read_deliveries()
    compute_and_plot_matches_played_per_year(matches)
    compute_and_plot_matches_won_by_teams_per_year(matches)
    compute_and_plot_extra_runs_conceded_per_team(matches, deliveries)
    compute_and_plot_top_economical_bowlers(matches, deliveries)
    compute_and_plot_matches_won_after_toss_decision(matches)


if __name__ == "__main__":
    main()
