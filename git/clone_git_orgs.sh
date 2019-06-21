#!/bin/env bash

export GIT_SERVER_URL=https://github.com
export GIT_TOKEN=a5f168e846fedb6d71ed1c00a523be3c0448a33d
GIT_ORGS=$( cat git.alm.orgs | tr '\r\n' ' ' )
for GIT_ORG in ${GIT_ORGS}; do
  mkdir -p ${GIT_ORG}
  cd ${GIT_ORG}
  curl "${GIT_SERVER_URL}/api/v3/orgs/${GIT_ORG}/repos?per_page=200&access_token=${GIT_TOKEN}" |   grep -e 'ssh_url*' |   cut -d \" -f 4 |   xargs -L1 git clone
  cd ..
done
