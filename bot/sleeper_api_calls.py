from sleeper_wrapper import League, Stats, Players
import datetime


def format_name(name):
    """
    Formats team names to only be 10 chars long to look nicely in the messages
    :param name: team name to be formatted
    :return: formatted string
    """

    # make sure team name exists
    if name is None:
        name = 'Team NA'
    # reduce name to max 8 chars for formatting
    if len(name) >= 10:
        name = name[:10]

    # make sure team name is at 8 chars for formatting
    while len(name) < 10:
        name += ' '

    return name


def current_week():
    """
    This function return current week of the league
    :return: int containing current week
    """
    # TODO: Make this more sustainable without hardcoding. I made this at 1:30 AM which is why it's hardcoded
    start_week = datetime.datetime(2021, 5, 24)
    curr_week = datetime.datetime.now()
    week = int(curr_week.strftime("%W")) - int(start_week.strftime("%W"))

    return week


def weekly_matchups(league_id, week):
    """
    Finds the scores for each specific week and league
    :param league_id: league id for league in Sleeper App
    :param week: week to find scores of
    :return: dictionary of (int) matchup id: (tuple of floats) scores
    """
    league = League(league_id)
    matchups = league.get_matchups(week)
    users = league.get_users()
    rosters = league.get_rosters()

    # THIS SHOULD BE UPDATED TO RETURN POINTS IF THE API GETS UPDATED
    return league.get_scoreboards(rosters, matchups, users, 'pts_ppr', week)


def get_standings(league_id):
    """
    Accepts a league id as a parameter and returns the currents standings for the league
    :param league_id: id of the league the user is in in the Sleeper App
    :return: string containing the current standings of the league
    """
    # get standings of the league from the API
    league = League(league_id)
    rosters = league.get_rosters()
    users = league.get_users()
    standings = league.get_standings(rosters, users)

    # backticks wrap the string for code block so that each char in font has the same width
    # used for better formatting
    standings_str = '```\n'
    spot = 1
    for team in standings:
        # unpack scoreboard
        name = team[0]
        wins = team[1]
        ties = team[2]
        losses = team[3]

        name = format_name(name)

        # create entry and add it to the table
        standings_entry = "| {} | {} | {} | {} | {} |\n".format(spot, name, wins, ties, losses)
        standings_str += standings_entry

        # increment spot
        spot += 1

    standings_str += '```'
    return standings_str

    return "standings"


def get_current_matchups(league_id):
    """
    Accepts a league id as a parameter and returns the current scores of each matchup in the league
    :param league_id: id of the league the user is in in the Sleeper App
    :return: string containing the scores of each matchup
    """
    week = current_week()
    matchups = weekly_matchups(league_id, week)

    # backticks added for formatting so every char is same width
    matchups_str = '```\n'
    game = 1
    for match in matchups.values():
        team0 = match[0]
        team1 = match[1]

        team0_name = team0[0]
        team1_name = team1[0]

        team0_name = format_name(team0_name)
        team1_name = format_name(team1_name)

        matchup_entry = "| {} | VS | {} |\n".format(team0_name, team1_name)
        matchups_str += matchup_entry

    matchups_str += '```'
    return matchups_str
