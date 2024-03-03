#!/bin/bash
# sends a POST req
# curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
# Color code variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
NC='\033[0m' # No Color

if [ $# -ne 1]; then
	echo "${RED}Usage: $0 <URL:PORT>${NC}"
	exit 1
fi

echo -e "${BLUE}Starting request...${NC}";
URL=$1