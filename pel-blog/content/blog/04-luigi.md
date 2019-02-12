Title: Working with Luigi
Slug: working-with-luigi
Date: 2017-12-30
Tags: python, luigi, pipelines
Status: published

![Luigi](https://luigi.readthedocs.io/en/stable/_static/luigi.png)

[//TODO]: <> (pass loaddataset task to externaltask)

[**Luigi**](https://github.com/spotify/luigi) is a workflow manager created by Spotify.
It is written completely in Python and is, to my opinion, a great way to do better data-science.

In this article, I'll try to show you why by working on a simple example:
training a statistical model on the Iris training set (link to iris dataset).

## How to start a Luigi project

The installation only require a simple `pip install luigi` here ;)

### Tasks and Target
First off, one thing I really like with Luigi is that it force you to take a minute
to focus on the unrolling of your project: what does it do? what are the steps followed?
how often should it run? does it connect to databases? what kind of intermediate or final
artifacts are produced?

You see, Luigi work with a system of **Task** and **Target**.

* A **Task** is a data-transforming operation.
    It may take data as input and produce some as output.
    It basically is the logic of your project.
* A **Target** represent one data artifact
    and can be used as input or output of Taskss.
    It's the CSV file you parse, the HDF5 file you load
    or maybe more interesting in industries,
    a PostGresSQL database or a Spark store.

Okay, the most important part here is that Tasks can be organised in an
Directed Acyclic Graph of Tasks.
When you trigger the run of a Task, it will check that all the Tasks
that comes to it are completed and run the ones that are not before running itself.
We'll see how it goes in the code later.

### Cutting down our process
Now, your problem can almost always be formulated with the 2 classes we saw.
Let's see how it goes with Iris:
![Tasks example](blog/04-luigi/tasks-target.png)

Simple enough, we download/parse the dataset in *LoadDataset*,
producing a CSV as Target,
this will feed *SplitDataset* that will produce 2 Numpy arrays
as Targets again.
*TrainModel* will end up training and evaluating a model statistical model
from the 2 .npz saving it in a final Target, a pickle file.

_But what are these Config and this PipelineTask? They are not in Luigi quick example._

Yes, I introduced 2 **Config** and a **WrapperTrask**.

* A **Config** serve to hold the parameter of a pipeline.
    They are easily accessible and good to avoid passing data objects all around in your code.
    With them, you setup once values like the path to data folder,
    path of Target, number of estimators, etc...
* A **WrapperTask** allow to encapsulate all your subjacent tasks in one,
    so you just have to call it to run the whole pipeline.

### Basis of a Task
In this paragrap, you'll learn nothing more than what is in Luigi's tutorial that
I recommend you to read (link to tutorial).

```python
class FooTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget('foo.txt')
    def requires(self):
        return {
            'bar': BarTask(),
            'zed': ZedTask()
        }
    def run(self):
        with self.input['bar'].open('r') as f:
            # Load your file
        # Do all your complicated computation
        with self.output.open('w') as f:
            # Create new artifact
```
So a Task in Luigi has always 3 methods:

* `output` that return an iterable of Target,
    corresponding to the artifacts the Task will create

* `requires` that return the Tasks that need to be completed before running
    this one.
    Multiple questions here:

    * how do I know a Task is complete?
        the base Task has a `.complete` method.
        It will check that every subjacent task is complete, and that its output exists.
        You can of course re-implement that
        method for your own use.

    * in what order are they going to be checked/executed?
        let's first remind that the task graph is acyclic, no loop are expected.
        Then, the `list`, `tuple`, `dict` (an iterable) you return from `.requires` will transformed
        into a list by iterating on it.
        So the order on which the items will be iterated on is the order of execution.

* `run` contains the logic of your Task.
    You can see here that I can access the output of the Tasks
    mentionned in `.requires` with `self.input` (note the use of a dict that allow
    to access with keys, not relying on an order)
    and the scheduled output of the Task with `self.output`.

### Config and WrapperTask

With just the part above, you are able to create your own pipeline.
However, I would like to show you here two elements that I find useful.

```python
class PathConfig(luigi.Config):
    iris_url =  luigi.Parameter(default='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    iris_csv = luigi.Parameter(default='iris.csv')
    pipeline_line = luigi.Parameter(default='pipeline-result.txt')
```

**Config** is a must to keep track of all the parameters you use in your program.
You can use subclasses of Parameter to check the type of the variable you introduce.
I personnaly always have something like this _PathConfig_ to hold all the filepath I use.
No need to search where is saved this Target or this other Target, it's all in the same class.
You can also save parameters for your models, your database configuration or your
infos about the time/place you run the script.
I've found it useful sometime to have Config classes whose attributes are instanciated
dynamically, to do so just implement the classic `__init__` method.

[//TODO]: <> (finish this example)
```python
class DynamicConfig(luigi.Config):
    static_path = luigi.Parameter(default=str(Path('my_file.txt')))
    def __init__(self, args, **kwargs):
        super()
```

[//TODO]: <> (does this class of task block some execution)
**WrapperTask** has nothing really interesting, it just contain a `.requires`
that hold the uppest node in your Task graph.
```python
class PipelineTask(luigi.Wrapper):
    def requires(self):
        return TrainModel()
    def run(self):
        print('Pipeline complete')
```
_So if it does nothing, why using it?_
Because of the way you call a Luigi Pipeline.

### Calling a Luigi pipeline
