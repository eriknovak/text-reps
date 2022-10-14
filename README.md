# NLP Word and Sentence Representations

This project contains the code for creating vector representations of texts.

## ☑️ Requirements

Before starting the project make sure these requirements are available:

- [conda][conda]. For setting up your research environment and python dependencies.
- [git][git]. For versioning your code.

## 🛠️ Setup

### Create a python environment

First create the virtual environment where all the modules will be stored.

#### Using virtualenv

Using the `virtualenv` command, run the following commands:

```bash
# install the virtual env command
pip install virtualenv

# create a new virtual environment
virtualenv -p python ./.venv

# activate the environment (UNIX)
./.venv/bin/activate

# activate the environment (WINDOWS)
./.venv/Scripts/activate

# deactivate the environment (UNIX & WINDOWS)
deactivate
```

#### Using conda

Install [conda][conda], a program for creating python virtual environments. Then run the following commands:

```bash
# create a new virtual environment
conda create --name text-reps python=3.8 pip

# activate the environment
conda activate text-reps

# deactivate the environment
deactivate
```

### Install

To install the requirements run:

```bash
pip install -e .
```


## ⚗️ Running scripts

TODO

## 🚧 Work In Progress

- [ ] Add support for various language models
    - [ ] Sentence Transformers
    - [ ] BERT
    - [ ] RoBERTa
    - [ ] XLM-RoBERTa

- [ ] Add support for various word embedding models
    - [ ] word2vec
    - [ ] GloVe
    - [ ] fastText

- [ ] Develop main script
- [ ] Write documentation
- [ ] Provide examples


## 📣 Acknowledgments

This work is developed by [Department of Artificial Intelligence][ailab] at [Jozef Stefan Institute][ijs].

This work is supported by the Slovenian Research Agency and the TODO.

[python]: https://www.python.org/
[conda]: https://www.anaconda.com/
[git]: https://git-scm.com/
[ailab]: http://ailab.ijs.si/
[ijs]: https://www.ijs.si/
