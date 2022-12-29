# {{ cookiecutter.component_project.title().replace('_', ' ') }}

{{ cookiecutter.description }}

## Python Virtual Environment

**Create:** `python3 -m venv ~/py_envs/{{ cookiecutter.top_level_project }}/{{ cookiecutter.short_name }}`

**Activate:** `source ~/py_envs/{{ cookiecutter.top_level_project }}/{{ cookiecutter.short_name }}/bin/activate`

**Upgrade pip:** `pip install --upgrade pip`

## Build process

`python3 setup.py sdist` (source-distribution)