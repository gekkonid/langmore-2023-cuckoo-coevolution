outhtmls := \
	02_initial-filtering-plots.html \
	03_basic-popgen.html \
	04_fresh-sample-popgen.html


html: $(outhtmls)

.PHONY: clean
clean:
	@echo rm -rf *_cache/ *_files/ *.html

ipynb := $(patsubst %.Rmd,%.ipynb,$(rmd))
ipynb_html := $(patsubst %.ipynb,%.html,$(nb))
nb_html: $(ipynb_html)

.PRECIOUS: %.ipynb

%.html: %.R
	Rscript -e 'rmarkdown::render("$^", output_file="$@")'
