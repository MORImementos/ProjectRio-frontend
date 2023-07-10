import { z } from "zod"

export const schema = z.object({
  "/api_key/register/": z.object({ Username: z.string() }),
  "/api_key/reset/": z.object({ Email: z.string() }),
  "/community/create": z.object({
    global_link: z.string(),
    desc: z.string(),
    community_name: z.string(),
    type: z.string(),
    private: z.string()
  }),
  "/community/join/<comm_name>": z.object({}),
  "/community/join/<comm_name>/<active_url>": z.object({}),
  "/community/join": z.object({ community_name: z.string(), URL: z.string() }),
  "/community/invite": z.object({
    community_name: z.string(),
    invite_list: z.array(z.unknown())
  }),
  "/community/manage": z.object({
    community_name: z.string(),
    user_list: z.array(z.unknown())
  }),
  "/community/sponsor": z.object({
    action: z.string(),
    community_name: z.string()
  }),
  "/community/key": z.object({
    action: z.string(),
    community_name: z.string()
  }),
  "/community/update": z.object({
    name: z.string(),
    community_id: z.number(),
    active_tag_set_limit: z.string(),
    desc: z.string(),
    type: z.string(),
    private: z.string(),
    link: z.string()
  }),
  "/db_to_sqlite/": z.object({ ADMIN_KEY: z.string() }),
  "/init_db/": z.object({ ADMIN_KEY: z.string() }),
  "/wipe_db/": z.object({ ADMIN_KEY: z.string() }),
  "/delete_game/": z.object({ game_id: z.number() }),
  "/populate_db/ongoing_game/": z.object({
    "Away Captain": z.string(),
    "Home Roster 4 CharID": z.string(),
    "Away Roster 3 CharID": z.string(),
    "Away Roster 8 CharID": z.string(),
    "Home Roster 7 CharID": z.string(),
    "Home Roster 8 CharID": z.string(),
    "Away Roster 5 CharID": z.string(),
    "Home Roster 5 CharID": z.string(),
    Outs: z.string(),
    "Runner 3B": z.string(),
    "Runner 2B": z.string(),
    "Away Roster 7 CharID": z.string(),
    "Away Stars": z.string(),
    "Away Roster 1 CharID": z.string(),
    GameID: z.string(),
    "Away Roster 6 CharID": z.string(),
    "Home Roster 6 CharID": z.string(),
    "Home Player": z.string(),
    "Home Stars": z.string(),
    TagSetID: z.string(),
    Pitcher: z.string(),
    Inning: z.string(),
    "Runner 1B": z.string(),
    "Home Roster 2 CharID": z.string(),
    "Away Score": z.string(),
    "Home Roster 0 CharID": z.string(),
    "Half Inning": z.string(),
    "Home Score": z.string(),
    "Home Roster 3 CharID": z.string(),
    "Home Roster 1 CharID": z.string(),
    "Date - Start": z.string(),
    StadiumID: z.string(),
    Batter: z.string(),
    "Away Roster 0 CharID": z.string(),
    "Away Roster 2 CharID": z.string(),
    "Away Roster 4 CharID": z.string(),
    "Home Captain": z.string(),
    "Away Player": z.string()
  }),
  "/ongoing_game/prune": z.object({ seconds: z.string() }),
  "/populate_db/": z.object({
    StadiumID: z.string(),
    "Innings Played": z.string(),
    "Average Ping": z.string(),
    "Lag Spikes": z.string(),
    "Date - End": z.string(),
    "Character Game Stats": z.string(),
    "Home Score": z.string(),
    "Away Score": z.string(),
    "Quitter Team": z.string(),
    "Innings Selected": z.string(),
    GameID: z.string(),
    Netplay: z.string(),
    Version: z.string(),
    Events: z.string(),
    "Date - Start": z.string(),
    "Away Player": z.string(),
    "Home Player": z.string(),
    TagSetID: z.string()
  }),
  "/manual_submit_game/": z.object({
    loser_score: z.string(),
    tag_set: z.string(),
    loser_username: z.string(),
    game_id_hex: z.number(),
    date: z.string(),
    submitter_rio_key: z.string(),
    winner_score: z.string(),
    winner_username: z.string(),
    game_id_dec: z.number()
  }),
  "/update_game_status/": z.object({
    game_id: z.number(),
    game_history_id: z.number()
  }),
  "/recalc_elo/": z.object({ tag_set_id: z.number() }),
  "/submit_reverification/": z.object({
    Username: z.string(),
    Password: z.string(),
    "Rio Key": z.string(),
    Email: z.string()
  }),
  "/gen_woba_data/": z.object({}),
  "/tag/create": z.object({
    name: z.string(),
    Desc: z.string(),
    community_name: z.string(),
    desc: z.string(),
    type: z.string(),
    Code: z.string()
  }),
  "/tag/update": z.object({
    name: z.string(),
    gecko_code_desc: z.string(),
    desc: z.string(),
    type: z.string(),
    tag_id: z.number(),
    gecko_code: z.string()
  }),
  "/tag/list": z.object({
    Communities: z.string(),
    Client: z.string(),
    Types: z.string()
  }),
  "/tag_set/create": z.object({
    name: z.string(),
    start_date: z.string(),
    end_date: z.string(),
    community_name: z.string(),
    desc: z.string(),
    type: z.string(),
    tags: z.string(),
    tag_set_id: z.number()
  }),
  "/tag_set/list": z.object({
    Communities: z.string(),
    Key: z.string(),
    Active: z.string(),
    Client: z.string()
  }),
  "/tag_set/update": z.object({
    name: z.string(),
    start_date: z.string(),
    end_date: z.string(),
    desc: z.string(),
    type: z.string(),
    tag_set_id: z.number(),
    tag_ids: z.number()
  }),
  "/tag_set/ladder": z.object({}),
  "/tag_set/ladder/": z.object({ TagSet: z.string() }),
  "/register/": z.object({
    Username: z.string(),
    Password: z.string(),
    Email: z.string()
  }),
  "/verify_email/<active_url>": z.object({}),
  "/request_password_change/": z.object({ username_or_email: z.string() }),
  "/change_password/": z.object({
    password: z.string(),
    active_url: z.string()
  }),
  "/login/": z.object({ Password: z.string(), Email: z.string() }),
  "/set_privacy/": z.object({}),
  "/user/prune": z.object({}),
  "/user_group/create": z.object({
    daily_limit: z.string(),
    weekly_limit: z.string(),
    group_name: z.string(),
    sponsor_limit: z.string()
  }),
  "/user_group/add_user": z.object({
    ADMIN_KEY: z.string(),
    username: z.string(),
    group_name: z.string()
  }),
  "/patreon/refresh/": z.object({}),
  "/patreon/list": z.object({}),
  "/user_group/add_all_users": z.object({ group_name: z.string() })
})
