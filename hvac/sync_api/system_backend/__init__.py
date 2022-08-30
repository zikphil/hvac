"""Collection of Vault system backend API endpoint classes."""
import logging

from hvac.sync_api.system_backend.audit import Audit
from hvac.sync_api.system_backend.auth import Auth
from hvac.sync_api.system_backend.capabilities import Capabilities
from hvac.sync_api.system_backend.health import Health
from hvac.sync_api.system_backend.init import Init
from hvac.sync_api.system_backend.key import Key
from hvac.sync_api.system_backend.leader import Leader
from hvac.sync_api.system_backend.lease import Lease
from hvac.sync_api.system_backend.mount import Mount
from hvac.sync_api.system_backend.namespace import Namespace
from hvac.sync_api.system_backend.policy import Policy
from hvac.sync_api.system_backend.raft import Raft
from hvac.sync_api.system_backend.seal import Seal
from hvac.sync_api.system_backend.wrapping import Wrapping
from hvac.sync_api.system_backend.system_backend_mixin import SystemBackendMixin
from hvac.sync_api.vault_api_category import VaultApiCategory

__all__ = (
    "Audit",
    "Auth",
    "Capabilities",
    "Health",
    "Init",
    "Key",
    "Leader",
    "Lease",
    "Mount",
    "Namespace",
    "Policy",
    "Raft",
    "Seal",
    "SystemBackend",
    "SystemBackendMixin",
    "Wrapping",
)


logger = logging.getLogger(__name__)


class SystemBackend(
    VaultApiCategory,
    Audit,
    Auth,
    Capabilities,
    Health,
    Init,
    Key,
    Leader,
    Lease,
    Mount,
    Namespace,
    Policy,
    Raft,
    Seal,
    Wrapping,
):
    implemented_classes = [
        Audit,
        Auth,
        Capabilities,
        Health,
        Init,
        Key,
        Leader,
        Lease,
        Mount,
        Namespace,
        Policy,
        Raft,
        Seal,
        Wrapping,
    ]
    unimplemented_classes = []

    def __init__(self, adapter):
        self._adapter = adapter

    def __getattr__(self, item):
        raise AttributeError
