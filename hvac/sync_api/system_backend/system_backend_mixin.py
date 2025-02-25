#!/usr/bin/env python
import logging
from abc import ABCMeta

from hvac.sync_api.vault_api_base import VaultApiBase

logger = logging.getLogger(__name__)


class SystemBackendMixin(VaultApiBase):
    """Base class for System Backend API endpoints."""

    __metaclass__ = ABCMeta
