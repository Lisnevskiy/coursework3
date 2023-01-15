from flask import Flask, send_from_directory, render_template, request

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, get_posts_by_user, search_for_posts

from api.views import api_blueprint


app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def get_post_by_post_id(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    if comments == 'ValueError':
        return 'Нет такого поста'
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@app.route('/search')
def get_posts_by_word():
    s = request.args['s']
    posts = search_for_posts(s)
    posts_count = len(posts)
    return render_template('search.html', posts=posts, posts_count=posts_count)


@app.route('/user/<username>')
def get_post_by_username(username):
    posts = get_posts_by_user(username)
    if posts == 'ValueError':
        return 'Нет такого пользователя'
    return render_template('user-feed.html', posts=posts, username=username)


if __name__ == '__main__':
    app.run(debug=True)
