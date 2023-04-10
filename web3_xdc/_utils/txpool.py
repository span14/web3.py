from typing import (
    Callable,
)

from web3_xdc._utils.rpc_abi import (
    RPC,
)
from web3_xdc.method import (
    Method,
)
from web3_xdc.types import (
    TxPoolContent,
    TxPoolInspect,
    TxPoolStatus,
)

content: Method[Callable[[], TxPoolContent]] = Method(
    RPC.txpool_content,
    mungers=None,
)


inspect: Method[Callable[[], TxPoolInspect]] = Method(
    RPC.txpool_inspect,
    mungers=None,
)


status: Method[Callable[[], TxPoolStatus]] = Method(
    RPC.txpool_status,
    mungers=None,
)
