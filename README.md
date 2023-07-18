# Python Discord Bot Template

<p align="center">
  <a href="https://discord.gg/mTBrXyWxAF"><img src="https://img.shields.io/discord/739934735387721768?logo=discord"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template/releases"><img src="https://img.shields.io/github/v/release/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template/commits/main"><img src="https://img.shields.io/github/last-commit/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template/blob/main/LICENSE.md"><img src="https://img.shields.io/github/license/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://github.com/kkrypt0nn/Python-Discord-Bot-Template"><img src="https://img.shields.io/github/languages/code-size/kkrypt0nn/Python-Discord-Bot-Template"></a>
  <a href="https://conventionalcommits.org/en/v1.0.0/"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

This repository is a template that everyone can use for the start of their discord bot.

When I first started creating my discord bot it took me a while to get everything setup and working with cogs and more.
I would've been happy if there were any template existing. However, there wasn't any existing template. That's why I
decided to create my own template to let <b>you</b> guys create your discord bot easily.

Please note that this template is not supposed to be the best template, but a good template to start learning how
discord.py works and to make your own bot easily.

If you plan to use this template to make your own template or bot, you **have to**:

- Keep the credits, and a link to this repository in all the files that contains my code
- Keep the same license for unchanged code

See [the license file](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/blob/master/LICENSE.md) for more
information, I reserve the right to take down any repository that does not meet these requirements.

## Support

Before requesting support, you should know that this template requires you to have at least a **basic knowledge** of
Python and the library is made for advanced users. Do not use this template if you don't know the
basics. [Here's](https://pythondiscord.com/pages/resources) a link for resources to learn python.

If you need some help for something, do not hesitate to join my discord server [here](https://discord.gg/mTBrXyWxAF).

All the updates of the template are available [here](UPDATES.md).

## Disclaimer

Slash commands can take some time to get registered globally, so if you want to test a command you should use
the `@app_commands.guilds()` decorator so that it gets registered instantly. Example:

```py
@commands.hybrid_command(
  name="command",
  description="Command description",
)
@app_commands.guilds(discord.Object(id=GUILD_ID)) # Place your guild ID here
```

When using the template you confirm that you have read the [license](LICENSE.md) and comprehend that I can take down
your repository if you do not meet these requirements.

Please do not open issues or pull requests about things that are written in the [TODO file](TODO.md), they are **already** under work for a future version of the template.

## How to download it

This repository is now a template, on the top left you can simply click on "**Use this template**" to create a GitHub
repository based on this template.

Alternatively you can do the following:

* Clone/Download the repository
    * To clone it and get the updates you can definitely use the command
      `git clone`
* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token
* Invite your bot on servers using the following invite:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  Replace `YOUR_APPLICATION_ID_HERE` with the application ID and replace `PERMISSIONS` with the required permissions
  your bot needs that it can be get at the bottom of a this
  page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)

## How to set up

To set up the bot I made it as simple as possible. I now created a [config.json](config.json) file where you can put the
needed things to edit.

Here is an explanation of what everything is:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |


## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
python -m pip install -r requirements.txt
```

After that you can start it with

```
python bot.py
```

## Build & Run with docker

```sh
docker build -t {my_bot} .
```

run the container and remove it on exit
```sh 
docker run  --name {my_bot_instance} --rm {my_bot}
```

## Deploy to GCP Compute Engine
Why compute engine well discord bots run on websockets and need a constant connection so we cant just deploy them to heroku or cloud functions.

1) Sign-up if you don't have an account already you will get $300 of credits but the small server we will spin up will be very cheap 
https://cloud.google.com/free

2) Create a new project: Once you've signed up and are on the GCP console, create a new project by clicking on the project dropdown on the header bar and then click on 'New Project'. Enter a name for your project and click 'Create'.

3) Enable Compute Engine API: Once your project is created, go to the Navigation Menu (hamburger icon on the top left), scroll down to 'APIs & Services' and click on 'Library'. In the library search for 'Compute Engine API' and enable it for your project.

4) Create a new Compute Engine instance: Go to the Navigation Menu again, scroll down to 'Compute Engine' and click on 'VM instances'. Click 'Create Instance'. Here you can specify the details for your instance. Choose the 'f1-micro' machine type (under the 'Machine configuration' section), select the region and zone of your choice, and choose the boot disk (for a basic setup, you can choose the Debian or Ubuntu OS). Leave the other options as their defaults.

if you use a spot instance its $2.83 for an E2 micro per month but the spot instance will go down.
Other wise its $7.11 for standard If you are using the $300 in free credits spluge on the standard as they only last 3 months (just be sure to turn it off or change it if you dont want to be spending that money after your credits exspier)


5) Set up your instance: Once your instance is created and running, you can set it up. Click the SSH button on your VM instances list to open a new browser window with a command-line interface to your new instance. From here, you can install any software you need (like Node.js, Python, etc.), clone your application from a git repository, install dependencies, etc.

Configure firewall rules: If your application needs to be accessible from the internet (e.g., a web server), you'll need to set up a firewall rule to allow traffic to your application. From the VM instance details page, click on the 'Edit' button and scroll down to 'Network interfaces'. Click on the name of your network interface, which will take you to the 'VPC network details' page. Scroll down to 'Firewall rules' and click 'Add firewall rule'. Give your firewall rule a name, leave 'Ingress' selected, and allow traffic from 'IP ranges' and enter '0.0.0.0/0'. Under 'Protocols and ports', you can specify which ports your application uses (for a web server, this is typically TCP port 80 or 443 for HTTPS). Click 'Create' to create your firewall rule.

Run your application: Back in your SSH window, you can now start your application. How to do this will depend on what your application is and how it's configured.

Keep your app running: If you want your app to stay running even after you close your SSH session, you may want to look into using a process manager like pm2 for Node.js applications or screen or tmux for more general use.


> **Note** You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.

## Issues or Questions

If you have any issues or questions of how to code a specific command, you can:

* Join my discord server [here](https://discord.gg/mTBrXyWxAF)
* Post them [here](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/issues)

Me or other people will take their time to answer and help you.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see
the [tags on this repository](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/tags).

## Built With

* [Python 3.9.12](https://www.python.org/)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
