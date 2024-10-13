# python-email-sender
A simple script for sending emails with attachment to several recipients.

# message format
Add `email_config.json` file to the root of your project. It should be structured in the following way:
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

# attachments
Make sure to add your attachment to the root of the project

# email list format
Name,Email

Recepient1, recepient@email.com

# env
Add .env file with values SENDER_EMAIL and SENDER_PASSWORD if you don't want to add them manually each time you run the script.

Have fun!