from hummingbot.core.api_throttler.data_types import RateLimit

EXCHANGE_NAME = "mexc_perpetual"

DOMAIN = EXCHANGE_NAME
PERPETUAL_BASE_URL = "https://contract.mexc.com/"
PERPETUAL_WS_URL = "wss://contract.mexc.com/ws/"

# Public endpoints
SERVER_TIME_PATH_URL = "api/v1/contract/ping"
CONTRACT_INFO_URL = "api/v1/contract/detail"
CONTRACT_INDEX_PRICE_URL = "api/v1/contract/index_price"


# Rate Limit Type
REQUEST_WEIGHT = "REQUEST_WEIGHT"
ORDERS_1MIN = "ORDERS_1MIN"
ORDERS_1SEC = "ORDERS_1SEC"

# Rate Limit time intervals
ONE_DAY = 86400
ONE_HOUR = 3600
ONE_MINUTE = 60
ONE_SECOND = 1

RATE_LIMITS = [
    RateLimit(limit_id=SERVER_TIME_PATH_URL, limit=20, time_interval=ONE_SECOND * 2),
    RateLimit(limit_id=CONTRACT_INFO_URL, limit=1, time_interval=ONE_SECOND * 5),
]
