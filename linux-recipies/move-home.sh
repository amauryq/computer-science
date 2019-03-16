# no encrypted filesystem
sudo rsync -aXS --progress --exclude='/*/.gvfs' /home/. /mnt/home/.
# verify
sudo diff -r /home /mnt/home -x ".gvfs/*"
