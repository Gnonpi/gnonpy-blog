Title: Are you a data-scientist?
Slug: are-you-a-data-scientist
Date: 2019-06-12
Tags: career, data-science
Status: published

Last month, when discussing with my chief, he asked me:
> Do you want to change your title to 'software engineer'?

I was already thinking about this but told him to not bother changing
and I'm still a Data-scientist.

I saw a
[post on /r/datascience](https://www.reddit.com/r/datascience/comments/ays79x/has_anyone_switched_from_a_data_science_role_to_a/)
asking people if they switched from a data-science position to a software engineer one.

I made this shift progressively since summer 2018
and thought it could help someone to share about it.

## Team context and project

So I started working in this startup as a data-scientist intern
and at the end of my internship, I was hired as full-time data-scientist.

I worked on diverse projects that all had to do with machine-learning in some way
and then on a service of data-ingestion.
This was more already more of a classical software project:
it was a service handling requests,
that had to call other services,
communicate with a database
and process lots of data.
Then in summer 2018,
we had a project that involved putting trained models in production
to be reached by our clients via the main application.
After the models were ready,
we decided to create a new service to allow data-scientists to deploy their models.

I was put to lead this project.
Why me?
It had a lot to do with circumstances and planning
but also with a set of skills:

* being able to understand the needs of each model
* being able to design an API and communicate with others
* being able to create a production ready service
* being able to (de)serialize models

What weighted most in the balance were the last two points:
the data-scientist team worked with Python
and the main core team worked with NodeJS,
creating a service in Node that could read Python models
would have cost us much more time
than learning to create a Python service that read those models.

In a big company,
you could have found dozens of persons who could have done this.
But back then,
because my academic background was more "software engineering" focused
than the rest of the data-scientist who were closer to mathematicians,
I was the right candidate.

## Data-scientists need to go to production

<p align="center">
  <img alt="Repairing cars" src="{static}/images/cars-2-1450196.jpg">
</p>

There's tons of solutions to put models in production
but I noted a trend:
a lot of companies will propose to do it for you "as a service".
And I think it reflect one problem the data-scientist community still has to work on.

**"I got my model, now what?"**

Data-scientist need to work hand in hand with software engineers
to be able to deploy their models.
And I think there's a new kind of data-scientist that is appearing
who are enabling that next step.

Distinct roles are starting to appear in data-science:
you got the person who's super strong at modeling,
another who's more focused on feature engineering
or another one who's centered on the data extraction,
etc...
They got different skill set,
are solving different problems
and produce different results (a model, a combination of features, a dataset).
But they need to work hand in hand to produce something that will reach to production
(and so that will generate business value).

## For lack of a better term

So for the first months, I thought I shouldn't care about my title
until the boss of the startup asked my chief why I wasn't working
on the same project as people with the same title.

That was the moment to change title.

My chief and I made some researches
and in the end, came up with **"Analyst software engineer"**.

So, what I do everyday?
Roughly, I try to help my team of data-scientists:

* 70% of my time is about working on the ML service we created ;
  fixing bugs, adding new features (and introducing new bugs) and helping the data-scientists use it
* I come up with new tools to automate some of their manual steps
* and I try being the layer between the data-scientists and the rest of the team
so they can focus on what really matter.

Basically, every one of my tasks should either
automate a task of the DS guys or make work for other people easier.

---

---

Ok, so this is a piece I started to write long ago,
that suffered some rewriting with events happening,
I hope this can maybe help some people.
