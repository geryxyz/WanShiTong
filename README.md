# WanShiTong

## Elevator Pitch

Our researchers prefer to use LaTeX to prepare their scientific publications. But a good paper contains several citations to specify the context of the research. In the case of the LaTeX ecosystem, these references are stored in a centralized BibTeX database, which is embodied by one or more BIB files. In essence, these are source code files of the database. For example:

```
...

@Book{abramowitz+stegun,
 author    = "Milton {Abramowitz} and Irene A. {Stegun}",
 title     = "Handbook of Mathematical Functions with
              Formulas, Graphs, and Mathematical Tables",
 publisher = "Dover",
 year      =  1964,
 address   = "New York City",
 edition   = "ninth Dover printing, tenth GPO printing"
}

...
```

Researchers rarely work alone, and publications are usually referred from several papers. Hence research teams have to introduce some processes to search, group, and store these BIB files. Several existing references management systems provide some degree of BibLaTeX integration, like exporting and importing BIB files. These tools usually store references in their own, non-BibTeX-based database; hence BibTeX support is merely one feature among several others.

Our goal is to reduce the cost and complexity of the bibliography management for those research teams, which use Git repositories and BIB files to store their references. The project Wan Shi Tong will provide a web application, which will utilize BibTeX as their primary storage system and Git to control the versions of the database. This solution will eliminate the need to convert back and forth from different representations of the references.

##A forráskód felépítése
A projekt Tornado keretrendszerben került megvalósításra, ez dokumentáció alapján lett szétbontva mappákra.

###A webszerver elindítása
A webszervert a gyökérben található _run_webserver.py_ segítségével lehet elindítani. Ez egy külön szálon elkezdi  felépíteni az egész webszervert és a háttérben elkezdi futtatni. A szerver alapértelmezetten 80-as porton elérhető. Az egyik legfontosabb funkciója a module_init-nek, hogy az adatbázis kapcsolat ott jön létre. 

###The handlers
A webszerver indításával párhuzamosan a module_init.py felépíti a weboldal hierarchiáját. A felhasználótól érkező get -és post kéréseket fogadja a modul és 'továbbítja' a handlerekhez. Az egyes handlerek eléréséhez szükséges URI-t a module_init adja meg. Egyes handlereknek a module_basehandler a szülője. Egy ilyen folyamat a kéréssel együtt felépül és a kérés végén a rendszer elpusztítja (destroy!), ezért szükséges az állandó változókat eltárolni handleren kívül. A module_init átadja paraméterként saját magát a module_basehandler részére.

###A templates
A tornado az automatikus weboldalgenerálást támogatja. Egy-egy handler rendereli a template-t és fokozatosan építi fel saját magát. A templates mappában a mappák neve megegyeznek a modulok neveivel.

###Adattovábbító réteg
Az utils mappában megtalálható az intermediate mappa, ebben van egy Processor.py. Ez építi fel a szűrőket és az egyéb keresési feltételeket.