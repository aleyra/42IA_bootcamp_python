# Module00

## Avant l'exercice 00
`wget https://www.python.org/ftp/python/3.7.13/Python-3.7.13.tar.xz`.\
`tar -xf Python-3.7.13.tar.xz`.\
`sudo mv Python-3.7.13 /opt/`.\
`sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev -y`.\
`cd /opt/Python-3.7.13/`.\
`./configure --enable-optimizations --enable-shared `.\
`make`.\
`sudo make altinstall`.\
`sudo ldconfig /opt/Python3.7.13 `.\
`python3.7 --version`.\
Vérifier le résultat.\
`curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"`.\
`sh Miniconda3-latest-Linux-x86_64.sh -b`.\
`/home/lucille/miniconda3/bin/conda init zsh`.\
`/home/lucille/miniconda3/bin/conda config  --set auto_activate_base false`.\
`source ~/.zshrc`.\
`conda create --name 42AI-lburnet python=3.7 jupyter pandas pycodestyle numpy`.\
`conda info --envs`.\
Vérifier le résultat.\
`conda activate 42AI-lburnet`.\
`which python`.\
Vérifier le résultat.\
`python -V`.\
Vérifier le résultat.\
`python -c "print('Hello World!')"`.\
Vérifier le résultat.\

## exercice 01
liens utiles
* equivalent argc, argv de C en python : https://realpython.com/python-command-line-arguments/
* utiliser sys.argv : https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
* reverse une liste : https://www.programiz.com/python-programming/methods/list/reverse