#!/bin/sh

# server=http://localhost:5000
server=https://thawing-castle-69213.herokuapp.com

curl -H "Content-Type: application/json" -X POST "$server/api/v1/posts/" \
	-d '{"title": "New Post", "content": "content of my new post"}'
