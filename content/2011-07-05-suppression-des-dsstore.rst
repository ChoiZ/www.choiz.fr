Suppression des .DS_Store
#########################
:date: 2011-07-05 18:01:40
:author: choiz
:category: text
:tags: Mac .DsStore, Mac, .DS_Store
:slug: 2011-07-05-suppression-des-dsstore
:status: published

Dans une console sur votre mac tappez :

    defaults write com.apple.desktopservices DSDontWriteNetworkStores
    true

Redemarrez le mac.

