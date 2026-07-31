# Jupyter Book

[Jupyter Book](https://jupyterbook.org/stable/) is a tool for building interactive books from Jupyter Notebooks.

Installation:

```bash
pip install jupyter-book
```

Initialize a project:

```bash
jupyter book init
```

Build a project:

```bash
jupyter book build
```

Start a project:

```bash
jupyter book start

# Or
npx mystmd start
```

Build and preview static pages:

```bash
npx mystmd build --html

python3 -m http.server 8000 --directory _build/html
```
