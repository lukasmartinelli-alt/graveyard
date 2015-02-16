I recently had to write a User Defined Transform with Python in SAP.
This was my first experience of developing something with SAP and I have to say - this sucks! It sucks alot!

However there are a few tricks I learned along the way that make working
with SAP easier.

Do as much outside of SAP as you can.


Design them just like regular programs:

You should write them as if you create a small command line utilities (without arguments.)

```python
if __name__ == '__main__':
    pass
```

Check if script is executed under the SAP interpreter.

```python
def runs_in_sap():
    return sys.executable.endswith('al_engine.exe')
```

Write the mapping from and to the Data Records separately. This allow for
easy testing.

Use my testing framework.
