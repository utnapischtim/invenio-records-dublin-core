# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""High-level API for working with Dublin Core records, pids, search."""

from .config import (
    GlobalSearchCommunityRecordServiceConfig,
    GlobalSearchRecordServiceConfig,
)
from .services import GlobalSearchCommunityRecordService, GlobalSearchRecordService

__all__ = (
    "GlobalSearchRecordService",
    "GlobalSearchRecordServiceConfig",
    "GlobalSearchCommunityRecordService",
    "GlobalSearchCommunityRecordServiceConfig",
)
