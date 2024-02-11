# EXTRA CREDIT
# Maybe in the README
# (cogli l'occasione per imparare come si può mostrare il contenuto di github in modo fancy)
# write: suppongo che abbiate bla bla (mongodb, poetry, git, docker-compose) installato, dopo aver git pullato fate poetry (?) install(?),
# poi qlcs tipo setup.sh (non .py, attenzione) che sovrascriva la riga VOLUMES di file yaml, poi docker up -d dalla cartella giusta (o addiritura lo posso mettere in questo file python così basta fare `$HOME/.local/bin/poetry run main.py` e fa tutto da solo? Potrei farlo con os [altrimenty c'è docker-py che è per Docker Engine API, import docker] :P) controlla il container con docker ps, poi fai che runnare main.py
#
# (6) Put stuff in the test folder, look at some test driven development stuff and understand what is important to be tested. Then put this stuff in readme so ppl know that, instead of/besides running main.py, they can run test1.py, test2.py, ..., tests1-5.py or whatever I learn when reading about TDD :D <3

Check che setup.py con poetry non serve!

Più interessante ora sarebbe:

1) Uno script tipo: import_data_to_db.py
che si connette al client, scarica, e popola il mio MongoDB database.

2) Poi, ho un main che sono 4 righe in croce, sta tutto in helpers.py, o simili
Lì dentro avrò tutte le definizioni di class e @app.get, e devo capire come queste funzioni siano note allo script main (https://realpython.com/python-application-layouts/)

To', magari (se ha senso per python) fare un "model_classes.py" e "get_functions.py"