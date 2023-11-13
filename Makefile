# ======================================================================================
# Linting
# ======================================================================================
.PHONY: ruff-checker
ruff-checker:  ##@Linting Runs ruff checker against the codebase
	@echo "Running ruff checker..."
	@ruff check ./ --fix --no-cache --respect-gitignore
	@echo "Ruff checker done."


.PHONY: ruff-formatter
ruff-formatter:  ##@Linting Runs ruff formatter against the codebase
	@echo "Running ruff formatter..."
	@ruff format ./ --no-cache --respect-gitignore
	@echo "Ruff formatter done."


.PHONY: ruff
ruff:  ##@Linting Runs all ruff linters against the codebase
	@$(MAKE) ruff-checker
	@$(MAKE) ruff-formatter


# ======================================================================================
# Typing
# ======================================================================================
.PHONY: mypy
mypy:  ##@Typing Runs mypy static type checker against the codebase
	@echo "Running mypy..."
	@mypy -p vtex --pretty --install-types --non-interactive
	@echo "Mypy done."


# ======================================================================================
# Releasing
# ======================================================================================
.PHONY: clear
clear:  ##@Releasing Clears the dist directory
	@echo "Clearing the dist directory..."
	@rm -rf dist/
	@echo "Directory cleared."

.PHONY: build
build:  ##@Releasing Builds the python package into the dist directory
	@echo "Building the package..."
	@poetry build
	@echo "Package build."


.PHONY: publish
publish:  ##@Releasing Publishes the built package from the dist directory
	@echo "Publishing the package..."
	@poetry publish
	@echo "Package published."


# ======================================================================================
# Help  -  https://stackoverflow.com/a/30796664
# ======================================================================================
HELP_FUN = \
    %help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
    if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for sort keys %help; \

.PHONY: help
help: ##@Help Show this help
	@echo "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)
