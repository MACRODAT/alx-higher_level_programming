#!/bin/bash
# sends a request to a URL display response
curl -s -o /dev/null -w "%{response_code}" "$1"
