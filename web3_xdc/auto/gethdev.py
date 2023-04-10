from web3_xdc import (
    IPCProvider,
    Web3,
)
from web3_xdc.middleware import (
    geth_poa_middleware,
)
from web3_xdc.providers.ipc import (
    get_dev_ipc_path,
)

w3 = Web3(IPCProvider(get_dev_ipc_path()))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
