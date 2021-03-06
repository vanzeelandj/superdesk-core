# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


import logging
import superdesk

from .validators import ValidatorsService, ValidatorsResource

logger = logging.getLogger(__name__)


def init_app(app) -> None:
    endpoint_name = "validators"
    service = ValidatorsService(endpoint_name, backend=superdesk.get_backend())
    ValidatorsResource(endpoint_name, app=app, service=service)
