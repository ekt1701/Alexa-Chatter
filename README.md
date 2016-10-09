# Alexa-Rivescript-Chatbot

This chatbot based on Rivescript https://www.rivescript.com/ is easier to modify and extend than AIML.  The chatbot has persistence, so it can remember things such as your name or age, tell a knock knock joke, keep track in a RPG game.

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
