# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Components."""


from invenio_records_resources.services.records.components import MetadataComponent

from .original import OriginalComponent
from .parent import ParentComponent

DefaultRecordsComponents = [
    MetadataComponent,
    OriginalComponent,
    ParentComponent,
]


__all__ = ("DefaultRecordsComponents",)
