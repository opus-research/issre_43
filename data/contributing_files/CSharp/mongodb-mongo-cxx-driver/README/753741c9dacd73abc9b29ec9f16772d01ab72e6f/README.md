# MongoDB C++ Driver [![Build Status](https://travis-ci.org/mongodb/mongo-cxx-driver.svg?branch=master)](https://travis-ci.org/mongodb/mongo-cxx-driver)

Welcome to the MongoDB C++ Driver!

## Resources

* [MongoDB C++ Driver Quickstart](https://mongodb.github.io/mongo-cxx-driver/mongocxx-v3/tutorial/)
* [MongoDB C++ Driver Manual](https://mongodb.github.io/mongo-cxx-driver/)
* [MongoDB C++ Driver API Documentation](https://mongodb.github.io/mongo-cxx-driver/api/mongocxx-v3)
* [MongoDB C++ Driver Contribution guidelines](https://mongodb.github.io/mongo-cxx-driver/contributing/)
* [MongoDB Database Manual](http://docs.mongodb.com/manual/)

## Driver status by family and version

Stability indicates whether this driver is recommended for production use.
Currently, no drivers guarantee API or ABI stability.

| Family/version       | Stability   | Development         | Purpose                                                      |
| -------------------- | ----------- | ------------------- | ------------------------------------------------------------ |
| (repo master branch) | Unstable    | Active development  | New feature development                                      |
| mongocxx 3.1.x       | Stable      | Bug fixes only      | Current stable C++ driver release, requires C++11            |
| mongocxx 3.0.x       | Stable      | Critical fixes only | Previous stable C++ driver release, requires C++11           |
| legacy   (all)       | Stable      | Critical fixes only | Legacy API stable C++ driver release, no longer recommended  |

## MongoDB compatibility

The following compatibility table specifies the driver version(s)
recommended for different versions of MongoDB.  The mongocxx series
is recommended for all new development.

| Family/version | MongoDB 2.4 | MongoDB 2.6 | MongoDB 3.0 | MongoDB 3.2 | MongoDB 3.4 |
| -------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| mongocxx 3.1.x | ✓           | ✓           | ✓           | ✓           | ✓           |
| mongocxx 3.0.x | ✓           | ✓           | ✓           | ✓           |             |
| legacy   1.1.x | ✓           | ✓           | ✓           | ✓           |             |
| legacy   1.0.x | ✓           | ✓           | ✓           |             |             |

## Bugs and issues

See our [JIRA project](http://jira.mongodb.org/browse/CXX).

## License

The source files in this repository are made available under the terms of
the Apache License, version 2.0.
