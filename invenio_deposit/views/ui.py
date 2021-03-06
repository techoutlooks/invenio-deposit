# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Deposit UI."""

from __future__ import absolute_import, print_function

from functools import partial

from flask import Blueprint, abort, current_app, render_template, request, \
    url_for
from flask_login import current_user, login_required
from invenio_db import db


def create_blueprint(endpoints):
    """Create Invenio-Deposit-UI blueprint."""
    from invenio_records_ui.views import create_url_rule

    blueprint = Blueprint(
        'invenio_deposit_ui',
        __name__,
        static_folder='../static',
        template_folder='../templates',
        url_prefix='',
    )

    for endpoint, options in (endpoints or {}).items():
        blueprint.add_url_rule(**create_url_rule(endpoint, **options))

    @blueprint.route('/deposit')
    @login_required
    def index():
        """List user deposits."""
        return render_template(
            'invenio_deposit/index.html',
        )

    @blueprint.route('/deposit/new')
    @login_required
    def new():
        """Create new deposit."""
        return render_template(
            'invenio_deposit/edit.html', record={'_deposit': {'id': None}},
        )

    return blueprint
