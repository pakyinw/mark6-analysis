# grabbing-mark6

## Run the program

### Create the virtual environment

Please ensure the PythonPath is setup.

```sh
virtualenv --no-site-packages venv
```

### Running the virtual env (Windows)

```sh
source venv/Scripts/activate
```

### Running the virtual env (MAC)

```sh
source venv/bin/activate
```

### Install the dependency

```sh
pip install -r requirements.txt
```

### Running the script

```sh
python analysis.py
```

### Save the virtual environment

```sh
pip freeze > requirements.txt
```

### Leaving the virtual env

```sh
deactivate
```

## log

| Date | Change |
|---|---|
| 26-Apr-2020  |  Remove pypuppeteer. Use requests. |
