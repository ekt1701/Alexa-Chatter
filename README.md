# Alexa-Chatter

This is a work in progress project.

Chatter is a programmable assistant that can get information from a number of sources. for example, weather, traffic APIs, rss feeds and more.  The brains behind Chatter is Rivescript a simple scripting language for chatbots.  Chatter uses Alexa Skills Kit catch all custom slot to capture what the users says, then Rivescript parses the utterances to the appropriate response.

Currently, Chatter can access the following APIs:

Adsbexchange - Interesting flights https://public-api.adsbexchange.com

Airnow http://www.airnowapi.org Requires API key

Cat Facts http://catfacts-api.appspot.com

DarkSky https://api.darksky.net Requires API key

Fixer.io - Foreign exchange rates http://api.fixer.io

Forismatic - Inspiring expressions http://api.forismatic.com

Google Maps https://maps.googleapis.com Requires API key

Mapquest http://www.mapquestapi.com/geocoding Requires API key

Moon API - Current status of moon http://api.burningsoul.in/moon

Oblique Strategies http://brianeno.needsyourhelp.org

Open Weather Map http://api.openweathermap.org Requires API key

People in Space http://api.open-notify.org

Random Jokes http://tambal.azurewebsites.net/joke/random

Space Launches https://launchlibrary.net/

The Open Movie Database http://www.omdbapi.com

The Internet Chuck Norris Database http://api.icndb.com/jokes/random

U.S. Geological Survey - Earthquakes http://earthquake.usgs.gov/fdsnws/event/1/

Weather Underground http://api.wunderground.com/ Requires API key


Chatter can search using these sites:

Duck Duck Go https://duckduckgo.com/

Open Movie Database http://www.omdbapi.com/

Rhyming Dictionary http://rhymebrain.com

Thesaurus http://words.bighugelabs.com Requires API key

Wikipedia https://www.wikipedia.org/

Wolfram Alpha http://api.wolframalpha.com Requires API key

WordNet - Definition http://chriscargile.com/dictionary/json/

Chatter can access common rss or xml feeds, google alerts and reddit topics.
RSS feeds for CNN, Reuters, Wall Street Journal, New York Times, Science Daily, NASA, CNET, Crunch Gear, Gadget Flow and more.

Daily feeds for quote of the day, word of the day, history of the day, what happened on this day

Google Alerts for Amazon Echo, Google Home and Chatbots.

Random Reddit Topics such as artificial, chatbots, Futurology, science, space, technology

Chatter can also go over your checklist, get your to do list and calendar events, either from a cvs file or a rss feed from 30boxes.com. 

You can also ask for a joke, riddle, random quote, random fact, imponderables or life's mysteries.

There are also some simple games written in Rivescript, such as a RPG demo, word game (madlibs), memory and math game. These games demonstrate what's possible.

To get started, say help me or what can I say, to get a basic list of the things you can say to Chatter.  Of course, since Chatter is a chatbot, you can also chat, though, currently the interactions are limited.

To debug the interactions, if there is something Chatter does not understand, it will say: "I have no response for " and repeat what you said.

All the code which runs Chatter is found in the brain directory.  You can easily change the wording of the commands, add other rss feeds or add functions.  With Rivescript, Chatter is easy to customize for your own use.

Instructions:

Copy the source_files.zip and upload to AWS Lambda. Note: I could not upload all the necessary files into the src directory, I kept getting an error,that is why I included the zip file.

The configuration is Runtime: Python 2.7, Handler: index.lambda_handler, Existing Role: lambda_basic_execution. In the Advanced settings, set the timeout to 50 seconds.

In the Amazon Developer Console, use the files from the speechAssets folder and make a custom slot named CHATTER and fill the slots with random words and phrases.

For the todo list, calendar, stocks and more you will need to host the startup.csv file somewhere. Personally, I saved the csv file to DropBox, which can easily be edited with a text editor. (Note when you get the link from DropBox change ?dl=0 to ?raw=1)  Currently, Chatter is using the startup.csv file from https://raw.githubusercontent.com/ekt1701/Alexa-Chatter/master/data/startup.csv

If you are interested in learning how to code Rivescript, look at this tutorial: https://www.rivescript.com/docs/tutorial
