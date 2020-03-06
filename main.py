import csv
from ipl_analytics.csv.matches_played_per_year import compute_and_plot_matches_played_per_year
from ipl_analytics.csv.matches_won_by_teams_per_year import compute_and_plot_matches_won_by_teams_per_year
from ipl_analytics.csv.extra_runs_conceded_per_team_2016 import compute_and_plot_extra_runs_conceded_per_team
from ipl_analytics.csv.top_economical_bowlers_2015 import compute_and_plot_top_economical_bowlers
from ipl_analytics.csv.matches_won_after_toss_decision import compute_and_plot_matches_won_after_toss_decision
from configparser import ConfigParser


config = ConfigParser()
config.read('configuration.ini')

def read_matches(file='matches.csv'):
    """Fetch the matches.csv data into ordered dictionary format

    :param file : raw matches csv file \n
    :return matches : List of dictionaries of matches.csv data
    """

    with open(config['Data_fetching_path']['path']+file) as f_matches:
        matches = csv.DictReader(f_matches)
        # Retuning list of dictionaries i.e, matches data
        return list(matches)


def read_deliveries(file='deliveries.csv'):
    """Fetch the deliveries.csv data into ordered dictionary format

    :param file : raw deliveries csv file \n
    :return deliveries : List of dictionaries of deliveries.csv data
    """
    with open(config['Data_fetching_path']['path']+file) as f_deliveries:
        deliveries = csv.DictReader(f_deliveries)
        # Returning list of dictionaries i.e, deliveries data
        return list(deliveries)

def read_mock_matches(file='mock_matches.csv'):
    """Fetch the matches.csv data into ordered dictionary format

    :param file : raw mock_matches csv file \n
    :return matches : List of dictionaries of matches.csv data
    """
    with open(config['Data_fetching_path']['path']+file) as f_matches:
        matches = csv.DictReader(f_matches)
        # Retuning list of dictionaries i.e, matches data
        return list(matches)


def read_mock_deliveries(file='mock_deliveries.csv'):
    """Fetch the deliveries.csv data into ordered dictionary format

    :param file : raw mock_deliveries csv file \n
    :return deliveries : List of dictionaries of deliveries.csv data
    """
    with open(config['Data_fetching_path']['path']+file) as f_deliveries:
        deliveries = csv.DictReader(f_deliveries)
        # Returning list of dictionaries i.e, deliveries data
        return list(deliveries)


def main():
    """Call all the main functions of each scenario"""
    matches = read_matches()
    deliveries = read_deliveries()
    compute_and_plot_matches_played_per_year(matches)
    compute_and_plot_matches_won_by_teams_per_year(matches)
    compute_and_plot_extra_runs_conceded_per_team(matches, deliveries)
    compute_and_plot_top_economical_bowlers(matches, deliveries)
    compute_and_plot_matches_won_after_toss_decision(matches)


if __name__ == "__main__":
    main()
