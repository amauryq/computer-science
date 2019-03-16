#!/bin/bash
rsync -avz --exclude '.cache' --exclude '.config' --exclude '.local' --exclude 'Downloads' --delete /home/amauryq/ /run/media/amauryq/home2/amauryq
rsync -avz --delete /home/amauryq/Pictures /run/media/amauryq/Iomega/Family
rsync -avz --delete /home/amauryq/Videos /run/media/amauryq/Iomega/Family
rsync -avz --delete /home/amauryq/Music /run/media/amauryq/Iomega/Public

#rsync -avz --delete /shares/usb1-1share1/Family/ /shares/Family/
