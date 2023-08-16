#!/bin/bash

token=$(curl -s -X POST 127.0.0.1:30002/login -u g@g.com:111)

curl -X POST -F "file=@video.mp4" -H "Authorization: Bearer $token" 127.0.0.1:30002/upload