Running local server
====================

 * Clone the repository:

    ````
    $ git clone git@github.com:tonnydourado/masenfim.git
    ````

 * Update the plugins submodule:

    ````
    $ git submodule init
    $ git submodule update
    ````

 * Create a virtualenv:

    ````
    $ mkvirtualenv masenf.im
    ````

 * Install the requirements (pelican, ghp-import, and all else):

    ````
    $ pip install -r requirements.txt
    ````

 * Run the local webserver:

    ````
    $ make devserver
    ````

 * On another terminal, run the regenerate command:

    ````
    $ make regenerate
    ````

Publishing
==========

 * Process the articles using the publish settings:

    ````
    $ make publish
    ````

 * Publish to github:

    ````
    $ make github
    ````
