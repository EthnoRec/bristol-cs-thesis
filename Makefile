all:
	bibtex thesis
	xelatex -shell-escape thesis
