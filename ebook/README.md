# eBook

## Generating the eBook

### Requirements
- [Pandoc](https://pandoc.org/installing.html),  convert files from one markup format into another;
- [Poetry](https://python-poetry.org/docs/#installation), python packaging and dependency management.

### Steps
- Enter poetry shell
```bash
poetry shell
```

- Install dependencies using poetry
```bash
poetry install
```

- Run pandoc to generate the epub file
```bash
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
```

## Extra
We are using [pandocfilters](https://github.com/jgm/pandocfilters) to create a filter for the table-of-contents (TOC) parts so we can exclude the ones within the files and let the one inside README.md as the truth-of-source for summaries in the book.
