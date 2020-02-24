import matplotlib.pyplot as plt


def matches_played_per_year(matches):
    """Compute number of matches played per year """
    mppy = {}                           # Matches played per year
    for pys in matches:                 # per year status
        if pys['season'] in mppy:
            mppy[pys['season']] += 1
        else:
            mppy[pys['season']] = 1

    match = {}                          # Sorted according to year
    for key in sorted(mppy.keys()):
        match[int(key)] = mppy[key]

    return match


def plot_matches_played_per_year(matches_per_year):
    """Plot bar chart for number of matches played per year """
    years = []
    matches_played = []

    for year in matches_per_year:
        years.append(year)              # Years in list
        # matches in list
        matches_played.append(matches_per_year[year])

    plt.bar(years, matches_played, color='orange')

    plt.ylabel('Years')
    plt.xlabel('Matches')

    plt.title('Matches Played Per Year')
    plt.show()


def compute_and_plot_matches_played_per_year(matches):
    """Handle all the function calls here """
    matches_per_year = matches_played_per_year(matches)
    plot_matches_played_per_year(matches_per_year)
