# Makefile for the {{ cookiecutter.component_project }} project.
TMPDIR=/tmp/build/{{cookiecutter.component_project}}_build

local: setup
	# Doesn't (yet) do anything other than running the test and setup
	# targets

setup:
	# Calls the main setup.py to buld a source-distribution
	~/py_envs/{{cookiecutter.top_level_project}}/{{cookiecutter.short_name}}/bin/python setup.py sdist

unit_test:
	# Executes the unit-tests for the package, allowing the build-
	# process to die and stop the build if a test fails
	~/py_envs/{{cookiecutter.top_level_project}}/{{cookiecutter.short_name}}/bin/python setup.py test

build_dir:
	# Creates a temporary build-directory, copies the project-files
	# to it.
	# Creating "$(TMPDIR)"
	mkdir -p $(TMPDIR)
	# Copying project-files to $(TMPDIR)
	cp -R bin $(TMPDIR)
	cp -R etc $(TMPDIR)
	cp -R src $(TMPDIR)
	cp -R var $(TMPDIR)
	cp setup.py $(TMPDIR)

dev_prep:
	# Renames any dev-specific files so that they will be the "real"
	# files included in the build.
	# At this point, there are none, so we'll just exit

dev: unit_test build_dir dev_prep
	# A make-target that generates a build intended to be deployed
	# to a shared development environment.
	cd $(TMPDIR);~/py_envs/{{cookiecutter.top_level_project}}/{{cookiecutter.short_name}}/bin/python setup.py sdist