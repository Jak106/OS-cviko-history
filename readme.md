<h1>History formatter</h1>
This is simple formatter for all history files from OS cvika.

<h2>Usage</h2>
<b>format.py</b> Add history files to folder with format script, change value on line 30 in format.py to name of teacher which you would like to create database from. After running this script it automatically rewrites database (commands.json)

<h3>index.html</h3>
Due to CORS rules in browsers, it is not possible to run html/js site and load data from database. This can be bypassed running live server. It requires having python installed in command line. You can check this by opening command line and run command 

```python```

If it opens python console, close it by running ```exit()```

Now run one of the following commands in folder where index.html is placed based on your system:

Windows:  
```python -m http.server```  

Ubuntu:  
```python3 -m http.server``` 

Arch:  
```python3 -m http.server```

Then open in browser:
[localhost:8000](http://127.0.0.1:8000/)

<h3>Website</h3>

In the top left corner there is filter button, click through options "Show all" "Show known" "Show unknown". Commands with green background are commands found in the tldr database. This means you need to be connected to the internet when launching site


