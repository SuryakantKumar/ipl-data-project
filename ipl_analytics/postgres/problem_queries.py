import psycopg2 as pg
from configparser import ConfigParser
from simplecrypt import decrypt
from base64 import b64decode
 
 
def config(filename='configuration.ini', section='postgres'):
    parser = ConfigParser()
    parser.read(filename)

    message = parser['encryption_key']['key']

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    encoded_cipher = db['password']
    cipher = b64decode(encoded_cipher)
    db['password'] = decrypt(message, cipher).decode('utf-8')
    
    return db


def fetch_data(query):
    params = config()

    connection = pg.connect(**params)
    cursor = connection.cursor()

    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()
    connection.close()

    return record


def matches_played_per_year_sql(table='matches'):
    matches_played_per_year = {}

    query = """SELECT DISTINCT season, COUNT(season) 
                FROM {} 
                GROUP BY season;
            """.format(table)

    record = fetch_data(query)

    for row in record:
        matches_played_per_year[row[0]] = row[1]

    return matches_played_per_year


def matches_won_by_teams_per_year_sql(table='matches'):
    matches_won_by_teams_per_year = {}

    query = """SELECT winner, season, COUNT(season) 
                FROM {0} 
                GROUP BY winner, season 
                ORDER BY winner, season;
            """.format(table)

    record = fetch_data(query)

    for row in record:
        if row[0] not in matches_won_by_teams_per_year and row[0] is not None:
            matches_won_by_teams_per_year[row[0]] = {}
            per_year_win = matches_won_by_teams_per_year[row[0]]
            per_year_win[row[1]] = row[2]
        elif row[0] in matches_won_by_teams_per_year and row[0] is not None:
            per_year_win = matches_won_by_teams_per_year[row[0]]
            per_year_win[row[1]] = row[2]

    return matches_won_by_teams_per_year


def extra_runs_conceded_per_team_2016_sql(table1='matches', table2='deliveries'):
    extra_runs_conceded_per_team = {}

    query = """SELECT bowling_team, SUM(extra_runs) 
                FROM {1} 
                WHERE match_id 
                IN (SELECT id 
                    FROM {0} 
                    WHERE season = 2016
                    ) 
                GROUP BY bowling_team;
            """.format(table1, table2)

    record = fetch_data(query)

    for row in record:
        extra_runs_conceded_per_team[row[0]] = row[1]

    return extra_runs_conceded_per_team


def top_economical_bowlers_2015_sql(table1='matches', table2='deliveries'):
    top_economical_bowlers = {}

    query = """WITH total_runs AS(
                    SELECT bowler, (SUM(total_runs) - SUM(bye_runs) - SUM(legbye_runs)) AS runs
                    FROM {1} 
                        JOIN {0} ON {0}.id = {1}.match_id 
                    WHERE season = 2015 AND is_super_over = FALSE
                    GROUP BY bowler
                    ORDER BY bowler
                    ),
                    total_balls AS(
                        SELECT bowler, COUNT(ball) AS balls
                        FROM {1} 
                            JOIN {0} ON {0}.id = {1}.match_id 
                        WHERE season = 2015 AND is_super_over = FALSE AND noball_runs = 0 AND wide_runs = 0
                        GROUP BY bowler
                        ORDER BY bowler
                    )
                SELECT total_runs.bowler, TRUNC(((runs * 6.0)/balls), 2) AS economy 
                FROM total_runs 
                JOIN total_balls ON total_runs.bowler = total_balls.bowler 
                ORDER BY economy 
                LIMIT 10;
            """.format(table1, table2)

    record = fetch_data(query)

    for row in record:
        top_economical_bowlers[row[0]] = float(row[1])

    return top_economical_bowlers


def matches_won_after_toss_decision(table='matches'):
    matches_won_after_toss = {}

    query = """WITH won_over_bat AS(
                    SELECT season, COUNT(season) AS won_over_bat_count
                    FROM {0}
                    WHERE toss_decision = 'bat' AND toss_winner = winner
                    GROUP BY season
                    ORDER BY season
                    ),
                    won_over_field AS(
                        SELECT season, COUNT(season) AS won_over_field_count
                        FROM {0}
                        WHERE toss_decision = 'field' AND toss_winner = winner
                        GROUP BY season
                        ORDER BY season
                    )
                SELECT won_over_bat.season, won_over_bat.won_over_bat_count, won_over_field.won_over_field_count
                FROM won_over_bat
                JOIN won_over_field ON won_over_bat.season = won_over_field.season ;
            """.format(table)

    record = fetch_data(query)

    for row in record:
        matches_won_after_toss[row[0]] = {'bat': row[1], 'field': row[2]}

    return matches_won_after_toss
