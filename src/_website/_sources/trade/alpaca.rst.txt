.. post:: Oct 12, 2022
   :category: Trading
   :tags: Trading
   :author: Sam Khalilian

Alpaca Trading
==============

Create an account at https://alpaca.markets/.

Activate Two-Factor Authentification which use SMS or Google Authenticator.

To generate new API keys and secret password:

1. Select -> Menu
2. Switch Account -> Paper/Live
3. Orders -> Dashboard
4. Your API Keys -> View -> Regenerate Key

Save the API key and secret password to environment variables:

.. code-block:: bash

    ALPACA_USE_LIVE_ACCOUNT = 0
    ALPACA_API_KEY_PAPER = "<YOUR ALPACA API KEY>"
    ALPACA_SECRET_KEY_PAPER = "<YOUR ALPACA SECRET KEY>"
    ALPACA_API_KEY_LIVE = "<YOUR ALPACA API KEY>"
    ALPACA_SECRET_KEY_LIVE = "<YOUR ALPACA SECRET KEY>"


Install the Alpaca Trade API:

.. code-block:: bash

    pip install alpaca-trade-api


