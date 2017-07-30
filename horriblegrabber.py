import feedparser
import json
import os
import sys
import webbrowser

HISTORY_FILE = "hist"
URL = "http://horriblesubs.info/rss.php?res=720"


def update_history(anime_name, link):
    if not os.path.isfile(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            f.write("{}")
    with open(HISTORY_FILE, "r+") as f:
        data = json.load(f)
        if anime_name in data:
            new_data = data[anime_name]
        else:
            new_data = []
        new_data.append(link)
        data[anime_name] = new_data
        f.seek(0)
        f.write(json.dumps(data, indent=4, sort_keys=True))
        f.write("\n")
        f.truncate()


def read_history(animes):
    if os.path.isfile(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            try:
                contents = json.load(f)
            except json.decoder.JSONDecodeError:
                print("history file '{}' broken, "
                      "will download all listed videos".format(HISTORY_FILE))
                os.remove(HISTORY_FILE)
                return {}
            history_dict = {}
            for a in animes:
                try:
                    history_dict[a] = contents[a]
                except KeyError:
                    pass
            return history_dict
    return {}

if __name__ == '__main__':
    feed = feedparser.parse(URL)
    feed_anime = feed["items"]
    anime_list = []

    if not os.path.isfile('tasklist.json'):
        print('Missing tasklist.json :( See README.md for details')
        sys.exit(1)

    with open('tasklist.json') as anime_list_file:
        try:
            anime_list_feed = json.load(anime_list_file)
        except json.decode.JSONDecodeError:
            print('Please provide valid JSON')
            sys.exit(3)
        if not 'animes' in anime_list_feed:
            print('No anime(s) found in list :(')
            sys.exit(2)
        for listed_anime in anime_list_feed["animes"]:
            anime_list.append(listed_anime)

    history = read_history(anime_list)

    for anime in feed_anime:
        for wanted_anime in anime_list:
            if '[HorribleSubs] {} - '.format(wanted_anime) in anime['title']:
                if wanted_anime in history:
                    if anime["link"] not in history[wanted_anime]:
                        print('Found a new episode of {}'.format(wanted_anime))
                        webbrowser.open(anime["link"])
                        update_history(wanted_anime, anime["link"])
                else:
                    print('Found a new episode of {}'.format(wanted_anime))
                    webbrowser.open(anime["link"])
                    update_history(wanted_anime, anime["link"])
    
    print('I should be done by now, bye ¯\(´•ω•`)/¯')