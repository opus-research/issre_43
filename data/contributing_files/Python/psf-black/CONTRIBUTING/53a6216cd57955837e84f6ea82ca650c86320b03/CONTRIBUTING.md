# Contributing to _Black_

Welcome! Happy to see you willing to make the project better. Have you read the entire
[user documentation](https://black.readthedocs.io/en/latest/) yet?

## Bird's eye view

In terms of inspiration, _Black_ is about as configurable as _gofmt_. This is
deliberate.

Bug reports and fixes are always welcome! Please follow the
[issue template on GitHub](https://github.com/psf/black/issues/new) for best results.

Before you suggest a new feature or configuration knob, ask yourself why you want it. If
it enables better integration with some workflow, fixes an inconsistency, speeds things
up, and so on - go for it! On the other hand, if your answer is "because I don't like a
particular formatting" then you're not ready to embrace _Black_ yet. Such changes are
unlikely to get accepted. You can still try but prepare to be disappointed.

## Technicalities

Development on the latest version of Python is preferred. As of this writing it's 3.9.
You can use any operating system. I am using macOS myself and CentOS at work.

Install all development dependencies using:

```console
$ pipenv install --dev
$ pipenv shell
$ pre-commit install
```

If you haven't used `pipenv` before but are comfortable with virtualenvs, just run
`pip install pipenv` in the virtualenv you're already using and invoke the command above
from the cloned _Black_ repo. It will do the correct thing.

Non pipenv install works too:

```console
$ pip install -r test_requirements
$ pip install -e .[d]
```

Before submitting pull requests, run lints and tests with the following commands from
the root of the black repo:

```console
# Linting
$ pre-commit run -a

# Unit tests
$ tox -e py

# Optional Fuzz testing
$ tox -e fuzz

# Optional CI run to test your changes on many popular python projects
$ black-primer [-k -w /tmp/black_test_repos]
```

### News / Changelog Requirement

`Black` has CI that will check for an entry corresponding to your PR in `CHANGES.md`. If
you feel this PR not require a changelog entry please state that in a comment and a
maintainer can add a `skip news` label to make the CI pass. Otherwise, please ensure you
have a line in the following format:

```md
- `Black` is now more awesome (#X)
```

To workout X, checkout the latest issue and PR number and add 1. This is not perfect but
saves a lot of release overhead as now the releaser does not need to go back and workout
what to add to the `CHANGES.md` for each release.

_Suggestions welcome on how this could be a better less invasive flow._

### Docs Testing

If you make changes to docs, you can test they still build locally too.

```console
$ pip install -r docs/requirements.txt
$ pip install [-e] .[d]
$ sphinx-build -a -b html -W docs/ docs/_build/
```

## black-primer

`black-primer` is used by CI to pull down well-known _Black_ formatted projects and see
if we get source code changes. It will error on formatting changes or errors. Please run
before pushing your PR to see if you get the actions you would expect from _Black_ with
your PR. You may need to change
[primer.json](https://github.com/psf/black/blob/master/src/black_primer/primer.json)
configuration for it to pass.

For more `black-primer` information visit the
[documentation](https://github.com/psf/black/blob/master/docs/black_primer.md).

## Hygiene

If you're fixing a bug, add a test. Run it first to confirm it fails, then fix the bug,
run it again to confirm it's really fixed.

If adding a new feature, add a test. In fact, always add a test. But wait, before adding
any large feature, first open an issue for us to discuss the idea first.

## Finally

Thanks again for your interest in improving the project! You're taking action when most
people decide to sit and watch.
