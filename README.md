# Introduction

This is a repository consisting of some analysis and representation of data over the IPL Data set available on kaggle https://www.kaggle.com/manasgarg/ipl 

Install 'requirements.txt' if you want to use this project.

At first, i transformed these data files from raw csv format to a data structure in a format suitable for plotting with matplotlib.

I have covered basic analysis of Ipl during 2008 - 2017 as :

1. Compute and Plot the number of matches played per season of all the seasons in IPL [2008-2017].
2. Compute and Plot a stacked bar chart of matches won of all teams over all the seasons of IPL [2008-2017].
3. Compute and Plot the extra runs conceded per team for season 2016.
4. Compute and plot the top economical bowlers for season 2015.
5. Compute and Plot stacked bar chart for total number of matches won over toss decision as bat/field over all the seasons [2008-2017]

## Directory Structure :

    IPL-Data-Project
    ├── README.md
    ├── analytics_plots
    │   ├── extra_runs_conceded_per_team_2016.png
    │   ├── matches_played_per_year.png
    │   ├── matches_won_after_toss_decision.png
    │   ├── matches_won_by_teams_per_year.png
    │   └── top_economical_bowlers_2015.png
    ├── ipl_analytics
    │   ├── __init__.py
    │   ├── csv
    │   │   ├── __init__.py
    │   │   ├── extra_runs_conceded_per_team_2016.py
    │   │   ├── matches_played_per_year.py
    │   │   ├── matches_won_after_toss_decision.py
    │   │   ├── matches_won_by_teams_per_year.py
    │   │   └── top_economical_bowlers_2015.py
    │   └── postgres
    │       ├── __init__.py
    │       ├── configuration.ini
    │       ├── ipl_test_db.txt
    │       └── problem_queries.py
    ├── ipl_data
    │   ├── deliveries.csv
    │   ├── matches.csv
    │   ├── mock_deliveries.csv
    │   └── mock_matches.csv
    ├── main.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        ├── configuration.ini
        ├── test_extra_runs_conceded_per_team_2016.py
        ├── test_matches_played_per_year.py
        ├── test_matches_won_after_toss_decision.py
        ├── test_matches_won_by_teams_per_year.py
        ├── test_postgres.py
        └── test_top_economical_bowlers_2015.py


## Instructions :
- Execute 'main.py' file in IPL-Data-Project directory to see the plots. Make sure the paths are correct according to the project on your system. You can change it in main.py file at the time of extraction of data
- There are five resulting plot files (.png format) in analytics_plots directories representing my analysis.
- If you want to run the tests on CSV or postgres then, First navigate to 'tests' folder then execute 'py.test'
- If you want to check the coverage of the tests then, First navigate to 'tests' folder then you can generate html page of coverage for every test using command 'coverage html' 