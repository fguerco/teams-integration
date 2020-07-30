## Requisitos

1. Python 3
2. Biblioteca requests do python

        pip install requests
3. Uma aplicação que tenha as seguintes permissões:
    - ChannelMessage.Send
    - user.read

## Configuração

Crie um arquivo chamado config.json com o seguinte conteúdo:

    {
      "tenant_id": "id da empresa",
      "app_id": "id da aplicação",
      "email": "seu email",
      "password": "sua senha",
      "client_secret": "secret",
      "group": "grupo (team)",
      "default_channel": "canal"
    }

## Dando consentimento

Acessar a url https://login.microsoftonline.com/{tenant-id}/oauth2/authorize?client_id={app-id}&prompt=consent&response_type=code&redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient

## Obtendo os ids de grupo e canal

Ir no MS Teams e selecionar canal. Clicar no botão "..." e escolher a opção "Get link to channel"

### Eexmplo de url

https://teams.microsoft.com/l/channel/{id-do-canal}/{nome-do-canal}?groupId={id-do-grupo}&tenantId={id-to-tenant}
