if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)

# Create a new config.py file in same dir and import, then extend this class.
    # REQUIRED
  TOKEN = "" # Your bot Token here
    #Recommended
  Webhook = False #Set Webhook
  PORT = 8443 # Ports currently supported for Webhooks: 443, 80, 88, 8443.

  bitlyapi = "" #Get this at https://bitly.is/accesstoken

