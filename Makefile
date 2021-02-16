#!/usr/bin/env make
# This makefile is used to compile my thesis on the fly.
# It build the glossary, bibliography and PDF
# cmdoret, 20201030

#GFXDIR="./gfx/"
#SRCDIR="./src/"
#SRC = $(shell find $(SRCDIR) -type f -regex '.*\.\(R\|py\)')
#GFX = $(patsubst $(GFXDIR)/%.pdf, $(SRCDIR)/%.(R|py), $(SRC))

#$(SRCDIR)/%.(py|R): $(GFXDIR)/%.pdf
#	@mkdir -p "$(@D)"
#	@echo "./$<" "$@"


.PHONY: clean,all
all: my-thesis.pdf

clean:
	find ./ -regex '.*\.\(aux\|acn\|fls\|glo\|lof\|lot\|nlg\|ntn\|run.xml\|xdy\|toc\)$$' -delete


my-thesis.pdf: my-thesis.tex library.bib
	pdflatex my-thesis
	bibtex my-thesis
	makeglossaries my-thesis
	pdflatex my-thesis

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
