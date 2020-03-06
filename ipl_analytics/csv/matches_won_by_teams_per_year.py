'''Importing pyplot module of matplotlib library'''

import matplotlib.pyplot as plt


def matches_won_by_team_per_year(matches):
    """Compute matches won by each team per season

    :param matches : list of dictionaries of matches.csv data \n
    :return matches_won_by_teams_per_year_sorted : Dictionary of dictionary of matches
    won by teams per year \n
    :return sorted(list(years)) : list of sorted years
    """
    matches_won_by_teams_per_year = {}
    years = set()
    for match in matches:
        if match['winner'] in matches_won_by_teams_per_year and match['winner'] != '':
            matches_won = matches_won_by_teams_per_year[match['winner']]

            if int(match['season']) in matches_won:
                matches_won[int(match['season'])] += 1
            else:
                matches_won[int(match['season'])] = 1
                years.add(int(match['season']))

        elif match['winner'] not in matches_won_by_teams_per_year and match['winner'] != '':
            matches_won_by_teams_per_year[match['winner']] = {}
            matches_won = matches_won_by_teams_per_year[match['winner']]
            matches_won[int(match['season'])] = 1
            years.add(int(match['season']))

    if 'Rising Pune Supergiants' in matches_won_by_teams_per_year:
        original_team = matches_won_by_teams_per_year['Rising Pune Supergiants']
        original_team.update(
            matches_won_by_teams_per_year['Rising Pune Supergiant'])
        del matches_won_by_teams_per_year['Rising Pune Supergiant']

    matches_won_by_teams_per_year_sorted = {}
    for team in matches_won_by_teams_per_year:
        match = matches_won_by_teams_per_year[team]
        for each_year in years:
            if each_year not in match:
                match[each_year] = 0
        year = {}
        for per_year in sorted(match.keys()):
            year[per_year] = match[per_year]
        matches_won_by_teams_per_year_sorted[team] = year

    return matches_won_by_teams_per_year_sorted, sorted(list(years))


def plot_matches_won_by_team_per_year(matches_won_by_teams_per_year, years):
    """Plot stacked bar chart for matches won by each team per season

    :param matches_won_by_teams_per_year:Dictionary of dictionary of matches won by teams per year\n
    :param years : list of sorted years
    """
    bottom_won_score = [0 for year in range(len(years))]
    teams = []
    for team in matches_won_by_teams_per_year:
        score = matches_won_by_teams_per_year[team]
        x_axis = list(score.keys())
        y_axis = list(score.values())
        plt.bar(x_axis, y_axis, bottom=bottom_won_score)
        for score in range(len(bottom_won_score)):
            bottom_won_score[score] += y_axis[score]
        teams.append(team)

    shortened_name_team = []
    for each_team in teams:
        shortened_name_each = [x_axis[0] for x_axis in each_team.split()]
        shortened_name_team.append("".join(shortened_name_each))

    plt.legend(shortened_name_team, ncol=4, loc='upper right')
    plt.xlabel('Years')
    plt.ylabel('Matches won')
    plt.title('Matches won by teams per year')

    plt.show()


def compute_and_plot_matches_won_by_teams_per_year(matches):
    """Handle all the function calls here

    :param matches : list of dictionaries of matches.csv data
    """
    matches_won_by_teams_per_year, teams = matches_won_by_team_per_year(
        matches)
    plot_matches_won_by_team_per_year(matches_won_by_teams_per_year, teams)
