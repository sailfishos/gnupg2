PKG_NAME := gnupg2
SPECFILE = $(addsuffix .spec, $(PKG_NAME))
YAMLFILE = $(addsuffix .yaml, $(PKG_NAME))

include /usr/share/meego-packaging-tools/Makefile.common

