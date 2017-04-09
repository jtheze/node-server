node-server
====

For this project, you'll need Python 3.5+ and [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) installed on your computer.



Follow these steps in a terminal :

- `git clone https://github.com/jtheze/node-server.git && cd node-server`

- `source venv/bin/activate`

- `python3 api/myproject.py`

Then, in your browser :

- `http://localhost:5000/data`

- `http://localhost:5000/doc` for documentation formated thanks to [apiDoc](http://apidocjs.com/)

Note that those data are from api/test.db which have been fakely-generated with a script and Postman.
Real ones are visible at http://jtheze.ddns.net/data


TO-DO:
- [ ] Manage database with an ORM such as [peewee](http://docs.peewee-orm.com/en/latest/)
- [ ] Add logging features for errors
- [ ] Client side to show data in a more "human" way
- [ ] Table representation with a library such as [Sortable](http://github.hubspot.com/sortable/docs/welcome/)
- [ ] Graphic representation with a library such as [Chart.js](http://www.chartjs.org/), [Chartist](http://gionkunz.github.io/chartist-js/), [C3.js](http://c3js.org/)...
- [ ] Web push notification for every new entry
- [ ] ...
