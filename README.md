# Box SDK Demo

Box offers a Python SDK - [link](https://github.com/box/box-python-sdk). This repository contains example code using that SDK.

# Setup

## Requirements

```
pip install boxsdk python-dotenv
```

or

```
pip3 install boxsdk python-dotenv
```

In order to protect credentials, but also provide an interface to store them, I have included a `.env.example` file. To set up your local environment, copy the `.env.example` file to a new file name `.env`, and set values for each of the variables.

If you want to create the copy in your terminal, you can

```
$ cp .env.example .env
```

Here's a cool site that will [explain that command](https://explainshell.com/explain?cmd=cp+.env.example+.env). That is a handy site to bookmark.

Notice the `.env` file is gray in the VS Code file explorer. Open that `.env` file and replace the values between the quotes with your real values.

<details>
  <summary>Explain</summary>

  ### What is git
  `git` is a tool for managing your source code - its contents, the changes to that content. It also does things which allow developer to work together on a project. It's just operating on text - so technically you could use it to track something like a book.
  
  So that's what we're using to track the work here. You can explicitly tell `git` **not** to track certain files. Thus ensuring they never make their way to github.

  This is done by including a [.gitignore](./.gitignore) file. Notice how we ignore `.env`.

  ### Ok but what about this .env thing
  If we don't want to write the key directly in our source code, we have to get it from somewhere. A common approach is to load them into what's known as an "Environment Variable". Your shell (the terminal runs your shell) runs in an environment - a variable is just some data in the environment you can set or get. There are a few predefined already in your system - and the system uses them to run, as does other software. For example, open the terminal and type `printenv HOME` or `printenv USERNAME`.

  Those are loaded in every shell session. But open two terminals now and follow along.

  ```
  // TERMINAL 1
  $ printenv PIZZA

  $ export PIZZA="shhhhh"

  $ printenv PIZZA
  shhhhh
  ```

  ```
  // TERMINAL 2
  $ printenv PIZZA

  ```

  Explanation - in terminal 1, we attempt to print the `PIZZA` environment variable. It does show up. So we call `export` to set the variable. Then, when we print it again, we see the value. Next, we head over to terminal two and notice that the `PIZZA` variable does not show up. Lesson - if I set an environment variable in a process, it does not mean other processes can get it. Hey - that's secure!

  You installed a package called `python-dotenv` - this will look for a file called `.env` and load the environment variables from them. What I do in this case is create an example file so someone using the project can copy it and set the values with their own keys. This is just a common convention and pattern. This `dotenv` package exists in some form in every language I've worked in. I find it simple and intuitive once you know what and why you're doing it.
</details>

To run the script in the terminal -

```
$ python3 ./client_example.py
The current user IS is 1723982340897
```