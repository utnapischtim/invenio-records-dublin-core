# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Global Search Record Resource."""

from flask import g
from flask_resources import resource_requestctx, response_handler, route
from invenio_records_resources.resources import RecordResource
from invenio_records_resources.resources.records.resource import (
    request_search_args,
    request_view_args,
)
from invenio_records_resources.resources.records.utils import search_preference


class GlobalSearchRecordResource(RecordResource):
    """GlobalSearchRecordResource."""

    def create_url_rules(self) -> list:
        """Create url rules for record resource."""
        routes = self.config.routes

        return [
            route("GET", routes["list"], self.search),
        ]


class GlobalSearchCommunityRecordResource(RecordResource):
    """GlobalSearchCommunityRecordResource."""

    def create_url_rules(self) -> list:
        """Create url rules for record resource."""
        routes = self.config.routes

        return [
            route("GET", routes["global-communities"], self.search_communities),
        ]

    @request_search_args
    @request_view_args
    @response_handler(many=True)
    def search_communities(self, **kwargs):
        """Search communities."""
        hits = self.service.search(
            identity=g.identity,
            community_id=resource_requestctx.view_args["pid_value"],
            params=resource_requestctx.args,
            search_preference=search_preference(),
        )
        return hits.to_dict(), 200
