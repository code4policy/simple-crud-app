#!/bin/sh

curl -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/posts/ \
	-d '{"title": "New Post", "content": "content of my new post"}'
