# Contributing to sentry-android

We love pull requests from everyone.

The project currently requires you run JDK version `1.8.x`.

To install spotlessCheck pre-commit hook:

```shell
git config core.hooksPath hooks/
```

To run the build and tests:

```shell
./gradlew build
```

Build and tests are automatically run against branches and pull requests
via TravisCI and AppVeyor.
