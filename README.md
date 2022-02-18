# Vue Python Sandbox

A ready-to-use environment for developing simple Python applications
to be viewed in the browser instead of the command line.

## Before starting

Before start developing using this project, you need to install some required software.

### Requirements

Download and install the following packages:

- **[Python](https://www.python.org/downloads/) 3.6** or higher
- **[Node.js](https://nodejs.org/en/) 16.*x*** or higher

... and also the following, which are usually included in the previous distributions:

- **[PIP](https://pypi.org/project/pip/)**
- **[NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)**

### Verify the requirements

Once you've installed the above packages or if you don't know they're already installed on your system and want to check it, open a terminal (it may depends on which OS you are using)...

- **Linux:** `Terminal`.
- **Mac:** `Terminal` or `iTerm2`.
- **Windows:** `Command Prompt` or `PowerShell`.

... and type the following commands (one line at a time):

```sh
node --version
npm --version

python --version
pip --version
```

Each of these command should print the version of the software you just installed on your system.  
If not, go back to the previous step and install the missing ones.

## Installation

Once you've verified that all the above distributions are installed, you can proceed with the installation of more specific packages.

### Global packages

Open a terminal (or get the same you opened before) and type the following commands (one line at a time):

```sh
npm install -g yarn
pip install pipenv
```

> **Note**: If you're using a **Mac** or **Linux** distribution, I recommend typing these commands by putting a `sudo` before each.  
> This will ask you to enter your password, but don't worry... It's safe!
> It will simply install the packages globally, as an admin user, making them available to all the users of your machine.

### Verify the global packages

Just like you already did before, using a terminal, type the following commands (one line at a time):

```sh
yarn --version
pipenv --version
```

If both of these commands print their own version of the software, you're good to go!

### Local packages

You'll now be able to install the dependencies required from the project itself to work properly.

#### Navigate to the project folder

To do so, use a terminal to move to the project's root directory (it may depends on which OS you are using):

**Mac** or **Linux**:

```sh
cd "/home/<your-user>/path/to/project/vue-python-sandbox"
```

**Windows**:
```sh
cd "C:\Users\<your-user>\Path\To\Project\vue-python-sandbox"
```

> **Note**: You need to replace the path I wrote in quotes with the actual path of the project.  
> As I write this, I cannot predict where you'll place the project once downloaded; you're the only one who knows.
>
> In some cases, it will also work just by simply typing `cd ` and then dragging and dropping the actual project folder directly into the terminal window.  
> Don't forget to press the `Enter` key after it has auto-typed the path, of course. 

#### Install the dependencies

Now that you're in the project's root directory, you can finally install the dependencies required to run the project correctly.

Type into the terminal the following commands (one line at a time):

```sh
yarn install
pipenv install
```

> **Note**: This may take a while, depending on your internet connection and the speed of your computer.

### Conclusion notes

You're now ready to run the project and start developing!  
All these steps above only need to be done once, the first time.

Typically, you'll never have to go through these steps ever again.  
However, should something go wrong in the future, you can safely try repeating all these previous steps without worry.

## Building the project

Before you can run the project, you need to build it.  
The build process only needs to be done once, the first time.

To do this, open a terminal and navigate to the project's root directory.  
Once you're there, simply type the following command:

```sh
yarn build
```

## Running the project

Every time you need to run the project, all you have to do is simply open a terminal and navigate to the project's root directory.  
Then, type the following commands (one line at a time):

```sh
pipenv shell
python run.py
```

Now, if you visit the URL [`http://localhost:8080`](http://localhost:8080), you should see the project running in the browser.

### Debugging the project
The terminal, while the project is running, is no longer usable; from now on, it will print some logging messages with some information on the functionality and performance of the process.  
The terminal in this state may be useful to you if you want to debug something because it will also print error messages if you're doing something wrong.

### Stopping the project
When you're done and want to close the project, you can press the `Ctrl + C` key combination on your keyboard.  
This will interrupt the execution of the project and bring you back to normal terminal functionality.

## Developing your application

While the project is running, you can start developing and testing your application.

This sandbox enviroment, allows you to develop your application in a simple way.  
You just need to write your application inside the function named `vue_python_sandbox` inside the `app.py` file.

### Requirements

There are just a couple of requirements you need to keep in mind, when developing your application:
- The `vue_python_sandbox` function must return an object of type `list[list[str]]` to be corrected rendered from the Web interface.
- The Web interface, on the other hand, can pass infinite arguments to this function.  
These arguments will always be of type `str` and, of course, they must be defined in the function prototype to be accepted and read correctly.

### Conclusion notes

That said, you can develop any application you can imagine, as long as it follows the above requirements.  
There are no other specific restrictions; from there on, you can use whatever you need, you can import as files or libraries as you want, you can write whatever the Python language allows you to do.

---

So... Be **creative** and, of course, have a **lot of fun**! 🚀🤩
