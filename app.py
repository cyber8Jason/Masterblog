from flask import Flask, render_template, request, redirect, url_for
from blog_posts_storage import load_blog_posts, save_blog_posts


# This is a simple Flask application that serves job posts from a JSON file.
app = Flask(__name__)


@app.route('/')
def index():
    """ Render the index page with a list of blog posts."""
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = load_blog_posts()
        new_post = {
            'id': max(post['id'] for post in blog_posts) + 1 if blog_posts else 1,
            'author': request.form.get('author'),
            'title': request.form.get('title'),
            'content': request.form.get('content'),
            'likes': 0  # Initialisiere likes mit 0
        }
        blog_posts.append(new_post)
        save_blog_posts(blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    blog_posts = load_blog_posts()
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    save_blog_posts(blog_posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog_posts = load_blog_posts()
    post = next((post for post in blog_posts if post['id'] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post
        post['title'] = request.form.get('title')
        post['author'] = request.form.get('author')
        post['content'] = request.form.get('content')

        # Save the updated posts
        save_blog_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/like/<int:post_id>', methods=['GET'])
def like(post_id):
    blog_posts = load_blog_posts()
    post = next((post for post in blog_posts if post['id'] == post_id), None)

    if post is not None:
        post['likes'] = post.get('likes', 0) + 1
        save_blog_posts(blog_posts)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)