# Minimal makefile for Sphinx documentation
#

define VSCODE_TASKS_JSON
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build Docs",
            "type": "shell",
            "command": "make",
            "args": [
                "html"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        }
    ]
}
endef

export VSCODE_TASKS_JSON
vscode:
	@mkdir -p .vscode
	@echo "$$VSCODE_TASKS_JSON" > .vscode/tasks.json

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
