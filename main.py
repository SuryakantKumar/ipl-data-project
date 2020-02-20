import csv
from matches_played_per_year import *


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


if __name__ == "__main__":
    main()
