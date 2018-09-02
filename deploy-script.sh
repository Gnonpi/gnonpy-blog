#!/usr/bin/env bash

# Get dirname of this script (repo)
echo "Getting workspace dir"
WORKSPACE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

# Export variables from config
echo "Exporting variables"
source ${WORKSPACE}/config/deploy-vars

# Create exportable public/ with hugo
echo "Generating public/ version"
hugo

# TODO: add git commit+version+push

# Send content of public to hosting server
echo "SENDING TO SERVER"
rsync -av public/* ${DEPLOY_USER}@${DEPLOY_HOST}:/var/www/gnonpy.com

# Remove last public folder
echo "Removing public"
rm -r ${WORKSPACE}/public/
