#!/bin/sh

if [ -z "$1" ]; then
	curl "http://localhost:5000/api/v1/posts/"
else
	curl "http://localhost:5000/api/v1/posts/$1/"
fi
