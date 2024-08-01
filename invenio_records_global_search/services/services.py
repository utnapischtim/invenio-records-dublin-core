# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2024 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Global Search Services."""

from flask_principal import Identity
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_records_resources.services import LinksTemplate, RecordService
from invenio_records_resources.services.records.results import RecordItem
from invenio_records_resources.services.uow import UnitOfWork, unit_of_work
from invenio_search.engine import dsl


class GlobalSearchRecordService(RecordService):
    """Global search record service."""

    @unit_of_work()
    def create_or_update(
        self,
        identity: Identity,
        data: dict,
        uow: UnitOfWork | None = None,
        *,
        expand: bool = False,
    ) -> RecordItem:
        """Create a record.

        :param identity: Identity of user creating the record.
        :param data: Input data according to the data schema.
        """
        gs_pid = "gs-" + data["original"]["pid"]

        try:
            # only to check if a exists already
            self.record_cls.pid.resolve(gs_pid)

            return self.update(identity, id_=gs_pid, data=data)
        except PIDDoesNotExistError:
            self.record_cls.gs_pid = gs_pid
            return self._create(self.record_cls, identity, data, uow=uow, expand=expand)


class GlobalSearchCommunityRecordService(RecordService):
    """Global search community service."""

    @property
    def community_cls(self):
        """Factory for creating a community class."""
        return self.config.community_cls

    def search(
        self,
        identity,
        community_id,
        params=None,
        search_preference=None,
        extra_filter=None,
        **kwargs,
    ):
        """Search for records published in the given community."""
        self.require_permission(identity, "search")

        params = params or {}

        community_filter = dsl.Q("term", **{"parent.communities.ids": community_id})

        if extra_filter is not None:
            community_filter = community_filter & extra_filter

        search = self._search(
            "search",
            identity,
            params,
            search_preference,
            extra_filter=community_filter,
            permission_action="read",
            **kwargs,
        )

        search_result = search.execute()
        return self.result_list(
            self,
            identity,
            search_result,
            params,
            links_tpl=LinksTemplate(
                self.config.links_search_community_records,
                context={
                    "args": params,
                    "id": community_id,
                },
            ),
            links_item_tpl=self.links_item_tpl,
        )
