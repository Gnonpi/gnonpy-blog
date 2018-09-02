#!/usr/bin/env bash

# Get dirname of this script (repo)
WORKSPACE=dirname $0

# Export variables from config
source ${WORKSPACE}/config/deploy-vars

# Create exportable public/ with hugo
hugo

# Send content of public to hosting server
rsync -av public/* ${DEPLOY_USER}@${DEPLOY_HOST}:/var/www/gnonpy.com

# Remove last public folder
rm -r public