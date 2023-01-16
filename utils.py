import json


def get_posts_all():
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_comments_all():
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(poster_name):
    posts = get_posts_all()
    posts_by_user = []
    for post in posts:
        if poster_name.lower() == post['poster_name']:
            posts_by_user.append(post)
    if len(posts_by_user) == 0:
        return 'ValueError'
    return posts_by_user


def get_comments_by_post_id(post_id):
    comments = get_comments_all()
    comments_by_post = []
    posts = get_posts_all()
    if post_id not in range(1, len(posts) + 1):
        return 'ValueError'
    for comment in comments:
        if post_id == comment['post_id']:
            comments_by_post.append(comment)
    return comments_by_post


def search_for_posts(query):
    posts = get_posts_all()
    posts_by_query = []
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_by_query.append(post)
    return posts_by_query


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if pk == post['pk']:
            return post
