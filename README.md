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
