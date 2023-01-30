from web3_xdc._utils.method_formatters import (
    PYTHONIC_REQUEST_FORMATTERS,
    PYTHONIC_RESULT_FORMATTERS,
)
from web3_xdc.middleware.formatting import (
    construct_formatting_middleware,
)

pythonic_middleware = construct_formatting_middleware(
    request_formatters=PYTHONIC_REQUEST_FORMATTERS,
    result_formatters=PYTHONIC_RESULT_FORMATTERS,
)
