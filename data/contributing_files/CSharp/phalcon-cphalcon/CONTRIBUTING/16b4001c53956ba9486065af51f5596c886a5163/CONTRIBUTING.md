# Contributing to Phalcon

Phalcon is an open source project and a volunteer effort. Phalcon welcomes contribution from everyone

## Contributions

Contributions to Phalcon should be made in the form of GitHub pull requests. Each pull request will be reviewed by a core contributor (someone with permission to land patches) and either landed in the main tree or given feedback for changes that would be required. All contributions should follow this format, even those from core contributors.
*We only accept bug reports, new feature requests and pull requests in GitHub*.

## Pull Request Checklist

- Don't submit your pull requests to master. Branch from the required branch and, 
  if needed, rebase to the proper branch before submitting your pull request. 
  If it doesn't merge cleanly with master you may be asked to rebase your changes.

- Don't put submodule updates in your pull request unless they are to landed
  commits.

- Add tests relevant to the fixed bug or new feature. See our testing
  guide for more information.

- Phalcon 2 is written in [Zephir](http://zephir-lang.com/), please do not submit 
  commits that modify C generated files directly or those whose functionality/fixes 
  is implemented in C language

- Remove any change to ext/kernel / *.zep.c / *.zep.h files before submit the pull request

## Getting Support

If you have a question about how to use Phalcon, please see the [support page](http://phalconphp.com/support).

## Requesting Features

If you have a change or new feature in mind, please fill an [NFR](https://github.com/phalcon/cphalcon/wiki/New-Feature-Request---NFR).

Thanks! <br />
Phalcon Team
