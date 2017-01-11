#!/bin/sh

if [ -z "$1" ]; then
	echo "need to provide post id"
else
	curl -X DELETE "http://localhost:5000/api/v1/posts/$1/"
fi
