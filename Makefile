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
# Publishing
# ======================================================================================
.PHONY: build
build:  ##@Publishing Builds the python package into the dist directory
	@echo "Running poetry build..."
	@poetry build
	@echo "Poetry build done."


.PHONY: publish
publish:  ##@Publishing Publishes the built package from the dist directory
	@echo "Running poetry publish..."
	@poetry publish
	@echo "Poetry publish done."


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
