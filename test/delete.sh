#!/bin/sh

# server=http://localhost:5000
server=https://thawing-castle-69213.herokuapp.com

if [ -z "$1" ]; then
	echo "need to provide post id"
else
	curl -X DELETE "$server/api/v1/posts/$1/"
fi
