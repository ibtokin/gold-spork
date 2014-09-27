gold-spork
==========

Django REST interface for Fat-Tony
A Django REST interface for Fat-Tony

**Disclaimer: I am currently working through the Django REST Framework tutorial, so until I'm comfortable enough with it, this API is going to be coded verbatim to match the REST Tutorial at http://www.django-rest-framework.org/. It seems like every time I get ballsy enough to go my own way with a new framework I overlook something and f- it up long before I notice it and debugging is a nightmare. SO... My new strategy is to go through the tutorials AT LEAST once step-by-step, then let it sink in for a bit before going through it a second or third time following my own specs. The difference is that now, I'm commiting all my work to GitHub, be it original , unoriginal or in between.**


This interface will be a one-stop shop for all of Fat-Tony's feed and notification data. Since Fat-Tony is only the beginning, I'm going to save my future self a lot of work here by having the server handle all the CRUD operations for the database containing the current feed items. A Python script will interact with the Twitter, Facebook, Instagram APIs and update the database according to our needs. A Django form will be provided to administrators for input as well (push notifications eventually, but let's not get ahead of ourselves as I'm a team of one.)

Don't laugh.

-Adan

Copyright (c) 2014 Adan Sandoval, D.B.A. XOR Development
