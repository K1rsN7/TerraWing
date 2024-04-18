from typing import Dict
from uuid import UUID

from aiortc import RTCPeerConnection


class DroneConnections:
    def __init__(self):
        self._connections: Dict[UUID, RTCPeerConnection] = {}

    def __getitem__(self, drone_id: UUID) -> RTCPeerConnection:
        return self._connections[drone_id]

    def __setitem__(self, drone_id: UUID, connection: RTCPeerConnection):
        self._connections[drone_id] = connection

    def __delitem__(self, drone_id: UUID):
        if drone_id in self._connections:
            del self._connections[drone_id]
