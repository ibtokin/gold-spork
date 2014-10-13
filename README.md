gold-spork
==========

A Django REST interface for Fat-Tony

Currently, this repo contains a pretty much verbatim fork of the official Django REST tutorial. Once I'm finally able to get it deployed to my AWS instance I'll be modifying the models and views to fit my custom JSON objects.


This interface will be a one-stop shop for all of Fat-Tony's social media data. Since Fat-Tony is only the beginning, I'm going to save my future self a lot of work here by having the server handle all the CRUD operations for the database containing the current feed items. A separate Python script will interact with Twitter, Facebook, Instagram APIs and update the database according to our needs. A Django form will be provided to administrators for input as well (push notifications eventually, but let's not get ahead of ourselves as I'm but a team of one.)

Don't laugh at my code.

-Adan

Copyright (c) 2014 Adan Sandoval, D.B.A. XOR Development
