Whats new in Python 3.7?
========================

Lightning talk about new features in Python 3.7.

How to run notebook?
--------------------

```
docker build -t jupyter37 .
docker run --rm -it -p 8888:8888 -v `pwd`:/data jupyter37 bash
```

How to run presentation?
------------------------

`jupyter nbconvert whats_new_in_python_37.ipynb --to slides --post serve`
