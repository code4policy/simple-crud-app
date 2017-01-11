from flask import Flask, request, jsonify

app = Flask(__name__)

posts = {
    1: {
        "id": 1,
        "title": "This is a sample post",
        "content": "<h1>Hello HKS!</h1>"
    }
}

def next_id():
    return sorted(posts.keys())[-1] + 1

def validate(post):
    if "title" not in post:
        raise Exception("post must have a 'title'")
    if "content" not in post:
        raise Exception("post must have 'content'")
    return post

@app.route("/")
def root():
    return "Hello World!"

@app.route("/api/v1/posts/", methods=['GET'])
def get_list():
    global posts
    return jsonify(list(posts.values()))

@app.route("/api/v1/posts/<int:post_id>/", methods=['GET'])
def get_one(post_id):
    global posts
    if post_id not in posts:
        raise Exception("could not find post %s" % post_id)
    return jsonify(posts[post_id])

@app.route("/api/v1/posts/", methods=['POST'])
def post():
    global posts
    post = validate(request.get_json())
    post['id'] = next_id()
    posts[post['id']] = post
    return jsonify(post), 201

@app.route("/api/v1/posts/<int:post_id>/", methods=['DELETE'])
def delete(post_id):
    global posts
    if post_id not in posts:
        raise Exception("could not find post %s" % post_id)
    del posts[post_id]
    return '', 204

@app.route("/api/v1/posts/<int:post_id>", methods=['PUT'])
def put(post_id):
    global posts
    posts[post_id] = validate(request.get_json())
    return posts[post_id]

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
