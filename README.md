# PhD Thesis
**cmdoret, 2020**

This repository contains all the different latex files required to compile my PhD thesis.
This is based on the cleanthesis style, hosted at: https://github.com/derric/cleanthesis

To compile the thesis into a pdf file, simply run `make`.

The precompiled thesis in PDF format is available from the [releases page](https://github.com/cmdoret/phd/releases).

Code and analyses associated with this thesis is available on the following repositories:

The structure of the latex files is as follows:


```
.
├── FrontBackMatter/       # Files related to front page, glossary etc.
├── my-thesis.tex          # Master .tex file for the thesis which gets compilated.
├── Parts/		   # Largest unit of separation (Intro, results, discussion, ...)
│  ├── Appendix.tex	   # Special part rendered at the end of the thesis.
│  ├── PartXX/		   # Contains all files required by partXX.tex.
│  │  ├── ChapterXX.tex	   # Subdivision of parts, where most of the text is written.
│  │  └── gfx/		   # Figure and graphical files used in the part.
│  └── PartXX.tex          # Master file for the part, with a short introduction and chapter imports.
└── Publications/	   # PDF files of publications included in the thesis.
```
