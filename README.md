# Alexa-Chatter

This is a work in progress project.

Chatter is a programmable assistant that can get information from a number of sources. for example, weather, traffic APIs, rss feeds and more.  The brains behind Chatter is Rivescript a simple scripting language for chatbots.  Chatter uses Alexa Skills Kit catchall custom slot to capture what the users says, then Rivescript parses the utterances to the appropriate action.

Some things you can ask are tell me a joke, tell me a story, make me think, play a game.  The chatbot can also get information from the Internet, such as get my weather, what is my to do list, get a random quote, get headline news from CNN, even "search for " using Duck Duck Go

The brain of the chatbot can be edited with a text editor, so you can personalize the bot to your liking and add more features.

There is also a tool that can convert AIML files to Rivescript files: https://github.com/aichaos/aiml2rs

Even though, my chatbot is written in Python, Rivescript can also be written in Java, JavaScript, Go and Perl.

Instructions:

Zip the contents of the src folder and upload to AWS Lambda.

The configuration is Runtime: Python 2.7, Handler: index.lambda_handler, Existing Role: lambda_basic_execution. In the Advanced settings, set the timeout to 20 seconds.

In the Amazon Developer Console, use the files from the speechAssets folder and make a custom slot named CHATTER and fill the slots with random words and phrases.

The woeid for the Yahoo Weather API, is set to my location, so you will need to change it for your location. You can find your woeid here: http://woeid.rosselliot.co.nz/

For the todo list you will need to host the csv file somewhere. Personally, I saved the csv files to DropBox, which can easily be edited with a text editor. (Note when you get the link from DropBox change ?dl=0 to ?raw=1)  The sample to do links to https://github.com/ekt1701/Alexa-Good-Morning/blob/master/todo.csv

If you are interested in learning how to code Rivescript, look at this tutorial: https://www.rivescript.com/docs/tutorial
