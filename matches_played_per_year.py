import matplotlib.pyplot as plt


def matches_played_per_year(matches):
    """Compute number of matches played per year """
    match_played_per_year = {}
    for per_year_status in matches:
        if per_year_status['season'] in match_played_per_year:
            match_played_per_year[per_year_status['season']] += 1
        else:
            match_played_per_year[per_year_status['season']] = 1

    match_played_per_year_sorted = {}   # Sorted according to year
    for year in sorted(match_played_per_year.keys()):
        match_played_per_year_sorted[int(year)] = match_played_per_year[year]

    return match_played_per_year_sorted


def plot_matches_played_per_year(matches_per_year):
    """Plot bar chart for number of matches played per year """
    years = []
    matches_played = []

    for year in matches_per_year:
        years.append(year)  # Years in list
        matches_played.append(matches_per_year[year])   # matches in list

    plt.bar(years, matches_played, color='orange')

    plt.ylabel('Years')
    plt.xlabel('Matches')

    plt.title('Matches Played Per Year')
    plt.show()


def compute_and_plot_matches_played_per_year(matches):
    """Handle all the function calls here """
    matches_per_year = matches_played_per_year(matches)
    plot_matches_played_per_year(matches_per_year)
