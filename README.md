# Project Setup

## 1. Bootstrap Script

This project includes a `bootstrap.sh` script to automate environment setup.

### What the Script Does
- Creates a Python virtual environment (`venv`)
- Activates the virtual environment
- Installs dependencies from `requirements.txt`

### How to Use

#### **Recommended:** Activate venv in your current shell

To set up and activate the virtual environment in your current shell, run:

```bash
source bootstrap.sh
```

This will:
- Create the `venv` if it doesn't exist
- Activate the `venv`
- Install all required packages

Your shell prompt should now show `(venv)`.

#### **Alternative:** Run in a subshell (not recommended for activation)

If you run:

```bash
bash bootstrap.sh
```

The environment will be set up, but you will **not remain in the virtual environment** after the script finishes.

### Manually Activating the venv

If you used `bash bootstrap.sh` or want to activate the venv later, run:

```bash
source venv/bin/activate
```

To exit the virtual environment, use:

```bash
deactivate
```
