# Documentation in the project
Documentation in the project is currently handled using
[Markdown](https://www.markdownguide.org/cheat-sheet) text files
is the docs directory, with the intention to move to
[Sphinx](http://www.sphinx-doc.org/en/master/).\
For this reason we will use sphinx compatible documentation in the code.\
In general, a typical `Sphinx` docstring has the following
[format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html):
```python
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```