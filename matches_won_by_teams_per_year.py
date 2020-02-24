import matplotlib.pyplot as plt


def matches_won_by_team_per_year(matches):
    """Compute matches won by each team per season"""
    result = {}
    years = set()
    for each in matches:
        if each['winner'] in result and each['winner'] != '':
            matches_won_dict = result[each['winner']]
            if int(each['season']) in matches_won_dict:
                matches_won_dict[int(each['season'])] += 1
            else:
                matches_won_dict[int(each['season'])] = 1
                years.add(int(each['season']))

        elif each['winner'] not in result and each['winner'] != '':
            result[each['winner']] = {}
            matches_won_dict = result[each['winner']]
            matches_won_dict[int(each['season'])] = 1
            years.add(int(each['season']))

    if 'Rising Pune Supergiants' in result:
        keep = result['Rising Pune Supergiants']
        keep.update(result['Rising Pune Supergiant'])
        del result['Rising Pune Supergiant']

    sorted_year_result = {}
    for team in result:
        each = result[team]
        for y in years:             # y is each year
            if y not in each:
                each[y] = 0
        year = {}
        for key in sorted(each.keys()):
            year[key] = each[key]
        sorted_year_result[team] = year

    return sorted_year_result, sorted(list(years))


def plot_matches_won_by_team_per_year(mwbtpy, years):
    """Plot stacked bar chart for matches won by each team per season"""
    bottom_li = [0 for i in range(len(years))]
    teams = []
    for team in mwbtpy:
        score = mwbtpy[team]
        x = list(score.keys())          # Horizontal axis
        y = list(score.values())        # Vertical axis
        plt.bar(x, y, bottom=bottom_li)
        for i in range(len(bottom_li)):
            bottom_li[i] += y[i]
        teams.append(team)

    shortened_teams = []
    for ele in teams:
        shortened_each = [x[0] for x in ele.split()]
        shortened_teams.append("".join(shortened_each))

    plt.legend(shortened_teams, ncol=4, loc='upper right')
    plt.xlabel('Years')
    plt.ylabel('Matches won')
    plt.title('Matches won by teams per year')

    plt.show()


def compute_and_plot_matches_won_by_teams_per_year(matches):
    """Handle all the function calls here """
    mwbtpy, teams = matches_won_by_team_per_year(matches)
    plot_matches_won_by_team_per_year(mwbtpy, teams)
