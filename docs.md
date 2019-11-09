***Only entities intended for external use are documented here.***

## `UNBClient(token)`
The client to send web requests to the UnbelievaBoat API.  
*Parameters*
 - `token`: Your application token, available [here](https://unbelievaboat.com/applications).
*Methods*  
 - `get_all_users`
    - Input: a discord.py `Guild`.
    - Output: a list of `UNBUser`s.
 - `get_user`
    - Input: a discord.py `User` and `Guild` or just a `Member`.
    - Ouput: a `UNBUser`.
## `UNBUser`
A class representing the data given by the API on a user. Should not be created externally.
*Methods*  
 - `reload`
    - Reload the bank, cash and rank properties to make them correct.
*Properties*  
 - `cash`: What a user has in cash. Changes will be sent to the API.
 - `bank`: What a user has in their bank. Changes will be sent to the API.
 - `rank`: The position of a user on the guild leaderboard. Read-only.
 - `user`: The discord.py `Member` representing this user.
 - `guild`: This discord.py `Guild` this user is in.
## Errors
 - `APIError`
    - Raised whenver the API returns a non-200 status response.