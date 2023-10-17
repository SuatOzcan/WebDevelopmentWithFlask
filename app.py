from flask import Flask, render_template, request, url_for, redirect
#HTML files should be in 'templates' folder.

app = Flask(__name__)

posts = {
    0 : {
        'id' : 0,
        'title' : 'Hello World!',
        'content' : 'This is my first blog post.'
    }
}

@app.route('/')
def home():
    return ('Hello World!')

@app.route('/post/<int:post_id>') #/post/0
def post(post_id):
    post = posts.get(post_id)
    if not post: #If posts.get(post_id) does not have the key, it will return None, and None is False.
        return render_template("404.jinja2", message = f"A post with id {post_id} is not found.")
    #return (f'Post {post["title"]}, content: \n\n {post["content"]}')
    return render_template('post.jinja2', post = post)

@app.route('/post/form')
def form():
    print(posts)
    return render_template('create.jinja2')

#127.0.0.1:5000/post/create?title=placeholder&content=anotherplaceholder
@app.route('/post/create')
def create():
    title = request.args.get('title')
    content = request.args.get('content')
    post_id = len(posts)
    posts[post_id] = {'id' : post_id, 'title' : title, 'content' : content}
    return redirect(url_for('post', post_id = post_id))

if __name__ == '__main__':
    app.run(debug = True)
