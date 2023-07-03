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
* reverse list : https://www.programiz.com/python-programming/methods/list/reverse
* changer la case : https://towardsdatascience.com/how-to-quickly-change-the-case-of-strings-in-python-a1565e383371
* reverse string : https://www.w3schools.com/python/python_howto_reverse_string.asp
* remove a char from string : https://www.askpython.com/python/string/remove-character-from-string-python

## exercice 02
liens utiles
* isdigit : https://www.w3schools.com/python/ref_string_isdigit.asp
* atoi : https://www.codespeedy.com/string-atoi-in-python/
* operator : https://www.w3schools.com/python/python_operators.asp
* function : https://www.w3schools.com/python/python_functions.asp

## exercice 03
liens utiles
* nb d'arg : https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-91.php
* function : https://www.w3schools.com/python/python_functions.asp
* print str and non-str as one : https://www.w3schools.com/python/python_strings_format.asp
* prompt : https://www.geeksforgeeks.org/taking-input-in-python/
* equivalent à main() : https://realpython.com/if-name-main-python/

## exercice 04
liens utiles
* operator : https://www.w3schools.com/python/python_operators.asp

## exercice 05
liens utiles
* tuple : https://www.w3schools.com/python/python_tuples_access.asp
* dict (un peu comme map) : https://www.w3schools.com/python/python_dictionaries.asp
* tuple to datetime : https://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/
* add item to tuple ; https://stackoverflow.com/questions/16730339/python-add-item-to-the-tuple
* fill avec un char speficique : https://stackoverflow.com/questions/4008546/how-to-pad-with-n-characters-in-python
* formatage nombre : https://www.w3schools.com/python/ref_string_format.asp
* 0 -> 00 : https://stackoverflow.com/questions/134934/display-number-with-leading-zeros

## exercice 06
liens utiles
### Part 1
* dict in dict : https://www.w3schools.com/python/python_dictionaries_nested.asp
### Part 2
* methodes de dict : https://www.w3schools.com/python/python_dictionaries_methods.asp
* https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python
* input -> list : https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
* str non vide : https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
* parce qu'à la fin de la list j'avais '' : https://www.geeksforgeeks.org/python-list-pop-method/

## exercice 07
liens utiles
* split : https://www.w3schools.com/python/ref_string_rsplit.asp
* strip = trim : https://www.w3schools.com/python/ref_string_strip.asp
* parcourir une liste : https://www.commentcoder.com/python-parcourir-liste/

## exercice 08
lien donné par le sujet : https://morsecode.world/international/morse2.html
liens utiles
* switch en python : https://www.commentcoder.com/python-switch-case/

## exercice 09
liens utiles
* randint : https://www.w3schools.com/python/ref_random_randint.asp

## exercice 10
J'y comprends rien ^^"

# Module01
## exercice 00
liens utiles
* class : https://www.w3schools.com/python/python_classes.asp
* isinstance pour check si c'est le bon type : https://pynative.com/python-isinstance-explained-with-examples/
* assert -> try throw error : https://www.w3schools.com/python/ref_keyword_assert.asp
* methodes du dict : https://www.w3schools.com/python/python_ref_dictionary.asp

## exercice 02
liens utiles
* operateurs class : https://zestedesavoir.com/tutoriels/1253/la-programmation-orientee-objet-en-python/4-operators/
* type of var : https://www.w3schools.com/python/python_datatypes.asp
* update tuple : https://www.w3schools.com/python/python_tuples_update.asp

## exercice 03
liens utiles
* yield : https://www.journaldunet.fr/web-tech/developpement/1202863-a-quoi-sert-le-mot-cle-yield-en-python/
* random.sample -> ordre aleatoire sans remise : https://openclassrooms.com/fr/courses/6204541-initiez-vous-a-python-pour-lanalyse-de-donnees/6252451-manipulez-des-nombres-aleatoires-avec-le-module-random
* suppr les doublons : https://waytolearnx.com/2019/04/supprimer-les-doublons-dune-liste-en-python.html
* trier une liste : https://geekflare.com/fr/python-sort-list/