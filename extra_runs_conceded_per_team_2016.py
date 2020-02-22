import matplotlib.pyplot as plt


def start_and_end_match_id(matches):
    start_id = 0
    live_id = 0
    for each in matches:
        if each['season'] != '2016':
            start_id += 1
        else:
            live_id += 1

    return start_id + 1, start_id + live_id


def extra_runs_conceded_per_team(deliveries, start_id, end_id):
    teams_with_extras = {}
    for each in deliveries:
        if int(each['match_id']) >= start_id and int(each['match_id']) <= end_id:
            if each['bowling_team'] not in teams_with_extras:
                teams_with_extras[each['bowling_team']] = int(
                    each['extra_runs'])
            else:
                teams_with_extras[each['bowling_team']
                                  ] += int(each['extra_runs'])
    return teams_with_extras


def plot_extra_runs_conceded_per_team(teams_with_extras):
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
    start_id, end_id = start_and_end_match_id(matches)
    teams_with_extras = extra_runs_conceded_per_team(
        deliveries, start_id, end_id)
    plot_extra_runs_conceded_per_team(teams_with_extras)
