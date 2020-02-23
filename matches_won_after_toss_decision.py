import matplotlib.pyplot as plt


def matches_won_after_toss_decision(matches):
    bat_field_per_year = {}
    for row in matches:
        if int(row['season']) not in bat_field_per_year:
            bat_field_won_count = {}
            if row['toss_winner'] == row['winner']:
                if row['toss_decision'] == 'bat':
                    bat_field_won_count['bat'] = 1
                else:
                    bat_field_won_count['field'] = 1
            bat_field_per_year[int(row['season'])] = bat_field_won_count

        else:
            bat_field_won_count = bat_field_per_year[int(row['season'])]
            if row['toss_winner'] == row['winner']:

                if row['toss_decision'] == 'bat' and 'bat' in bat_field_won_count:
                    bat_field_won_count['bat'] += 1
                elif row['toss_decision'] == 'bat' and 'bat' not in bat_field_won_count:
                    bat_field_won_count['bat'] = 1
                elif row['toss_decision'] == 'field' and 'field' in bat_field_won_count:
                    bat_field_won_count['field'] += 1
                elif row['toss_decision'] == 'field' and 'field' not in bat_field_won_count:
                    bat_field_won_count['field'] = 1
    return bat_field_per_year


def plot_matches_won_after_toss_decision(bat_field_per_year):
    sorted_bat_field_per_year = {}
    for year in sorted(bat_field_per_year.keys()):
        sorted_bat_field_per_year[int(year)] = bat_field_per_year[year]

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
    bat_field_per_year = matches_won_after_toss_decision(matches)
    plot_matches_won_after_toss_decision(bat_field_per_year)
