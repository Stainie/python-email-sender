# python-email-sender
A simple script for sending emails with attachment to several recipients.

# message format
Your `email_config.json` should be structured in the following way:
```
{
    'subject': '...',
    'body': '...',
    'links': {
        ...
    },
    'attachments': [
        ...
    ]
}
```

# email list format
name,email

Recepient1, recepient@email.com

# env
Add .env file with values SENDER_EMAIL and SENDER_PASSWORD if you don't want to add them manually each time you run the script.

Have fun!