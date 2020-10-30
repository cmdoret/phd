#!/usr/bin/env make
# This makefile is used to generate / update figures on the fly.
# All scripts in SRCDIR are detected and their file hierarchy is replicated
# into GFXDIR so that each script has a figure of the same name.
# cmdoret, 20201030
GFXDIR="./gfx/"
SRCDIR="./src/"
SRC = $(shell find $(SRCDIR) -type f -name '*.(R|py)')
GFX = $(patsubst $(GFXDIR)/%.pdf, $(SRCDIR)/%.(R|py), $(SRC))

.PHONY: all
all: $(GFX)

$(SRCDIR)/%.(py|R): $(GFXDIR)/%.pdf
    @mkdir -p "$(@D)"
	@echo "./$<" "$@"
### Part I ###
## ch:01-01 ##
## ch:01-02 ##
## ch:01-03 ##
### Part II ###
## ch:02-01 ##
## ch:02-02 ##
## ch:02-03 ##
### Part III ###
## ch:03-01 ##
## ch:03-02 ##
## ch:03-03 ##
