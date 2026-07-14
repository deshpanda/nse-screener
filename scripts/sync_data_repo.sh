#!/bin/sh
# Sync big panels to the public data repo (run after major ingests).
set -e
SRC=~/Documents/personal-github-repos/nse-screener/data
DST=~/Documents/personal-github-repos/nse-screener-data
for d in bhav futstk pit ann_full announcements fr_xbrl deals_hist mto \
         shareholding indices pledge index_members ratings \
         reconstitution shareholding_detail; do
  [ -d "$SRC/$d" ] && rsync -a --delete "$SRC/$d/" "$DST/$d/"
done
cd "$DST" && git add -A && git commit -m "data sync $(date +%F)" && git push
