# Alpaca for data
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import config
import plotly.graph_objects as go
import plotly.express as px
from sys import os

# Our API keys for Alpaca
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")

from config import APCA_API_BASE_URL, APCA_API_DATA_URL, APCA_RETRY_MAX, APCA_RETRY_WAIT, APCA_RETRY_CODES

# Setup instance of alpaca api
alpaca = tradeapi.REST(API_KEY, API_SECRET)