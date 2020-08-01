# Teams Integration - Send messages to a MS Teams channel

This software will help automation tools send messages to a MS Teams channel

## Requisites

1. Python 3
2. Python requests dependency

       pip install requests
3. An applicatin in the Active Directory with the permissions:
    - ChannelMessage.Send
    - user.read

## Configuration

Create a file named config.json with contents:

    {
      "tenant_id": "xxxx-aaa-bbbb (uuid)",
      "app_id": "xxx-aaaa-bbbb (uuid)",
      "email": "your email",
      "password": "your senha",
      "client_secret": "secret obtained from the app",
      "group": "group id (team)",
      "default_channel": "channel",
      "channels": {
        "alias": "id",
        ...
      }
    }

## Using docker

This project has `Dockerfile` and `docker-compose.yml` for convenience. If you wish to develop using docker:

Start with

    $ docker-compose up -d
Then run the application with

    $ docker-compose exec app teams-msg [args]

When you are done

    $ docker-compose down

## Giving consent

In your browser go to

    https://login.microsoftonline.com/{tenant-id}/oauth2/authorize?client_id={app-id}&prompt=consent&response_type=code&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient
and follow the instructions

## Getting ids for group and channel

Go to MS Teams e select the channel. Click the ellipsis (...) and choose the menu option "Get link to channel"

### Example URL

https://teams.microsoft.com/l/channel/{id-do-canal}/{nome-do-canal}?groupId={id-do-grupo}&tenantId={id-to-tenant}
