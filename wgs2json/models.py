import dataclasses
from typing import List


@dataclasses.dataclass
class WgPeer:
    peer: str
    allowed_ips: List[str]
    preshared_key: str
    endpoint: str = None
    latest_handshake: str = None
    persistent_keepalive: str = None
    transfer: str = None

    def __repr__(self):
        return json.dumps(self.__dict__)


@dataclasses.dataclass
class WgInterface:
    interface: str
    listening_port: str
    private_key: str
    public_key: str
    peers: List[WgPeer] = dataclasses.field(default_factory=[])

    def __repr__(self):
        return json.dumps(self.__dict__)
