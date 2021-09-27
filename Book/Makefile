DATE = $(shell date --iso=seconds)

help: 
	@echo '#########################################################'
	@echo '# options:                                              #'
	@echo '#   book:        pdf built with bbl files included      #'
	@echo '#   reindex:     reindexing                             #'
	@echo '#   clean:       all removed, except sources and builts #'
	@echo '#########################################################'

book: 
	$(MAKE) clean
	pdflatex book.tex
	pdflatex book.tex
	$(MAKE) reIndex


reIndex:
	pdflatex book.tex
	makeindex -s svind.ist book.idx
	pdflatex book.tex

clean:
	find . -name \*.aux -type f -delete
	find . -name \*.log -type f -delete
	find . -name \*~ -type f -delete
	find . -name \*.backup -type f -delete
	find . -name \*.blg -type f -delete
	find . -name \*.bak -type f -delete
	find . -name \*.pyc -type f -delete
	find . -name \*.lof -type f -delete
	find . -name \*.lot -type f -delete
	find . -name \*.toc -type f -delete
	find . -name \*.mtc -type f -delete
	find . -name \*.bmt -type f -delete
	find . -name \*.out -type f -delete
	find . -name \*.brf -type f -delete
	find . -name \*.idx -type f -delete
	find . -name \*.ilg -type f -delete
	find . -name \*.ind -type f -delete
	find . -name \*.maf -type f -delete
	find . -name \*.synctex.gz -type f -delete
