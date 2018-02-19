# Import flask dependencies
from flask import Blueprint, request, render_template, redirect
from flask_login import login_required
from ..webapp import database as db


# Import the database object from the main app module
from the_miner.models import Miner
from the_miner.mod_miner.helpers import getMinerID


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_miners = Blueprint('miners', __name__)

# View list and search miners


@mod_miners.route('/miners/', methods=['GET', 'POST'])
@mod_miners.route('/miners/<int:page>/', methods=['GET', 'POST'])
def miners(page=1):
    query = request.args.get('q')

    if(query is None):
        per_page = 24
        paginate = db.session.query(Miner).paginate(
            page, per_page, error_out=False)
        miner_exist = paginate.miners
    else:
        miner_exist = db.session.query(Miner).filter(
            Miner.title.ilike('%' + query + '%')).all()

    return render_template('miner.html', miners=miner_exist, pagination=paginate)

# View selected miner


@mod_miners.route('/miners/view/<id>/', methods=['GET', 'POST'])
def miners_find(id):

    miner_exist = getMinerID(id)

    return render_template('miner_view.html', miner=miner_exist)


@mod_miners.route('/miners/create/', methods=['POST'])
# @login_required
def miners_create_post():
    data = request.form
    print data

    title = data['title']
    headline = data['headline']
    description = data['description']
    url = data['url']
    primary_key = data['primary_key']
    thumbnail = ''

    try:
        miner_exist = Miner.add(title, headline, description,
                              primary_key, url, thumbnail)
        miner_id = miner_exist.insert()
        return redirect("/miners/" + miner_id)
    except Exception as e:
        print e
        return render_template('miner_create.html', error=404)


@mod_miners.route('/miners/create/', methods=['GET'])
# @login_required
def miners_create():
    print 'outpost'
    return render_template('miner_create.html')


# Delete
@mod_miners.route('/miners/<id>/delete', methods=['GET', 'POST'])
@login_required
def miners_delete(id):

    miner_exist = getMinerID(id)

    db.session.delete(miner_exist)
    db.session.commit()

    return redirect('/miners/')
