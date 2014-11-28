contaboard
==========

As a Campus Ambassador I need an overview of my talent pool.
Contaboard provides an interface for creating new contacts and view existing ones.
This is not about managing relations but to keep notes about a person in an uncomplicated way (in contrast to most CRMs).

# idea
The central model is a talent which can have many skills or any information. How a model looks like is defined in an initial schema.
A talent model can have tags (speak skills?). These hashtags provide good additional information.

To create the talent you simply input the name and a description:

```json
{
    name: "Lukas Martinelli",
    desc: "Has built websites with #django and is a proficient #python user.
           Has worked 4 years on the #dotnet platform."
}
```

This information can now be enriched with more data. For example we try to find the person
via social networks and the internet.
The end result may look like this

```


