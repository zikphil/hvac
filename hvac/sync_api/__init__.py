"""Collection of Vault API endpoint classes."""
from hvac.sync_api.auth_methods import AuthMethods
from hvac.sync_api.secrets_engines import SecretsEngines
from hvac.sync_api.system_backend import SystemBackend
from hvac.sync_api.vault_api_base import VaultApiBase
from hvac.sync_api.vault_api_category import VaultApiCategory

__all__ = (
    "AuthMethods",
    "SecretsEngines",
    "SystemBackend",
    "VaultApiBase",
    "VaultApiCategory",
)
