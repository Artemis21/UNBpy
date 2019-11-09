***Only entities intended for external use are documented here.***

## `UNBClient(token)`
The client to send web requests to the [UnbelievaBoat API](https://unbelievaboat.com/api/docs).  
*Parameters*
 - `token`: Your application token, available [here](https://unbelievaboat.com/applications).
*Methods*  
 - `get_all_users`
    - Input: a [discord.py](https://github.com/Rapptz/discord.py) [`Guild`](https://discordpy.readthedocs.io/en/latest/api.html#guild).
    - Output: a list of [`UNBUser`](#unbuser)s.
    - Raises: `APIError`.
 - `get_user`
    - Input: a [discord.py](https://github.com/Rapptz/discord.py) [`User`](https://discordpy.readthedocs.io/en/latest/api.html#user) and [`Guild`](https://discordpy.readthedocs.io/en/latest/api.html#guild) or just a [`Member`](https://discordpy.readthedocs.io/en/latest/api.html#member).
    - Ouput: a [`UNBUser`](#unbuser).
    - Raises: `APIError`.
## `UNBUser`
A class representing the data given by the API on a user. Should not be created externally.
*Methods*  
 - `reload`
    - Reload the bank, cash and rank properties to make them correct.
*Properties*  
 - `cash`: What a user has in cash. Changes will be sent to the API (and may raise an `APIError`).
 - `bank`: What a user has in their bank. Changes will be sent to the API (and may raise an `APIError`).
 - `rank`: The position of a user on the guild leaderboard. Read-only.
 - `user`: The [discord.py](https://github.com/Rapptz/discord.py) [`Member`](https://discordpy.readthedocs.io/en/latest/api.html#member) representing this user.
 - `guild`: This [discord.py](https://github.com/Rapptz/discord.py) [`Guild`](https://discordpy.readthedocs.io/en/latest/api.html#guild) this user is in.
## Errors
 - `APIError`
    - Raised whenver the API returns a non-200 status response.
