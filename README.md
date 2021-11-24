# PhD Thesis
**cmdoret, 2020**

This repository contains all the different latex files required to compile my PhD thesis.
This is based on the cleanthesis style, hosted at: https://github.com/derric/cleanthesis

To compile the thesis into a pdf file, simply run `make`.

The precompiled thesis in PDF format is available from the [releases page](https://github.com/cmdoret/phd/releases). Each tagged commit (release) was automatically compiled into a pdf using github workflows.

The structure of the latex files is as follows:

```
.
├── my-thesis.tex          # Master .tex file for the thesis which gets compiled.
├── FrontBackMatter/       # Files related to front page, glossary etc.
├── assets/       	   # External PDF files to include as appendices.
├── Parts/		   # Largest unit of separation (Intro, results, discussion, ...)
│  ├── Appendix.tex	   # Special part rendered at the end of the thesis.
│  ├── PartXX/		   # Contains all files required by partXX.tex.
│  │  ├── ChapterXX.tex	   # Subdivision of parts, where most of the text is written.
│  │  └── gfx/		   # Figure and graphical files used in the part.
│  └── PartXX.tex          # Master file for the part, with a short introduction and chapter imports.
└── Publications/	   # PDF files of publications included in the thesis.
```

Code and analyses associated with this thesis' results are available on the following repositories:

* Part II, Chapter 1:
  + [hicstuff](https://github.com/koszullab/hicstuff)
  + [chromosight](https://github.com/koszullab/chromosight)
  + [pareidolia](https://github.com/koszullab/pareidolia)
* Part II, Chapter 2:
  + [A. castellanii assembly](https://github.com/cmdoret/Acastellanii_hybrid_assembly)
  + [A. castellanii annotation](https://github.com/cmdoret/Acastellanii_genome_annotation)
  + [A. castellanii genome analysis](https://github.com/cmdoret/Acastellanii_genome_analysis)
  + [A. castellanii-legionella infection analysis](https://github.com/cmdoret/Acastellanii_legionella_infection)
* Part II, Chapter 3:
  + [Mouse macrophage-Salmonella infection analysis](https://github.com/cmdoret/mouse_salmonella_infection)
