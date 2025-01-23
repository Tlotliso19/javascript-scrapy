from polygon import RESTClient
from polygon.rest.models import Exchange
# docs
# https://polygon.io/docs/crypto/get_v3_reference_exchanges
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-exchanges

# client = RESTClient("XXXXXX") # hardcoded api_key is used
apikey='DEQ4_lFm4uwvgpElerfhox3iFpvpgVMn'
client = RESTClient(api_key=apikey)  # POLYGON_API_KEY environment variable is used

exchanges = client.get_exchanges("future")
print(exchanges)

# loop over exchanges
for exchange in exchanges:
    # verify this is an exchange
    if isinstance(exchange, Exchange):
        # print exchange info
        print(
            "{:<15}{} ({})".format(
                exchange.asset_class, exchange.name, exchange.operating_mic
            )
        )