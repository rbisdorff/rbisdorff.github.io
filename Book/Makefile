DATE = $(shell date --iso=seconds)

help: 
	@echo '#########################################################'
	@echo '# options:                                              #'
	@echo '#   all:         pdf built with pdflatex                #'
	@echo '#   book.pdf:    pdf built with pdflatex                #'
	@echo '#   clean:       all removed, except sources and builts #'
	@echo '#   veryClean:   everything removed, except sources     #'
	@echo '#########################################################'

all: 
	$(MAKE) veryClean
	$(MAKE) book.pdf

book.pdf: 
	# makes a pdf directly
	pdflatex book.tex
	#bibtex 02-mainMatters/00-chapterIntroduction.aux
	#bibtex 02-mainMatters/01-chapterIntroDigraph3.aux
	bibtex 02-mainMatters/02-chapterDigraphs.aux
	bibtex 02-mainMatters/03-chapterOutrankingDigraphs.aux
	bibtex 02-mainMatters/04-chapterNewPerfTab.aux
	#bibtex 02-mainMatters/05-chapterRandomPerfTabs.aux
	bibtex 02-mainMatters/06-chapterBestChoice.aux
	bibtex 02-mainMatters/07-chapterWinnerElection.aux
	bibtex 02-mainMatters/08-chapterRankings.aux
	#bibtex 02-mainMatters/09-chapterRelativeRating.aux
	bibtex 02-mainMatters/10-chapterAbsoluteRating.aux
	bibtex 02-mainMatters/11-chapterHPCRanking.aux
	bibtex 02-mainMatters/12-chapterAliceChoice.aux
	bibtex 02-mainMatters/13-chapterBestCSDpts.aux
	#bibtex 02-mainMatters/14-chapterBestStudents.aux
	#bibtex 02-mainMatters/15-chapterExercises.aux
	bibtex 02-mainMatters/16-chapterCorrelation.aux
	bibtex 02-mainMatters/17-chapterKernels.aux
	bibtex 02-mainMatters/18-chapterConfidentOutrankings.aux
	bibtex 02-mainMatters/19-chapterRobustOutrankings.aux
	#bibtex 02-mainMatters/20-chapterMultipartisan.aux
	#bibtex 02-mainMatters/21-chapterTemperingPlurality.aux
	bibtex 02-mainMatters/22-chapterGraphs.aux
	bibtex 02-mainMatters/23-chapterTreeGraphs.aux
	bibtex 02-mainMatters/24-chapterIsomorphicMIS.aux
	bibtex 02-mainMatters/25-chapterPerfectGraphs.aux
	pdflatex book.tex
	pdflatex book.tex
	#makeindex -s svind.ist book.idx
	#pdflatex book.tex
	#pdflatex book.tex

reIndex:
	pdflatex book.tex
	makeindex -s svind.ist editor.idx
	pdflatex book.tex

clean:
#	rm -f *~ *.aux  *.log *.backup *.bbl *.blg *.bak *.pyc *.lof *.lot *.toc *.mtc* *.bmt *.out *.brf *.idx *.ilg *.ind *.maf *.synctex.gz
#	rm -f 01-frontmatter/*~ 01-frontmatter/*.aux 01-frontmatter/*.log 01-frontmatter/*.backup 01-frontmatter/*.bbl 01-frontmatter/*.blg 01-frontmatter/*.bak 01-frontmatter/*.pyc 01-frontmatter/*.lof 01-frontmatter/*.lot 01-frontmatter/*.toc 
	find . -name \*.aux -type f -delete
	find . -name \*.log -type f -delete
	find . -name \*~ -type f -delete
	find . -name \*.backup -type f -delete
	find . -name \*.bbl -type f -delete
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

veryClean:
	$(MAKE) clean
	rm book.pdf
