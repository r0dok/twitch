
# -*- coding: utf-8 -*-

import logging

from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.entities.Bet import (BetSettings,
                                                           Condition,
                                                           DelayMode,
                                                           FilterCondition,
                                                           OutcomeKeys,
                                                           Strategy)
from TwitchChannelPointsMiner.classes.entities.Streamer import (
    Streamer, StreamerSettings)
from TwitchChannelPointsMiner.classes.Settings import Events, Priority
from TwitchChannelPointsMiner.classes.Telegram import Telegram
from TwitchChannelPointsMiner.logger import ColorPalette, LoggerSettings

#from colorama import Fore


twitch_miner = TwitchChannelPointsMiner(
    username="r0dok",
    password="V@@E<ZYx_88L77,",                 # If no password will be provided, the script will ask interactively
    claim_drops_startup=True,                   # If you want to auto claim all drops from Twitch inventory on the startup
    priority=[                                  # Custom priority in this case for example:
        Priority.STREAK,                        # - We want first of all to catch all watch streak from all streamers
        Priority.DROPS,                         # - When we don't have anymore watch streak to catch, wait until all drops are collected over the streamers
        Priority.ORDER                          # - When we have all of the drops claimed and no watch-streak available, use the order priority (POINTS_ASCENDING, POINTS_DESCEDING)
    ],
    logger_settings=LoggerSettings(
        save=True,                              # If you want to save logs in a file (suggested)
        console_level=logging.INFO,             # Level of logs - use logging.DEBUG for more info
        file_level=logging.DEBUG,               # Level of logs - If you think the log file it's too big, use logging.INFO
        emoji=False,                            # On Windows, we have a problem printing emoji. Set to false if you have a problem
        less=True,                              # If you think that the logs are too verbose, set this to True
        colored=True,                           # If you want to print colored text
        color_palette=ColorPalette(             # You can also create a custom palette color (for the common message).
            STREAMER_online="GREEN",            # Don't worry about lower/upper case. The script will parse all the values.
            streamer_offline="red",             # Read more in README.md
            #BET_wiN=Fore.MAGENTA               # Color allowed are: [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET].
        ),
        telegram=Telegram(                                                          # You can omit or leave None if you don't want to receive updates on Telegram
            chat_id=123456789,                                                      # Chat ID to send messages @GiveChatId
            token="123456789:shfuihreuifheuifhiu34578347",                          # Telegram API token @BotFather
            events=[Events.STREAMER_ONLINE, Events.STREAMER_OFFLINE, "BET_LOSE"],   # Only these events will be sent to the chat
            disable_notification=True,                                              # Revoke the notification (sound/vibration)
        )
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,                  # If you want to Bet / Make prediction
        follow_raid=True,                        # Follow raid to obtain more points
        claim_drops=True,                        # We can't filter rewards base on stream. Set to False for skip viewing counter increase and you will never obtain a drop reward from this script. Issue #21
        watch_streak=True,                       # If a streamer go online change the priority of streamers array and catch the watch streak. Issue #11
        #join_chat=True,                         # Join irc chat to increase watch-time
        bet=BetSettings(
            strategy=Strategy.SMART,             # Choose you strategy!
            percentage=5,                        # Place the x% of your channel points
            percentage_gap=10,                   # Gap difference between outcomesA and outcomesB (for SMART strategy)
            max_points=50000,                    # If the x percentage of your channel points is gt bet_max_points set this value
            stealth_mode=True,                   # If the calculated amount of channel points is GT the highest bet, place the highest value minus 1-2 points Issue #33
            delay_mode=DelayMode.FROM_END,       # When placing a bet, we will wait until `delay` seconds before the end of the timer
            delay=6,
            minimum_points=100000,               # Place the bet only if we have at least 100k points. Issue #113
            filter_condition=FilterCondition(
                by=OutcomeKeys.TOTAL_USERS,      # Where apply the filter. Allowed [PERCENTAGE_USERS, ODDS_PERCENTAGE, ODDS, TOP_POINTS, TOTAL_USERS, TOTAL_POINTS]
                where=Condition.LTE,             # by must be [GT, LT, GTE, LTE] than value
                value=800
            )
        )
    )
)

twitch_miner.mine(
    [
       #Favourite + quest
       "TeamLiquid",
    
       #TL+Sign  
       "oseecs",        #10k
       "acronik_",      #15k
       "yekindar",      #25k
       "nats",          #50k
       "superjamppi",   #100k
       
       #Steam sign
       "cadian",        #25k
       #"stewie2k",     #250k

       #RLCS Steam sings
       "monkeym00n",    #25k
       "yukeo",         #25k
       "itsjstn",       #30k
       "thanovic",      #30k
       "chicago",       #30k
       "arsenal",       #40k
       #"rizzo",         #75k
       #"forky",         #80k
       "fairypeak",     #100k
       #"kaydop",       #150k
       
       #TL+
       "sliggytv",
       "areliann",
       "raxin",
       "wardiii",
       "tiffae",
       "rubenderonde",
       "riddlesmk",
       "Bwipolol",
       "hungrybox",

       #Steam sign
       "fangcsgo",      #25k
       #"dimaoneshot"   #100k
       
       #TL   
       "pulgaboy",
       "Mendo",
       "Hanssama",
       "RubenDeRonde",
       "Harmii",
       "zai",
       "72hrs",
       "Kaymind",
       "AKAWonder",
       "MATUMBAMAN",
       "vivid",
       "LiquidHasuObs",
       "razah",
       "naxysz",
       "scoped",
       "qojqva",
       "pulgaboy",
       "resetzR6",
       "LiquidBunny",
       "LiquidSnute",
       "LiquidKen",
       "Savjz",
       "chillindude",
       "DaHanG",
       "nurok",
       "midbeast",
       "drnpaola",
       "paluhh",
       "Hungrybox",
       "BananaSlamJamma",
       "bjergsenlol",
       "SunBaconRelaxer",
       "Kaymind",
       "midbeast",
       "RedBeard",
       "Slysssa",
       "naguura"
    ],                                
    followers=False                                             # Array of streamers (order = priority)
    # Automatic download the list of your followers (unable to set custom settings for you followers list)
)
