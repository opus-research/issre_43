<p align="center">
    <a href="https://sentry.io" target="_blank" align="center">
        <img src="https://sentry-brand.storage.googleapis.com/sentry-logo-black.png" width="280">
    </a>
</p>

_Bad software is everywhere, and we're tired of it. Sentry is on a mission to help developers write better software faster, so we can get back to enjoying technology. If you want to join us [<kbd>**Check out our open positions**</kbd>](https://sentry.io/careers/)_

# Official Sentry SDK for Python

[![Build Status](https://travis-ci.com/getsentry/sentry-python.svg?branch=master)](https://travis-ci.com/getsentry/sentry-python)
[![PyPi page link -- version](https://img.shields.io/pypi/v/sentry-sdk.svg)](https://pypi.python.org/pypi/sentry-sdk)
[![Discord](https://img.shields.io/discord/621778831602221064)](https://discord.gg/cWnMQeA)

This is the official Python SDK for [Sentry](http://sentry.io/)

---

## Versioning Policy

This project follows [semver](https://semver.org/), with three additions:

- Semver says that major version `0` can include breaking changes at any time. Still, it is common practice to assume that only `0.x` releases (minor versions) can contain breaking changes while `0.x.y` releases (patch versions) are used for backwards-compatible changes (bugfixes and features). This project also follows that practice.

- All undocumented APIs are considered internal. They are not part of this contract.

- Certain features (e.g. integrations) may be explicitly called out as "experimental" or "unstable" in the documentation. They come with their own versioning policy described in the documentation.

We recommend to pin your version requirements against `1.x.*` or `1.x.y`.
Either one of the following is fine:

```
sentry-sdk>=1.0.0,<2.0.0
sentry-sdk==1.5.0
```

A major release `N` implies the previous release `N-1` will no longer receive updates. We generally do not backport bugfixes to older versions unless they are security relevant. However, feel free to ask for backports of specific commits on the bugtracker.

## Migrate From sentry-raven

The old `raven-python` client has entered maintenance mode and was moved [here](https://github.com/getsentry/raven-python).

If you're using `raven-python`, we recommend you to migrate to this new SDK. You can find the benefits of migrating and how to do it in our [migration guide](https://docs.sentry.io/platforms/python/migration/).

## Getting Started

### Install

```bash
pip install --upgrade sentry-sdk
```

### Configuration

```python
import sentry_sdk

sentry_sdk.init(
    "https://12927b5f211046b575ee51fd8b1ac34f@o1.ingest.sentry.io/1",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
```

### Usage

```python
from sentry_sdk import capture_message
capture_message("Hello World")  # Will create an event in Sentry.

raise ValueError()  # Will also create an event in Sentry.
```

- To learn more about how to use the SDK [refer to our docs](https://docs.sentry.io/platforms/python/)
- Are you coming from raven-python? [Use this migration guide](https://docs.sentry.io/platforms/python/migration/)
- To learn about internals use the [API Reference](https://getsentry.github.io/sentry-python/)

## Integrations

- [Django](https://docs.sentry.io/platforms/python/guides/django/)
- [Flask](https://docs.sentry.io/platforms/python/guides/flask/)
- [Bottle](https://docs.sentry.io/platforms/python/guides/bottle/)
- [AWS Lambda](https://docs.sentry.io/platforms/python/guides/aws-lambda/)
- [Google Cloud Functions](https://docs.sentry.io/platforms/python/guides/gcp-functions/)
- [WSGI](https://docs.sentry.io/platforms/python/guides/wsgi/)
- [ASGI](https://docs.sentry.io/platforms/python/guides/asgi/)
- [AIOHTTP](https://docs.sentry.io/platforms/python/guides/aiohttp/)
- [RQ (Redis Queue)](https://docs.sentry.io/platforms/python/guides/rq/)
- [Celery](https://docs.sentry.io/platforms/python/guides/celery/)
- [Chalice](https://docs.sentry.io/platforms/python/guides/chalice/)
- [Falcon](https://docs.sentry.io/platforms/python/guides/falcon/)
- [Quart](https://docs.sentry.io/platforms/python/guides/quart/)
- [Sanic](https://docs.sentry.io/platforms/python/guides/sanic/)
- [Tornado](https://docs.sentry.io/platforms/python/guides/tornado/)
- [Tryton](https://docs.sentry.io/platforms/python/guides/tryton/)
- [Pyramid](https://docs.sentry.io/platforms/python/guides/pyramid/)
- [Logging](https://docs.sentry.io/platforms/python/guides/logging/)
- [Apache Airflow](https://docs.sentry.io/platforms/python/guides/airflow/)
- [Apache Beam](https://docs.sentry.io/platforms/python/guides/beam/)
- [Apache Spark](https://docs.sentry.io/platforms/python/guides/pyspark/)

## Contributing to the SDK

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## Getting help/support

If you need help setting up or configuring the Python SDK (or anything else in the Sentry universe) please head over to the [Sentry Community on Discord](https://discord.com/invite/Ww9hbqr). There is a ton of great people in our Discord community ready to help you!

## Resources

- [![Documentation](https://img.shields.io/badge/documentation-sentry.io-green.svg)](https://docs.sentry.io/quickstart/)
- [![Forum](https://img.shields.io/badge/forum-sentry-green.svg)](https://forum.sentry.io/c/sdks)
- [![Discord](https://img.shields.io/discord/621778831602221064)](https://discord.gg/Ww9hbqr)
- [![Stack Overflow](https://img.shields.io/badge/stack%20overflow-sentry-green.svg)](http://stackoverflow.com/questions/tagged/sentry)
- [![Twitter Follow](https://img.shields.io/twitter/follow/getsentry?label=getsentry&style=social)](https://twitter.com/intent/follow?screen_name=getsentry)

## License

Licensed under the BSD license, see [`LICENSE`](LICENSE)
