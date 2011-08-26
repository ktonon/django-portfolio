django-portfolio
================

django-portfolio is a reusable Django app for displaying your personal and professional projects in style.

Installation
------------

Install the Python package in whatever way you normally do.

Add these lines to your `INSTALLED_APPS` tuple

```python
INSTALLED_APPS = (
  # ...
  'django.contrib.markup',
  'portfolio',
)
```

Then do a `syncdb`.

Features
--------

* Group projects by skill.
* Group projects by named categories.
* Optional pull quotes for each project.
* Associate files with projects.
* List & Detail approach.
* Integration with Git repositories.
* Django command to resize all ProjectImages to specified height / width.
