import logging

from flask import Blueprint, jsonify

from coursework2_source.utils import get_posts_all, get_post_by_pk


api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename='logs/api.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')


@api_blueprint.route('/api/posts')
def get_api_posts_json():
    logging.info('Запрос /api/posts')
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/post/<int:post_id>')
def get_api_post_json(post_id):
    logging.info('Запрос /api/posts')
    post = get_post_by_pk(post_id)
    return jsonify(post)
