from web3_xdc import Web3
from web3_xdc.providers.auto import (
    load_provider_from_uri,
)

from .endpoints import (
    INFURA_SEPOLIA_DOMAIN,
    build_http_headers,
    build_infura_url,
)

_headers = build_http_headers()
_infura_url = build_infura_url(INFURA_SEPOLIA_DOMAIN)

w3 = Web3(load_provider_from_uri(_infura_url, _headers))
