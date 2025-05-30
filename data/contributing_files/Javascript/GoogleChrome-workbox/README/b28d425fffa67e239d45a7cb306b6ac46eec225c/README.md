<!-- DO NOT EDIT. This page is autogenerated. -->
<!-- To make changes, edit templates/README.hbs, not this file. -->
[![Travis Build Status][travis-image]][travis-url]
[![AppVeyor Build status][appveyor-image]][appveyor-url]
[![Dependency Status][dependency-image]][dependency-url]
[![Dev Dependency Status][dev-dependency-image]][dev-dependency-url]

# Welcome to Workbox

Workbox is a suite of helper libraries for service workers and progressive web
apps that lets you implement precaching in a manner of minutes. Its features
support runtime caching, routing, offline analytics, background syncing, and
more.

## A service worker in two minutes

Use [workbox-cli](workbox-cli) to add a service worker to an existing project in under two
minutes. 

## A build script in ten minutes

Generate a service worker in your build process
using [workbox-build](workbox-build).

## Much more

Go beyond the basics. If you'd like to use the Workbox libraries, and you
already have your own service worker, then checkout
[workbox-sw](workbox-sw) which lets
you add to what you've already got.

If you've been using Workbox for a while, or you're
ambitious, you can delve into its more advanced features. Browse the
[recipes section](recipes), try the [examples](examples), or look up
something in the [mobules reference](reference-docs/stable/latest/).

## Installing a library

Each library is installed separately using the command line [as listed below](#the-libraries). To use a particular library:

1. Install the library. For example:

   `npm install --save-dev workbox-sw`
2. Copy the library's JavaScript and map files to your serving directory. 

   `cp node_modules/workbox-sw/build/* app/`
3. Import the library to your service worker file. For example:

   `importScripts('workbox-sw.min.js');`

## The Libraries

All of the libraries are described below. Each has an _About_ page with basic usage instructions and a _Demo_ directory with an example. The main page of the documentation is [here](https://googlechrome.github.io/workbox/#main).

### workbox-background-sync

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-background-sync%22)][travis-url]

Queues failed requests and uses the Background Sync API to replay those requests at a later time when the network state has changed.

**Install**: `npm install --save-dev workbox-background-sync`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-background-sync.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-background-sync/demo)

### workbox-broadcast-cache-update

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-broadcast-cache-update%22)][travis-url]

A service worker helper library that uses the Broadcast Channel API to announce when two Response objects differ.

**Install**: `npm install --save-dev workbox-broadcast-cache-update`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-broadcast-cache-update.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-broadcast-cache-update/demo)

### workbox-build

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-build%22)][travis-url]

This module can be used to generate a file manifest or service worker, that can be used with workbox-sw.

**Install**: `npm install --save-dev workbox-build`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-build.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-build/demo)

### workbox-cache-expiration

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-cache-expiration%22)][travis-url]

Service worker helper library that expires cached responses based on age or maximum number of entries.

**Install**: `npm install --save-dev workbox-cache-expiration`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-cache-expiration.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-cache-expiration/demo)

### workbox-cacheable-response

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-cacheable-response%22)][travis-url]

This library takes a Response object and determines whether it&#x27;s cacheable, based on a specific configuration.

**Install**: `npm install --save-dev workbox-cacheable-response`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-cacheable-response.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-cacheable-response/demo)

### workbox-cli

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-cli%22)][travis-url]

A CLI tool to generate a service worker and a file manifest making use of the workbox-sw module.

**Install**: `npm install --global workbox-cli`



### workbox-google-analytics

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-google-analytics%22)][travis-url]

A service worker helper library to retry offline Google Analytics requests when a connection is available.

**Install**: `npm install --save-dev workbox-google-analytics`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-google-analytics.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-google-analytics/demo)

### workbox-precaching

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-precaching%22)][travis-url]

This library is still a work in progress and is not functional.

**Install**: `npm install --save-dev workbox-precaching`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-precaching.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-precaching/demo)

### workbox-routing

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-routing%22)][travis-url]

A service worker helper library to route request URLs to handlers.

**Install**: `npm install --save-dev workbox-routing`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-routing.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-routing/demo)

### workbox-runtime-caching

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-runtime-caching%22)][travis-url]

A service worker helper library that implements various runtime caching strategies.

**Install**: `npm install --save-dev workbox-runtime-caching`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-runtime-caching.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-runtime-caching/demo)

### workbox-sw

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-sw%22)][travis-url]

A service worker library to make managing fetch requests and caching as easy as possible.

**Install**: `npm install --save-dev workbox-sw`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-sw.html) •
                [Demo Code](https://github.com/GoogleChrome/workbox/tree/master/packages/workbox-sw/demo)

### workbox-webpack-plugin

[![Build Status](https://travis-shields.appspot.com/shield/GoogleChrome/workbox/master/PROJECT%3D%22workbox-webpack-plugin%22)][travis-url]

This is a webpack plugin for workbox-build

**Install**: `npm install --save-dev workbox-webpack-plugin`

**Learn More**: [About](https://googlechrome.github.io/workbox/reference-docs/stable/latest/module-workbox-webpack-plugin.html)


## External Contributions

Please read the [guide to contributing](https://googlechrome.github.io/workbox/contributing.html)
prior to filing any pull requests.

## License

Copyright 2016 Google, Inc.

Licensed under the [Apache License, Version 2.0](LICENSE) (the "License");
you may not use this file except in compliance with the License. You may
obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[npm-url]: https://npmjs.org/package/workbox
[npm-image]: https://badge.fury.io/js/workbox.svg
[travis-url]: https://travis-ci.org/GoogleChrome/workbox
[travis-image]: https://travis-ci.org/GoogleChrome/workbox.svg?branch=master
[appveyor-image]: https://ci.appveyor.com/api/projects/status/4ct8ph4d34c5ifnw?svg=true
[appveyor-url]: https://ci.appveyor.com/project/gauntface/workbox
[dependency-url]: https://david-dm.org/GoogleChrome/workbox/
[dependency-image]: https://david-dm.org/GoogleChrome/workbox/status.svg
[dev-dependency-url]: https://david-dm.org/GoogleChrome/workbox?type=dev
[dev-dependency-image]: https://david-dm.org/GoogleChrome/workbox/dev-status.svg
