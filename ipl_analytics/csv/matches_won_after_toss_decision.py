import matplotlib.pyplot as plt


def matches_won_after_toss_decision(matches):
    """Compute number of winning matches by toss winner and decision,
    of either choosing bat first or field first for every season 

    :param matches : list of dictionaries of matches.csv data \n
    :return sorted_bat_field_per_year : Dictionary of dictionary of win over choosing bat and field per year
    """
    bat_field_per_year = {}
    for match in matches:
        if int(match['season']) not in bat_field_per_year:
            bat_field_won_count = {}
            if match['toss_winner'] == match['winner']:
                if match['toss_decision'] == 'bat':
                    bat_field_won_count['bat'] = 1
                else:
                    bat_field_won_count['field'] = 1
            bat_field_per_year[int(match['season'])] = bat_field_won_count

        else:
            bat_field_won_count = bat_field_per_year[int(match['season'])]
            if match['toss_winner'] == match['winner']:

                if match['toss_decision'] == 'bat' and 'bat' in bat_field_won_count:
                    bat_field_won_count['bat'] += 1
                elif match['toss_decision'] == 'bat' and 'bat' not in bat_field_won_count:
                    bat_field_won_count['bat'] = 1
                elif match['toss_decision'] == 'field' and 'field' in bat_field_won_count:
                    bat_field_won_count['field'] += 1
                elif match['toss_decision'] == 'field' and 'field' not in bat_field_won_count:
                    bat_field_won_count['field'] = 1

    sorted_bat_field_per_year = {}
    for year in sorted(bat_field_per_year.keys()):
        sorted_bat_field_per_year[int(year)] = bat_field_per_year[year]

    return sorted_bat_field_per_year


def plot_matches_won_after_toss_decision(sorted_bat_field_per_year):
    """Plot stacked bar chart for number of winning matches after toss decision as bat/field

    :param sorted_bat_field_per_year : Dictionary of dictionary of win over choosing bat and field per year
    """
    years = []
    won_over_bat = []
    won_over_field = []
    for year in sorted_bat_field_per_year:
        years.append(year)
        won_over_bat.append(sorted_bat_field_per_year[year]['bat'])
        won_over_field.append(sorted_bat_field_per_year[year]['field'])

    plt.bar(years, won_over_bat)
    plt.bar(years, won_over_field, bottom=won_over_bat)

    plt.legend(['matches won over bat', 'matches won over field'],
               loc='upper right')
    plt.xlabel('Years')
    plt.ylabel('Matches won')
    plt.title('Matches won after toss decision as bat or field')

    plt.show()


def compute_and_plot_matches_won_after_toss_decision(matches):
    """Handle all the function calls here 

    :param matches : list of dictionaries of matches.csv data
    """
    sorted_bat_field_per_year = matches_won_after_toss_decision(matches)
    plot_matches_won_after_toss_decision(sorted_bat_field_per_year)
