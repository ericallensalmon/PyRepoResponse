# PyRepoResponse
Python app to receive emails for GitHub WebHooks

To set up (for testing or use) you will need: 

- A server to run the app (or run locally with something like ngrok)
- a Mailgun account
- a GitHub repository to test the web hook

Instructions:
1. Start up a server (or use ngrok or similar to forward a web address to your local machine) 
2. Set up a WebHook on your GitHub repository using the server's public IP(or ngrok address)
3. For now, replace the hardcoded mailgun domain, key, and email address (and the port if desired)
    - Remember not to commit your details!
4. Run the server.py on your server



TODO: management screen to handle configuration of ports, urls, etc.


