# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Views."""

from functools import partial

from flask import Blueprint, Flask, current_app, render_template
from invenio_search_ui.searchconfig import search_app_config


def create_blueprint(_: Flask) -> Blueprint:
    """Create Blueprint."""
    routes = {
        "record-search": "/search",
    }

    blueprint = Blueprint(
        "invenio_records_global_search",
        __name__,
        template_folder="templates",
        url_prefix="/global-search",
    )
    blueprint.add_url_rule(routes["record-search"], view_func=search)
    blueprint.app_context_processor(search_app_context)
    blueprint.app_context_processor(search_app_context_community)

    return blueprint


def search_app_context() -> dict:
    """Global search search app context."""
    return {
        "search_app_global_search_config": partial(
            search_app_config,
            "GLOBAL_SEARCH_SEARCH",
            current_app.config["GLOBAL_SEARCH_FACETS"],
            current_app.config["GLOBAL_SEARCH_SORT_OPTIONS"],
            "/api/global-search",
            {"Accept": "application/vnd.invenioglobalsearch.v1+json"},
            app_id="GlobalSearchRecords.Search",
        ),
    }


def search_app_context_community():
    """Search app context processor."""
    return {
        "search_app_communities_global_search_records_config": partial(
            search_app_config,
            config_name="GLOBAL_SEARCH_COMMUNITIES_SEARCH",
            available_facets=current_app.config["GLOBAL_SEARCH_FACETS"],
            sort_options=current_app.config["GLOBAL_SEARCH_SORT_OPTIONS"],
            headers={"Accept": "application/vnd.invenioglobalsearch.v1+json"},
            pagination_options=(10, 20),
            app_id="GlobalSearchCommunity.Search",
        ),
    }


def search() -> str:
    """Search help guide."""
    return render_template("invenio_records_global_search/search/search.html")


def create_record_bp(app: Flask) -> Blueprint:
    """Create records blueprint."""
    return app.extensions[
        "invenio-records-global-search"
    ].records_resource.as_blueprint()


def create_community_record_bp(app: Flask) -> Blueprint:
    """Create community records blueprint."""
    return app.extensions[
        "invenio-records-global-search"
    ].community_records_resource.as_blueprint()
