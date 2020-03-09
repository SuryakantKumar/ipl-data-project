'''Importing pyplot module of matplotlib library'''

import matplotlib.pyplot as plt


def start_and_end_match_ids(matches):
    """Compute starting match id and ending match id from matches.csv data,
    on the basis of season 2015 to use into deliveries.csv data

    :param matches : list of dictionaries of matches.csv data\n
    :return start_id : int start match id of matches played in 2015\n
    :return end_id : int end match id of matches played in 2015
    """
    start_ids = 10000
    end_ids = -10000
    for match in matches:
        if match['season'] == '2015':
            if int(match['id']) < start_ids:
                start_ids = int(match['id'])

            if int(match['id']) > end_ids:
                end_ids = int(match['id'])
    return start_ids, end_ids


def top_economical_bowlers(deliveries, start_id, end_id):
    """Compute total runs conceded by each bowler and total deliveries by
    each bowler then top economical bowlers

    :param deliveries : list of dictionaries of deliveries.csv data\n
    :param start_id : int start match id of matches played in 2015\n
    :param end_id : int end match id of matches played in 2015\n
    :return top_economy_bowlers : dictionary of bowlers having top economy
    """
    total_runs_per_bowler, total_deliveries_per_bowler = {}, {}
    for delivery in deliveries:
        if start_id <= int(delivery['match_id']) <= end_id:
            if delivery['bowler'] not in total_runs_per_bowler:
                if int(delivery['is_super_over']) == 0:
                    total_runs_per_bowler[delivery['bowler']] = (
                        int(delivery['total_runs']) - (int(delivery['bye_runs']) + int(delivery['legbye_runs'])))
                if int(delivery['noball_runs']) != 0 or int(delivery['wide_runs']) != 0 or int(delivery['is_super_over']) != 0:
                    total_deliveries_per_bowler[delivery['bowler']] = 0
                else:
                    total_deliveries_per_bowler[delivery['bowler']] = 1
            else:
                if int(delivery['is_super_over']) == 0:
                    total_runs_per_bowler[delivery['bowler']] += (
                        int(delivery['total_runs']) - (int(delivery['bye_runs']) + int(delivery['legbye_runs'])))
                if int(delivery['noball_runs']) != 0 or int(delivery['wide_runs']) != 0 or int(delivery['is_super_over']) != 0:
                    total_deliveries_per_bowler[delivery['bowler']] += 0
                else:
                    total_deliveries_per_bowler[delivery['bowler']] += 1

    total_economy_per_bowler = {}
    for bowler in total_runs_per_bowler:
        total_economy_per_bowler[float('%.2f' % (
            (total_runs_per_bowler[bowler] / total_deliveries_per_bowler[bowler])*6))] = bowler

    total_economy_per_bowler_sorted = {}
    for economy in sorted(total_economy_per_bowler.keys()):
        total_economy_per_bowler_sorted[economy] = total_economy_per_bowler[economy]

    top_economy_bowlers, limit_count = {}, 0
    for delivery in total_economy_per_bowler_sorted:
        if limit_count == 10:
            break
        top_economy_bowlers[delivery] = total_economy_per_bowler_sorted[delivery]
        limit_count += 1
    return top_economy_bowlers


def plot_top_economical_bowlers(top_economy_bowler):
    """plot horizontal bar chart for top economical bowlers

    :param top_economy_bowlers : dictionary of bowlers having top economy
    """
    bowlers = list(top_economy_bowler.values())
    economy = list(top_economy_bowler.keys())
    plt.barh(bowlers, economy, color="#6c3376",
             edgecolor="#409240", linewidth=1)
    plt.xlabel('Economy rates')
    plt.ylabel('Bowler')
    plt.title('Top economical bowlers 2015')
    plt.show()


def compute_and_plot_top_economical_bowlers(matches, deliveries):
    """Handle all the function calls here

    :param matches : list of dictionaries of matches.csv data\n
    :param deliveries : list of dictionaries of deliveries.csv data
    """
    start_id, end_id = start_and_end_match_ids(matches)
    top_economy_bowlers = top_economical_bowlers(deliveries, start_id, end_id)
    plot_top_economical_bowlers(top_economy_bowlers)
