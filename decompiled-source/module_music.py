from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
	("molda_music_stop", "molda_music_stop.ogg", mtf_start_immediately|mtf_module_track, 0),

	("nomad_1", "nomad_1.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_2", "nomad_2.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_3", "nomad_3.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_4", "nomad_4.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_5", "nomad_5.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_6", "nomad_6.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("nomad_7", "nomad_7.ogg", mtf_start_immediately|mtf_sit_tavern|mtf_module_track, 0),

	("east_1", "east_1.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_2", "east_2.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_3", "east_3.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_4", "east_4.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_5", "east_5.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_6", "east_6.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_7", "east_7.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_8", "east_8.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("east_9", "east_9.ogg", mtf_start_immediately|mtf_sit_multiplayer_fight|mtf_module_track, 0),

	("jap_1", "jap_1.ogg", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 0),

	("jap_2", "jap_2.ogg", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 0),

	("jap_3", "jap_3.ogg", mtf_start_immediately|mtf_sit_ambushed|mtf_module_track, 0),

	("ac_1", "ac_1.ogg", mtf_start_immediately|mtf_sit_town|mtf_module_track, 0),

	("ac_2", "ac_2.ogg", mtf_start_immediately|mtf_sit_town|mtf_module_track, 0),

	("ac_3", "ac_3.ogg", mtf_start_immediately|mtf_sit_town|mtf_module_track, 0),

	("ac_4", "ac_4.ogg", mtf_start_immediately|mtf_sit_town|mtf_module_track, 0),

	("ac_5", "ac_5.ogg", mtf_start_immediately|mtf_sit_town|mtf_module_track, 0),

	("arab_1", "arab_1.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_2", "arab_2.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_3", "arab_3.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_4", "arab_4.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_5", "arab_5.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_6", "arab_6.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("arab_7", "arab_7.ogg", mtf_start_immediately|mtf_sit_town_infiltrate|mtf_module_track, 0),

	("north_1", "north_1.ogg", mtf_start_immediately|mtf_sit_travel|mtf_module_track, 0),

	("north_2", "north_2.ogg", mtf_start_immediately|mtf_sit_travel|mtf_module_track, 0),

	("north_3", "north_3.ogg", mtf_start_immediately|mtf_sit_travel|mtf_module_track, 0),

	("north_4", "north_4.ogg", mtf_start_immediately|mtf_sit_travel|mtf_module_track, 0),

	("north_5", "north_5.ogg", mtf_start_immediately|mtf_sit_travel|mtf_module_track, 0),

	("west_1", "west_1.ogg", mtf_start_immediately|mtf_sit_night|mtf_module_track, 0),

	("west_2", "west_2.ogg", mtf_start_immediately|mtf_sit_night|mtf_module_track, 0),

	("west_3", "west_3.ogg", mtf_start_immediately|mtf_sit_night|mtf_module_track, 0),

	("west_4", "west_4.ogg", mtf_start_immediately|mtf_sit_night|mtf_module_track, 0),

	("west_5", "west_5.ogg", mtf_start_immediately|mtf_sit_night|mtf_module_track, 0),

	("baba_1", "baba_1.ogg", mtf_start_immediately|mtf_sit_day|mtf_module_track, 0),

	("baba_2", "baba_2.ogg", mtf_start_immediately|mtf_sit_day|mtf_module_track, 0),

	("baba_3", "baba_3.ogg", mtf_start_immediately|mtf_sit_day|mtf_module_track, 0),

	("baba_4", "baba_4.ogg", mtf_start_immediately|mtf_sit_day|mtf_module_track, 0),

	("iber_1", "iber_1.ogg", mtf_start_immediately|mtf_sit_siege|mtf_module_track, 0),

	("iber_2", "iber_2.ogg", mtf_start_immediately|mtf_sit_siege|mtf_module_track, 0),

	("iber_3", "iber_3.ogg", mtf_start_immediately|mtf_sit_siege|mtf_module_track, 0),

	("war_1", "war_1.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_2", "war_2.ogg", mtf_start_immediately|mtf_sit_arena|mtf_module_track, 0),

	("war_3", "war_3.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_4", "war_4.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_5", "war_5.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_6", "war_6.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_7", "war_7.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_8", "war_8.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_9", "war_9.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_10", "war_10.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_11", "war_11.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_12", "war_12.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_13", "war_13.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_14", "war_14.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_15", "war_15.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_16", "war_16.ogg", mtf_start_immediately|mtf_sit_arena|mtf_module_track, 0),

	("war_17", "war_17.ogg", mtf_start_immediately|mtf_sit_fight|mtf_module_track, 0),

	("war_2", "war_2.ogg", mtf_start_immediately|mtf_sit_arena|mtf_module_track, 0),

	("war_16", "war_16.ogg", mtf_start_immediately|mtf_sit_arena|mtf_module_track, 0),

	("quest_1", "quest_1.ogg", mtf_start_immediately|mtf_module_track, 0),

	("festival_1", "festival_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("festival_2", "festival_2.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("night_1", "night_1.ogg", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),

	("night_2", "night_2.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("night_3", "night_3.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_1", "camp_1.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_2", "camp_2.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_3", "camp_3.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_4", "camp_4.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_5", "camp_5.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("camp_6", "camp_6.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("ship_1", "ship_1.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("ship_2", "ship_2.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("ship_3", "ship_3.ogg", mtf_start_immediately|mtf_sit_killed|mtf_module_track, 0),

	("sea_1", "sea_1.ogg", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 0),

	("sea_2", "sea_2.ogg", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 0),

	("sea_3", "sea_3.ogg", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 0),

	("sea_4", "sea_4.ogg", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 0),

	("sea_5", "sea_5.ogg", mtf_start_immediately|mtf_sit_victorious|mtf_module_track, 0),

	("night_1", "night_1.ogg", mtf_start_immediately|mtf_sit_main_title|mtf_module_track, 0),

	("festival_1", "festival_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("retire_1", "retire_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("love_scene", "love_scene.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	("frustrated", "frustrated.ogg", mtf_persist_until_finished|mtf_module_track, 0),

]