Horriblegrabber
===============

A ~~small~~ horrible script meant for downloading ~~ongoing~~ horrible anime.

This script rips the magnet link out of HorribleSubs' RRS feed and blabs it into the browser. Luckily that browser just so happens to ~~usually~~ redirect it to your torrent client :ok_hand:.

Plus it also makes a `hist` file for keeping track of which magnets have been downloaded already.

## Usage
Put a file named `tasklist.json` in the same directory as the `horriblegrabber.py` containing a list of animes like in the following example:
```json
{
    "animes" : [
        "Boku no Hero Academia",
        "Date a Live",
        "Qualidea Code"
    ]
}
```

It can only rip items that are in their RSS feed, meaning not everything from HorribleSubs can be added instantaneously.

## Requirements
* [feedparser](https://pypi.python.org/pypi/feedparser)

## License
[Apache 2.0 license](LICENSE)

## Anime or Animes
[Wiktionary says both is ok so gfy](https://en.wiktionary.org/wiki/anime#Noun)

[![](http://www.reactiongifs.com/r/bth.gif)](https://en.wiktionary.org/wiki/anime#Noun)