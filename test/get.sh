#!/bin/sh

# server=http://localhost:5000
server=https://thawing-castle-69213.herokuapp.com

if [ -z "$1" ]; then
	curl "$server/api/v1/posts/"
else
	curl "$server/api/v1/posts/$1/"
fi
