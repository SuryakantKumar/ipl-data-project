import matplotlib.pyplot as plt


def start_and_end_match_id(matches):
    """Compute starting match id and ending match id from matches.csv data,
    on the basis of season 2016 to use into deliveries.csv data
    """
    start_id = 0
    live_id = 0
    for each in matches:
        if each['season'] != '2016':
            start_id += 1
        else:
            live_id += 1

    return start_id + 1, start_id + live_id


def extra_runs_conceded_per_team(deliveries, start_id, end_id):
    """For every ball, Compute all the teams with their extra runs conceded """
    teams_with_extras = {}
    for each in deliveries:
        if int(each['match_id']) >= start_id and int(each['match_id']) <= end_id:
            if each['bowling_team'] not in teams_with_extras:
                if int(each['is_super_over']) == 0:
                    teams_with_extras[each['bowling_team']] = int(
                        each['extra_runs'])
            else:
                if int(each['is_super_over']) == 0:
                    teams_with_extras[each['bowling_team']
                                      ] += int(each['extra_runs'])
    return teams_with_extras


def plot_extra_runs_conceded_per_team(teams_with_extras):
    """Plot horizontal bar chart for extra runs conceded by each team in season 2016 """
    teams = list(teams_with_extras.keys())
    shortened_teams = []
    for ele in teams:
        shortened_each = [x[0] for x in ele.split()]
        shortened_teams.append("".join(shortened_each))

    runs = list(teams_with_extras.values())

    plt.barh(shortened_teams, runs, color="#6c3376",
             edgecolor="#409240", linewidth=1)
    plt.xlabel('Extra runs conceded by Teams')
    plt.ylabel('Teams')
    plt.title('Extra runs conceded per team in 2016')
    plt.show()


def compute_and_plot_extra_runs_conceded_per_team(matches, deliveries):
    """Handle all the function calls here """
    start_id, end_id = start_and_end_match_id(matches)
    teams_with_extras = extra_runs_conceded_per_team(
        deliveries, start_id, end_id)
    plot_extra_runs_conceded_per_team(teams_with_extras)
