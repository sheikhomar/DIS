# [Highly Accurate Dichotomous Image Segmentation （ECCV 2022）](https://arxiv.org/pdf/2203.03041.pdf)

Paper [Highly Accurate Dichotomous Image Segmentation （ECCV 2022）](https://arxiv.org/pdf/2203.03041.pdf) by
[Xuebin Qin](https://xuebinqin.github.io/), [Hang Dai](https://scholar.google.co.uk/citations?user=6yvjpQQAAAAJ&hl=en), [Xiaobin Hu](https://scholar.google.de/citations?user=3lMuodUAAAAJ&hl=en), [Deng-Ping Fan*](https://dengpingfan.github.io/), [Ling Shao](https://scholar.google.com/citations?user=z84rLjoAAAAJ&hl=en), [Luc Van Gool](https://scholar.google.com/citations?user=TwMib_QAAAAJ&hl=en).

This repo is forked from https://github.com/xuebinqin/DIS.

## Development Setup

1. Install [pyenv](https://github.com/pyenv/pyenv).

2. Install and activate the required Python version:

   ```bash
   pyenv install
   ```

3. Install [Poetry](https://python-poetry.org/docs/).

4. Install required Python libraries for this project:

   ```bash
   poetry install
   ```

5. Install pre-commit hooks:

    ```bash
    poetry run pre-commit install
    ```

## Getting Started

Download pretrained models:

```bash
poetry run download-models
```
