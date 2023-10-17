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
    return render_template('home.jinja2', posts = posts)

@app.route('/post/<int:post_id>') #/post/0
def post(post_id):
    post = posts.get(post_id)
    if not post: #If posts.get(post_id) does not have the key, it will return None, and None is False.
        return render_template("404.jinja2", message = f"A post with id {post_id} is not found.")
    #return (f'Post {post["title"]}, content: \n\n {post["content"]}')
    return render_template('post.jinja2', post = post)

#127.0.0.1:5000/post/create?title=placeholder&content=anotherplaceholder
@app.route('/post/create', methods = ['GET','POST'])
def create():
    # title = request.args.get('title')
    # content = request.args.get('content')
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id' : post_id, 'title' : title, 'content' : content}
        return redirect(url_for('post', post_id = post_id))
    return render_template("create.jinja2")

if __name__ == '__main__':
    app.run(debug = True)
