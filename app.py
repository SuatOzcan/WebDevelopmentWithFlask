from flask import Flask, render_template
#HTML files should be in 'templates' folder.

app = Flask(__name__)

posts = {
    0 : {
        'title' : 'Hello World!',
        'content' : 'This is my first blog post.'
    }
}

@app.route('/post/<int:post_id>') #/post/0
def post_id(post_id):
    post = posts.get(post_id)
    if not post: #If posts.get(post_id) does not have the key, it will return None, and None is False.
        return render_template("404.jinja2", message = f"A post with id {post_id} is not found.")
    #return (f'Post {post["title"]}, content: \n\n {post["content"]}')
    return render_template('post.jinja2', post = post)

@app.route('/')
def home():
    return ('Hello World!')

if __name__ == '__main__':
    app.run(debug = True)
