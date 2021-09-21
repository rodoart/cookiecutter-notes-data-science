# Cookiecuter Simple Data Science Notes for Data Science

This is my personal template for taking notes for online classes.

## Requirements

- [Anaconda](https://www.anaconda.com/download/)
- [git](https://git-scm.com/)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)
- [VSCode](https://code.visualstudio.com/)

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create new project

In the folder you want to create a new project, run

```bash
cookiecutter https://github.com/rodoart/cookiecutter-notes-data-science
```


## File structure

    {{ cookiecutter.project_slug }}
        ├── data <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---

## Credits

This project was forked from [jvelezmagic](https://github.com/jvelezmagic).
