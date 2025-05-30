﻿MongoDB C# Driver
=================

You can get the latest stable release from the [official Nuget.org feed](https://www.nuget.org/packages/MongoDB.Driver) or from our [github releases page](https://github.com/mongodb/mongo-csharp-driver/releases).

Getting Started
---------------

### Untyped Documents
```C#
using MongoDB.Bson;
using MongoDB.Driver;
```

```C#
var client = new MongoClient("mongodb://localhost:27017");
var database = client.GetDatabase("foo");
var collection = database.GetCollection<BsonDocument>("bar");

await collection.InsertOneAsync(new BsonDocument("Name", "Jack"));

var list = await collection.Find(new BsonDocument("Name", "Jack"))
    .ToListAsync();

foreach(var document in list)
{
    Console.WriteLine(document["Name"]);
}
```

### Typed Documents

```C#
using MongoDB.Bson;
using MongoDB.Driver;
```

```C#
public class Person
{
    public ObjectId Id { get; set; }
    public string Name { get; set; }
}
```

```C#
var client = new MongoClient("mongodb://localhost:27017");
var database = client.GetDatabase("foo");
var collection = database.GetCollection<Person>("bar");

await collection.InsertOneAsync(new Person { Name = "Jack" });

var list = await collection.Find(x => x.Name == "Jack")
    .ToListAsync();

foreach(var person in list)
{
    Console.WriteLine(person.Name);
}
```

Documentation
-------------
* [MongoDB](https://www.mongodb.com/docs)
* [Documentation](https://mongodb.github.io/mongo-csharp-driver/)

Questions/Bug Reports
---------------------
* [MongoDB Community Forum](https://developer.mongodb.com/community/forums/tags/c/drivers-odms-connectors/7/dot-net-driver)
* [Jira](https://jira.mongodb.org/browse/CSHARP)

If you’ve identified a security vulnerability in a driver or any other MongoDB project, please report it according to the [instructions here](https://www.mongodb.com/docs/manual/tutorial/create-a-vulnerability-report).

Contributing
------------

Please see our [guidelines](CONTRIBUTING.md) for contributing to the driver.

### Maintainers:
* Boris Dogadov             boris.dogadov@mongodb.com
* Dmitry Lukyanov           dmitry.lukyanov@mongodb.com
* James Kovacs              james.kovacs@mongodb.com
* Robert Stam               robert@mongodb.com

### Contributors:
* Alexander Aramov          https://github.com/alex687
* Bar Arnon                 https://github.com/I3arnon
* Wan Bachtiar              https://github.com/sindbach
* Mark Benvenuto            https://github.com/markbenvenuto
* Bit Diffusion Limited     code@bitdiff.com
* Jimmy Bogard              https://github.com/jbogard
* Ross Buggins              https://github.com/rbugginsvia
* Nima Boscarino            https://github.com/NimaBoscarino
* Oscar Bralo               https://github.com/Oscarbralo
* Alex Brown                https://github.com/alexjamesbrown
* Ethan Celletti            https://github.com/Gekctek
* Chris Cho                 https://github.com/ccho-mongodb
* Adam Avery Cole           https://github.com/adamaverycole
* Nate Contino              https://github.com/nathan-contino-mongo
* Alex Dawes                https://github.com/alexdawes
* Justin Dearing            zippy1981@gmail.com
* Dan DeBilt                dan.debilt@gmail.com
* Teun Duynstee             teun@duynstee.com
* Einar Egilsson            https://github.com/einaregilsson
* Ken Egozi                 mail@kenegozi.com
* Alexander Endris          https://github.com/AlexEndris
* Daniel Goldman            daniel@stackwave.com
* Simon Green               simon@captaincodeman.com
* Bouke Haarsma             https://github.com/Bouke
* James Hadwen              james.hadwen@sociustec.com
* Nuri Halperin             https://github.com/nurih
* Nikola Irinchev           https://github.com/nirinchev
* Jacob Jewell              jacobjewell@eflexsystems.com
* Danny Kendrick            https://github.com/dkendrick
* Ruslan Khasanbaev         https://github.com/flaksirus
* Konstantin Khitrykh       https://github.com/KonH
* Brian Knight              brianknight10@gmail.com
* John Knoop                https://github.com/johnknoop
* Andrey Kondratyev         https://github.com/byTimo
* Anatoly Koperin           https://github.com/ExM
* Nik Kolev                 nkolev@gmail.com
* Oleg Kosmakov             https://github.com/kosmakoff
* Maksim Krautsou           https://github.com/MaKCbIMKo
* Richard Kreuter           richard@10gen.com
* Daniel Lee                https://github.com/dlee148
* Kevin Lewis               kevin.l.lewis@gmail.com
* Dow Liu                   redforks@gmail.com
* Chuck Lu                  https://github.com/chucklu
* Alex Lyman                mail.alex.lyman@gmail.com
* Tomasz Masternak          https://github.com/tmasternak
* Mikalai Mazurenka         mikalai.mazurenka@mongodb.com
* John Murphy               https://github.com/jsmurphy
* Alexander Nagy            optimiz3@gmail.com
* Sridhar Nanjundeswaran    https://github.com/sridharn
* Nathan                    https://github.com/terakilobyte
* Rachelle Palmer           https://github.com/techbelle
* Rich Quackenbush          rich.quackenbush@captiveaire.com
* Carl Reinke               https://github.com/mindless2112
* Rodrigo Reis              https://github.com/rodrigoreis
* Gian Maria Ricci          https://github.com/alkampfergit
* Andrew Rondeau            github@andrewrondeau.com
* Ed Rooth                  edward.rooth@wallstreetjapan.com
* Katie Sadoff              https://github.com/ksadoff
* Sam558                    https://github.com/Sam558
* Sergey Shushlyapin        https://github.com/sergeyshushlyapin
* Alexey Skalozub           pieceofsummer@gmail.com
* Kevin Smith               https://github.com/kevbite
* Pete Smith                roysvork@gmail.com
* staywellandy              https://github.com/staywellandy
* Vyacheslav Stroy          https://github.com/kreig
* Jake Sta. Teresa          https://github.com/JakeStaTeresa
* Testo                     test1@doramail.com
* TimTim                    https://github.com/wegylexy
* Zhmayev Yaroslav          https://github.com/salaros
* Aristarkh Zagorodnikov    https://github.com/onyxmaster
* Vincent Kam               https://github.com/vincentkam
* Craig Wilson              https://github.com/craiggwilson
* Ming Yau Lee              https://github.com/mingyaulee
* Daniel Hegener            daniel.hegener@fisglobal.com
* Vladimir Setyaev          setyaev_v@pgstudio.io

If you have contributed and we have neglected to add you to this list please contact one of the maintainers to be added to the list (with apologies).
