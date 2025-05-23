# Welcome 💖

Before anything else, thank you for taking some of your precious time to help this project move forward. ❤️

If you're new to open source and feeling a bit nervous 😳, we understand! We recommend watching [this excellent guide](https://egghead.io/talks/git-how-to-make-your-first-open-source-contribution)
to give you a grounding in some of the basic concepts. We want you to feel safe to make mistakes, and ask questions.

If anything in this guide or anywhere else in the codebase doesn't make sense to you, please let us know! It's through your feedback that we can make this codebase more welcoming, so we'll be glad to hear thoughts.

You can chat with us in the [#committers-js](https://cucumberbdd.slack.com/archives/C612KCP1P) channel in our [Community Slack], or feel free to [raise an issue] if you're experiencing any friction trying make your contribution.

## Local setup

To get a local development environment:

* use [Git] to [fork and clone] the repo
* If you're running Windows, make sure to enable [Developer Mode]
* install [Node.Js](https://nodejs.org/en/)
* Make sure you have a recent version of `npm` installed: `npm install -g npm`
* `npm install` - Install dependencies
* `npm test` - Compile typescript and run the tests

If everything passes, you're ready to hack! ⛏

## Tests

Type `npm run` or see the `package.json` scripts section for how to run each category of tests.

* lint - `npm run lint`
  * [prettier](https://github.com/prettier/prettier)
  * [eslint](https://eslint.org/)
  * [dependency-lint](https://github.com/charlierudolph/dependency-lint)
* typescript tests - `npm run types-test`
  * [tsd](https://github.com/SamVerschueren/tsd)
* unit tests - `npm run unit-test`
  * [mocha](https://mochajs.org/)
  * [chai](https://www.chaijs.com/)
  * [sinon](https://sinonjs.org/)
* compatibility kit - `npm run cck-test`
  * checking that cucumber-js emits the [correct messages](https://github.com/cucumber/cucumber/tree/master/compatibility-kit)
* feature tests - `npm run feature-test`
  * cucumber-js tests itself

## Internals

### Project Structure

```
└── src
    │
    ├── cli                   # argv parsing, reading files
    │
    ├── formatter             # displaying the results
    │
    ├── models                # data structures
    │
    ├── runtime               # run test cases, emits the event protocol
    │
    └── support_code_library  # load hooks / step definitions
```

The runtime emits events with an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter)

### Coding style

* Promises and ES7 async/await
* Try to make things as unit testable as possible. If it's hard to unit test, the class/function may be doing too much.

## Changelog

* Every PR should have a changelog entry
* The contributor should update the changelog
* Each entry in the changelog should include a link to the relevant issues/PRs

[Community Slack]: https://cucumber.io/community#slack
[raise an issue]: https://github.com/cucumber/cucumber-js/issues/new/choose
[Developer Mode]: https://docs.microsoft.com/en-us/windows/apps/get-started/developer-mode-features-and-debugging
[fork and clone]: https://docs.github.com/en/get-started/quickstart/fork-a-repo
[Git]: https://docs.github.com/en/get-started/quickstart/set-up-git
