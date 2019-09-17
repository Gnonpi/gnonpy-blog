Title:  From raw pip to poetry
Slug: from-raw-pip-to-poetry
Date: 2019-07-21
Tags: python, pip, pipenv, poetry
Status: published

[//]: <> (ref: https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)
[//]: <> (ref: https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)

<p align="center">
  <img alt="Repairing cars" src="https://imgs.xkcd.com/comics/python_environment.png">
</p>
<center>
  <i>There's always a relevant xkcd</i>
</center>

Other the years writing Python,
I've learned a lot about packaging and dependency manager.

Today, I'd like to present the peripeties and adventures
that lead to an "almost clean" Python installation in my workstations.

## Raw pip

<p align="center">
  <img alt="View of raw pip - system and user install" src="{static}/images/raw-pip.png">
</p>

When I was in engineering school,
I remember starting starting using [pip](https://pip.pypa.io/en/stable/installing/)
like I was using Ubuntu packages manager:
just raw `pip install --user`.

I had my `requirements.txt` and just dump everything into whatever python installation I had.
How foolish!
Of course, I ended up with problems having multiple projects with conflicting versions.

## A first isolation: virtualenv

<p align="center">
  <img alt="View of virtualenv - bin/ include/ and lib/" src="{static}/images/virtualenv.png">
</p>


So, I searched a better way to do isolate my Python dependencies.
And of course, I arrived to [virtualenv](https://virtualenv.pypa.io/en/latest/).

Virtualenv create a folder where the dependencies you install go,
and ensure they don't go outside that folder.
It ships a link to a Python in your system (but only use it to execute stuff)
and a Pip binary.

With that you can do the full:
```shell
# virtualenv -p <python path> will create a link to that python
$ virtualenv -p $(which python3.6) my_venv
# now we activate it (source for bash/zsh/dash)
$ source my_venv/bin/activate
$ which python
/path/to/my_venv/bin/python
# tadaaa! we can now do pip install, it'll install in my_venv folder
```

It's so widely used, that it has been integrated in stdlib as the `venv` module ([attention, it's not exactly the same thing](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)).

So you can even use it with a basic Python installing:
````
$ python3 -m venv my_venv
````
but you cannot pass the path to a Python binary like earlier 🙃

## Virtualenvs as toolbox

One cool thing,
you can use things that are inside your virtualenv without activating it.
For example:
```shell
$ virtualenv my_venv
# directly installing using my_venv's pip
$ my_venv/bin/pip install cookiecutter
# now in another terminal, you can do
$ path/to/my_venv/bin/cookiecutter
Usage: cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]...
```

This is super useful when you have a project running on Python2.7
but the rest of your projects are in Python3
(looking at you Ansible 😬).

## The false Messiah: Pipenv

### The savior
I could have continued with my virtualenv a long time.
However,  they are some limits:

- you have to remember what virtualenv to use for each project
- the dependency solver of pip has its limits ([link to github issue](https://github.com/pypa/pip/issues/988))
- you have to maintain a requirements.txt plus a requirements-dev.txt
- you have to activate the virtualenv in every shell

To try and improve the situation,
Kenneth Reitz came up with **[Pipenv](https://docs.pipenv.org/en/latest/)**.
It's simple:

1. you install pipenv in your system ([link to docs](https://docs.pipenv.org/en/latest/install/)),
2. initialize your project with `pipenv --python 3.6`.
It will create a Pipfile in your current folder,
defining the project characteristics and its dependencies
3. install the dependencies for your project with `pipenv install`.
This will create a virtualenv in a fixed location and install in it the dependencies described in the Pipfile 
(and in Pipfile.lock, a file containing the latest combination of dependencies used, to ensure compatibility),
4. then, everytime you want to run a command in your project,
you can prepend it with `pipenv run` to run in it the virtualenv

<p align="center">
  <img alt="View of pipenv" src="{static}/images/pipenv.png">
</p>

You can share the Pipfile in your version control system
for your colleagues to easily run your code.
For small tasks or bigger projects,
just having to do a `pipenv install` followed by a `pipenv run python <something>`
really save time and reduce the complexity of taking on someone else's project.

It simplify your workflow a lot.

### The various problems

I started using Pipenv at my job,
first on pure data-science problems where I typicaly only had to produce a result file (csv or other)
and then for a service.

At the beginning, everything was fine.
But as we used more and more pipenv,
we started to see some of its limitations:

- the dependency manager is slow.
With a kinda big project, it started to last around 10 minutes to install everything.
Since deploys meant to reinstall dependencies
(we thought that it would be the safest and painless way to do),
quickly `pipenv install` became our main bottleneck.
- some dependencies randomly broke it.
This meant that if you didn't pin versions to minor
(we learned that the hard way, for an application **pin carefully what version you want to use**),
you could have "surprise!" failed deploys.
- it was not made for libraries.
After creating our service,
we wanted to create our own Python libraries, 
publishing them to an internal artifact repository
and install them in our service.
But Pipenv was made to work for applications with concrete dependencies,
while libraries require abstract dependencies: 
it is very well explained [here](https://docs.pipenv.org/en/latest/advanced/#pipfile-vs-setup-py).

On top of that,
the controversies around Kenneth Reitz behaviour and the tone used when responding to issues on github
lead us to start thinking that maybe it was time to look for another solution.

## Poetry, a good solution

### A Pipenv-like
**[Poetry](https://poetry.eustace.io/)** is a project created by Sébastien Eustace,
who I already knew for being the author of the [pendulum](https://pendulum.eustace.io/) library (which I recommend).

On the surface, it look the same as Pipenv to use:

1. install poetry on your system (instructions [here](https://poetry.eustace.io/docs/#installation))
2. initialize your project with `poetry init`.
This will create a *pyproject.toml* file containing info about your project and its dependencies
3. install the project dependencies with `poetry install`.
This will create a virtualenv in a fixed location and install the dependencies there.
Poetry will use a lock file similar to the Pipfile.lock to try to maintain backward compatibility with the dependencies you already have
4. then every time you want to launch a command in your project,
you can do `poetry run <command>` to run it in the virtualenv.

So it's as easy to use as Pipenv.

What I like about Poetry is that it's not trying to reinvent the wheel,
it's reusing a lot of existing tools with close to no modifications.
Eustace always put good thinking into how he approach his projects
and (I think) that decision of reusing elements is a plus for Poetry.

### Poetry over Pipenv

#### Speed
When we made the transition from pipenv to poetry,
I measured the time each took to install the dependencies for that big service I mentioned,
with the same machine, from a raw installation:

- Pipenv: **6min30s**
- Poetry: **1min11s**

Seeing that, we were pretty pleased!
We were finally saying goodbye to our bottleneck!

#### Creating libraries

One other point where Poetry facilitated our dev lives
is when working with libraries.
Pipenv is made with applications in mind
while Poetry is more flexible 
and work well with both applications and libraries.
As said before, Pipenv use concrete dependencies
while Poetry can handle abstract dependencies.
Having the same tool for application and libraries was a great relief 
(you should focus on the problems the code solve, not the tools used).

And Poetry has a nice `publish` command that directly
pack and upload your library to a pypi repository.
It also allow you to make the distinction between the repo where you publish
and the repo from where you download.

#### Consistency

Since we started using Poetry a few months ago,
we seldom had problems with a dependency breaking the installation step.

It happened a few times with Pipenv, 
forcing us to pin up to minor version
and adding the burden of checking from time to time
if a pinned dependency had received a security patch or a cool new feature.

With Poetry, once we filled the first *pyproject.toml*,
we were good to go.

---

For the moment,
my team and I are very happy with poetry
and it has become a central tool in our Python ecosystem.
Even our devops team started to like it for its speed and its simplicity to use.

## A useful tool: pex

[pex](https://github.com/pantsbuild/pex) is a tool created at Twitter that create
some sorts of "virtualenv as file".
<explain the shims part, duplicata with pyenv>

It works like this:

1. you install pex
2. you write your list of dependencies in a *requirements.txt*
3. you run `pex -r requirements.txt -o my_pex_venv.pex`
You get a file called *my_pex_venv.pex* that "contains" your virtualenv
4. now to run a command using the pex virtualenv,
wherever the pex file is, you do `./my_pex_venv.pex <some>.py`
and it runs!

I haven't used pex in production or in a big project yet.
But when doing some experiments and integrating it in some projects,
I've noticed some things:

- having to have the right Python version installed in the same system is still a constraint
- the pex file is really lightweight compared to full virtualenv (I think it's because virtualenv ship more things than pex, like *pip*, *easy_install* and *setuptools*)
- having the virtualenv activation in a file instead of using an *activate.sh* feels more natural
- I think you can do some cool things with Python subprocesses that use different dependencies than the parent process

I'm eager to see what pex can do
but I will personally experiment a bit more with it before using it in production.

## A word about pyenv and dephell

### pyenv: Python version manager

[pyenv](https://github.com/pyenv/pyenv) allow you to have multiple Python versions
in your system (for example Cpython 2.7 - Cpython 3.6 - pypy3.6).
If you've done some NodeJS, it's exactly the same as [nvm](https://github.com/nvm-sh/nvm).

I finally installed it in all my laptops 
after I messed up with the Python used by the OS:
now I don't have problems anymore.
It's super useful when developing.

### The ultimate problem solver: dephell

I haven't tried [dephell](https://github.com/dephell/dephell),
the project promise a lot but I would like to try it some day.

## Conclusions

From my experience, and what I saw:

- Python dependency management still don't have a unique good solution
- We saw some new promising tools that try to tackle this

Some recommendations:

- Always use at least a virtualenv: 
it will save from you a lot of troubles
- Use pyenv in your dev laptop:
I didn't expand on it, but it's a must
- Use poetry if you can:
it has been working very well for us and I think it's pushing toward good practices


