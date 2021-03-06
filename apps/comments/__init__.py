# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

"""Generic comments module."""

import superdesk

from .comments import CommentsService, CommentsResource, comments_schema  # noqa
from .user_mentions import on_activity_updated
from .inline_comments import handle_inline_mentions


def init_app(app) -> None:
    endpoint_name = "comments"
    service = CommentsService(endpoint_name, backend=superdesk.get_backend())
    CommentsResource(endpoint_name, app=app, service=service)

    app.on_updated_activity -= on_activity_updated
    app.on_updated_activity += on_activity_updated

    superdesk.item_update.connect(handle_inline_mentions)
