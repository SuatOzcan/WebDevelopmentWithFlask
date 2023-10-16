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
    #post = posts.get(post_id)
    #return (f'Post {post["title"]}, content: \n\n {post["content"]}')
    return render_template('post.html', post = posts.get(post_id))

@app.route('/')
def home():
    return ('Hello World!')

if __name__ == '__main__':
    app.run(debug = True)
