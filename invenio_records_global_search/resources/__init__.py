# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Records module to create REST APIs."""

from .config import (
    GlobalSearchCommunityRecordResourceConfig,
    GlobalSearchRecordResourceConfig,
)
from .resources import GlobalSearchCommunityRecordResource, GlobalSearchRecordResource

__all__ = (
    "GlobalSearchRecordResource",
    "GlobalSearchRecordResourceConfig",
    "GlobalSearchCommunityRecordResource",
    "GlobalSearchCommunityRecordResourceConfig",
)
