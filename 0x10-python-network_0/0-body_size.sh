#!/bin/bash
# sends a POST req
curl -sI "$URL" | grep -i content-length | cut -d " " -f 2
