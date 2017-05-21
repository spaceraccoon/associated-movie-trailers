# Associated Movie Trailers
Associated Movie Trailers (AMT) pulls the bio and associated movies of your chosen person, then generates an html page displaying this information.

## Quickstart

### Dependencies

AMT is built on Python and uses two additional packages, [tmdbsimple](https://pypi.python.org/pypi/tmdbsimple) and [wikipedia](https://pypi.python.org/pypi/wikipedia/). tmdbsimple requires an API key from [The Movie Database](https://www.themoviedb.org/) to work. 

1. Register for and verify an account at TMDB.
2. Log into your account.
3. Select the API section on left side of your account page.
4. Click on the link to generate a new API key and follow the instructions.

Next, use pip to install the packages. Installation instructions for pip can be found [here](https://pip.pypa.io/en/stable/installing/).
1. `pip install tmdbsimple`
2. `pip install wikipedia`