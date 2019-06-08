# -*- coding: utf-8 -*-
from flask import redirect, render_template, request
from flask import g, Blueprint, flash, url_for, session
from app import logger

from app.services.api_call import ApiCall
from app.services.ssm_collect import SsmCollect

blueprint = Blueprint('tutorial', __name__, url_prefix='/tutorial')


@blueprint.route('/requesting')
def requesting():
    search = request.args.get('query', '')
    search_api = request.args.get('query_api', '')

    apicall = ApiCall()
    results1 = apicall.get('/todos')

    if len(search_api) != 0:
        results2 = apicall.get_id('/todos/', search_api)
    else:
        results2 = False

    ssm_collect = SsmCollect()
    results3 = ssm_collect.get_parameters(search)

    #logger.log(results1)
    logger.log(results2)
    #logger.log(results3)

    return render_template('tutorial/requesting.html',
        tutorial1 = results1[:5],
        tutorial2 = results2,
        tutorial3=results3,
        query = search,
    )

