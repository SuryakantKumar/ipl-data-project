import matplotlib.pyplot as plt


def start_and_end_match_ids(matches):
    """Compute starting match id and ending match id from matches.csv data,
    on the basis of season 2015 to use into deliveries.csv data
    """
    start_id = 0
    live_id = 0
    for each in matches:
        if each['season'] != '2015':
            start_id += 1
        else:
            live_id += 1

    return start_id - live_id, start_id - 1


def top_economical_bowlers(deliveries, start_id, end_id):
    """Compute total runs conceded by each bowler and total deliveries by each bowler then top economical bowlers"""
    total_runs_per_baller = {}
    total_deliveries_per_baller = {}
    for each in deliveries:
        if int(each['match_id']) >= start_id and int(each['match_id']) <= end_id:
            if each['bowler'] not in total_runs_per_baller:
                if int(each['is_super_over']) == 0:
                    total_runs_per_baller[each['bowler']] = (
                        int(each['total_runs']) - (int(each['bye_runs']) + int(each['legbye_runs'])))

                if int(each['noball_runs']) != 0 or int(each['wide_runs']) != 0 or int(each['is_super_over']) != 0:
                    total_deliveries_per_baller[each['bowler']] = 0
                else:
                    total_deliveries_per_baller[each['bowler']] = 1

            else:
                if int(each['is_super_over']) == 0:
                    total_runs_per_baller[each['bowler']] += (
                        int(each['total_runs']) - (int(each['bye_runs']) + int(each['legbye_runs'])))

                if int(each['noball_runs']) != 0 or int(each['wide_runs']) != 0 or int(each['is_super_over']) != 0:
                    total_deliveries_per_baller[each['bowler']] += 0
                else:
                    total_deliveries_per_baller[each['bowler']] += 1

    total_economy_per_baller = {}
    for each in total_runs_per_baller:
        total_economy_per_baller[each] = (
            total_runs_per_baller[each] / total_deliveries_per_baller[each])*6

    total_economy_per_baller_swap = {}
    for player in total_economy_per_baller:
        total_economy_per_baller_swap[(
            total_economy_per_baller[player])] = player

    total_economy_per_baller_sorted = {}
    for economy in sorted(total_economy_per_baller_swap.keys()):
        total_economy_per_baller_sorted[economy] = total_economy_per_baller_swap[economy]

    top_economy_bowler = {}
    count = 0
    for each in total_economy_per_baller_sorted:
        if count == 15:
            break
        top_economy_bowler[float('%.3f' % each)
                           ] = total_economy_per_baller_sorted[each]
        count += 1

    return top_economy_bowler


def plot_top_economical_bowlers(top_economy_bowler):
    """plot horizontal bar chart for top economical bowlers"""
    bowlers = list(top_economy_bowler.values())
    economy = list(top_economy_bowler.keys())
    plt.barh(bowlers, economy, color="#6c3376",
             edgecolor="#409240", linewidth=1)
    plt.xlabel('Economy rates')
    plt.ylabel('Bowler')
    plt.title('Top economical bowlers 2015')
    plt.show()


def compute_and_plot_top_economical_bowlers(matches, deliveries):
    """Handle all the function calls here """
    start_id, end_id = start_and_end_match_ids(matches)
    top_economy_bowler = top_economical_bowlers(deliveries, start_id, end_id)
    plot_top_economical_bowlers(top_economy_bowler)
