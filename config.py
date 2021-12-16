
# Enter the following two as environment variables and ignore them here
APCA_API_KEY_ID=<key_id>
APCA_API_SECRET_KEY=<secret_key> 

# The following can work within your program you can ignore the two lines above
APCA_API_BASE_URL="https://api.alpaca.markets" 
APCA_API_PAPER_URL="https://paper-api/alpaca.markets"
APCA_API_DATA_URL="https://data.alpaca.markets"
APCA_RETRY_MAX=3 #The number of subsequent API calls to retry on timeouts
APCA_RETRY_WAIT=3 #seconds to wait between each retry attempt
APCA_RETRY_CODES=429,504    #429,504	comma-separated HTTP status code for which retry is attempted
#DATA_PROXY_WS   #When using the alpaca-proxy-agent you need to set this environment variable as described here
