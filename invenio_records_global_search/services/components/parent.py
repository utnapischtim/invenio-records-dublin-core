# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Parent Component."""

from flask_principal import Identity
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.records.components.base import ServiceComponent


class ParentComponent(ServiceComponent):
    """Service component for metadata."""

    def create(
        self,
        _: Identity,
        data: dict | None = None,
        record: Record | None = None,
        errors: dict | None = None,  # noqa: ARG002
        **__: dict,
    ) -> None:
        """Inject parsed view to the record."""
        record.parent = data.get("parent", "")

    def update(
        self,
        _: Identity,
        data: dict | None = None,
        record: Record | None = None,
        **__: dict,
    ) -> None:
        """Inject parsed view to the record."""
        record.parent = data.get("parent", "")
