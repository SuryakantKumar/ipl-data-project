import matplotlib.pyplot as plt


def start_and_end_match_id(matches):
    """Compute starting match id and ending match id from matches.csv data,
    on the basis of season 2016 to use into deliveries.csv data
    """
    start_id = 1000
    end_id = -1000
    for match in matches:
        if match['season'] == '2016':
            if int(match['id']) < start_id:
                start_id = int(match['id'])
            
            if int(match['id']) > end_id:
                end_id = int(match['id'])
    return start_id, end_id


def extra_runs_conceded_per_team(deliveries, start_id, end_id):
    """For every ball, Compute all the teams with their extra runs conceded """
    teams_with_extras = {}
    for delivery in deliveries:
        if start_id <= int(delivery['match_id']) <= end_id:
            if delivery['bowling_team'] not in teams_with_extras:
                if int(delivery['is_super_over']) == 0:
                    teams_with_extras[delivery['bowling_team']] = int(
                        delivery['extra_runs'])
            else:
                if int(delivery['is_super_over']) == 0:
                    teams_with_extras[delivery['bowling_team']
                                      ] += int(delivery['extra_runs'])
    # Handle the edge case when "Rising pune supergiant" in present along side 
    if 'Rising Pune Supergiant' in teams_with_extras:
        if 'Rising Pune Supergiants' in teams_with_extras:
            teams_with_extras['Rising Pune Supergiants'] += teams_with_extras['Rising Pune Supergiant']
            del teams_with_extras['Rising Pune Supergiant']
        else:
            teams_with_extras['Rising Pune Supergiants'] = teams_with_extras['Rising Pune Supergiant']
            del teams_with_extras['Rising Pune Supergiant']

    return teams_with_extras


def plot_extra_runs_conceded_per_team(teams_with_extras):
    """Plot horizontal bar chart for extra runs conceded by each team in season 2016 """
    teams = list(teams_with_extras.keys())
    shortened_name_teams = []
    for team in teams:
        shortened_each = [word[0] for word in team.split()]
        shortened_name_teams.append("".join(shortened_each))

    runs = list(teams_with_extras.values())

    plt.barh(shortened_name_teams, runs, color="#6c3376",
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
