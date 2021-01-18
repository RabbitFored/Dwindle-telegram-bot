if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)

# Create a new config.py file in same dir and import, then extend this class.

TOKEN = "" # Your bot Token here
Webhook = "" #webhook url here.(Ex: https://dwindle.heroku.app.If you are using heroku get using the format - https://{your heroku app name here}.herokuapp.com/)
GpApi = "" #Get this at https://bitly.is/accesstoken
GpBase = " https://gplinks.in/api?api={}&url=".format(GpApi)
bitlyapi = "" #Get this at https://bitly.is/accesstoken
bitlybase = "https://api-ssl.bitly.com/v3/shorten?access_token={}&uri=".format(bitlyapi)
