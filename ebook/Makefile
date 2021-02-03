.PHONY: default
default: help

.PHONY: help
## help: prints this help message
help:
	@echo "Usage: \n"
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

.PHONY: ebook
## ebook: generates the epub file
ebook:
	@echo "Generating epub file..."
	pandoc \
		--filter pandoc-filter/toc-remove.py \
		--dpi=300 \
		--standalone \
		--output DescomplicandoKubernetes.epub \
		title.txt \
		../README.md \
		../day-1/DescomplicandoKubernetes-Day1.md \
		../day-2/DescomplicandoKubernetes-Day2.md \
		../day-3/DescomplicandoKubernetes-Day3.md \
		../day-4/DescomplicandoKubernetes-Day4.md \
		../day-5/DescomplicandoKubernetes-Day5.md \
		../day-6/DescomplicandoKubernetes-Day6.md \
		../Extras/Dicas_prova.md \
		../Extras/pod-security-policy.md

.PHONY: lint
## lint: modifies the code that doesn't follow the PEP 8 style guide
lint:
	black .

.PHONY: lint-check
## lint-check: runs the check flag of black
lint-check:
	black --check .
