from typing import (
    TYPE_CHECKING,
)

from web3_xdc._utils.normalizers import (
    abi_ens_resolver,
)
from web3_xdc._utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)
from web3_xdc.types import (
    Middleware,
)

from .formatting import (
    construct_formatting_middleware,
)

if TYPE_CHECKING:
    from web3_xdc import Web3  # noqa: F401


def name_to_address_middleware(w3: "Web3") -> Middleware:
    normalizers = [
        abi_ens_resolver(w3),
    ]
    return construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )
