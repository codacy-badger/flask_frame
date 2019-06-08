# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from flask import g, Blueprint, flash, url_for, session
from app import logger

from app.services.apiCall import apiCall
from app.services.ssm_collect import SsmCollect

blueprint = Blueprint('tutorial', __name__, url_prefix='/tutorial')


@blueprint.route('/requesting')
def requesting():
    search = request.args.get('query', '')

    apicall = apiCall()
    results1 = apicall.get('/todos')
    results2 = apicall.get_by_id('/todos/', search)

    ssm_collect = SsmCollect()
    results3 = ssm_collect.get_parameters(search)

    logger.log(results3)
    logger.log(results2)

    return render_template('tutorial/requesting.html',
        tutorial1 = results1[:3],
        tutorial3 = results3,
        #tutorial2 = results2[:1],
        query = search,
    )

