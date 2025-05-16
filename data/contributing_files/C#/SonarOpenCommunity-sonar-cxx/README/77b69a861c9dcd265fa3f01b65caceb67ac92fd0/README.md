|     |     |     |
| --- | --- | --- |
| **SonarCloud**<br>(Technical Debt analysis) | [![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=org.sonarsource.sonarqube-plugins.cxx%3Acxx&metric=alert_status)](https://sonarcloud.io/dashboard?id=org.sonarsource.sonarqube-plugins.cxx%3Acxx) | ![Coverage](https://sonarcloud.io/api/project_badges/measure?project=org.sonarsource.sonarqube-plugins.cxx%3Acxx&metric=coverage) |
| **DeepCode**<br>(real-time AI powered semantic code analysis) | [![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6IlNvbmFyT3BlbkNvbW11bml0eSIsInJlcG8xIjoic29uYXItY3h4IiwiaW5jbHVkZUxpbnQiOmZhbHNlLCJhdXRob3JJZCI6MTU1ODMsImlhdCI6MTYwMTI4MjcwOH0.Wz0G-HIoHfLfP1SjzxUnbyA598JfjKkQTsBqGG4Kleo)](https://www.deepcode.ai/app/gh/SonarOpenCommunity/sonar-cxx/_/dashboard?utm_content=gh%2FSonarOpenCommunity%2Fsonar-cxx) |
| **Travis CI**<br>(Linux Build and Integration Tests) | [![Build Status](https://travis-ci.org/SonarOpenCommunity/sonar-cxx.svg?branch=master)](https://travis-ci.org/SonarOpenCommunity/sonar-cxx) |   |
| **AppVeyor CI**<br>(Windows Build and Deployment) | [![Build status](https://ci.appveyor.com/api/projects/status/f6p12h9n59w01770/branch/master?svg=true)](https://ci.appveyor.com/project/SonarOpenCommunity/sonar-cxx/branch/master) | [Download latest snapshot](https://ci.appveyor.com/project/SonarOpenCommunity/sonar-cxx/branch/master/artifacts) |

## SonarQube C++ plugin (Community)

[SonarQube](https://www.sonarqube.org) is an open platform to manage code quality. This plugin
adds C++ support to SonarQube with the focus on integration of existing C++ tools.

This plugin is free software; you can redistribute it and/or modify it under the terms of the [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl-3.0.en.html) as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

* parser supporting C89, C99, C11, C++03, C++11, C++14 and C++17 standards
  * Microsoft extensions: C++/CLI, Attributed ATL
  * GNU extensions
  * CUDA extensions
* Microsoft Windows and Linux for runtime environment

Sensors for **static and dynamic code analysis**:
* Cppcheck warnings support (http://cppcheck.sourceforge.net/)
* GCC/G++ warnings support (https://gcc.gnu.org/)
* Visual Studio warnings support (https://www.visualstudio.com/)
* Visual Studio Core Guideline Checker warnings support
* Clang Static Analyzer support (https://clang-analyzer.llvm.org/)
* Clang Tidy warnings support (http://clang.llvm.org/extra/clang-tidy/)
* Infer warnings support (https://fbinfer.com/)
* PC-Lint warnings support (http://www.gimpel.com/)
* RATS (https://github.com/andrew-d/rough-auditing-tool-for-security)
* Valgrind (http://valgrind.org/)
* Vera++ (https://bitbucket.org/verateam/vera/wiki/Home)
* Dr. Memory warnings support (http://drmemory.org/)

**Test framework** sensors for:
* XUnit file format
* Google Test file format
* Boost.Test file format
* CppUnit file format
* VSTest file format
* NUnit file format
* extensions over XSLT possible

**Coverage** sensors for:
* Visual Studio coverage reports
* Bullseye coverage reports (http://www.bullseye.com/)
* Cobertura coverage reports (http://cobertura.github.io/cobertura/)
   * gcov / gcovr coverage reports --xml https://gcovr.com/en/stable/guide.html
   * OpenCppCoverage --export_type=cobertura (https://github.com/OpenCppCoverage/OpenCppCoverage/)
* Testwell CTC++ coverage reports (https://www.verifysoft.com/en_ctcpp.html)

Simple to **customize**
* provide the ability to write custom rules
* custom rules by XPath checks possible
* custom rules by regular expression checks possible
* easy 3rd party tool integration with XML rule definitions and reports possible


## Quickstart
1. Setup a SonarQube instance
2. Install the plugin (see [Installation](https://github.com/SonarOpenCommunity/sonar-cxx/wiki/Installation))
3. Run an analysis (see [Running the analysis](https://github.com/SonarOpenCommunity/sonar-cxx/wiki/Running-the-analysis))


## Resources
- [Latest release](https://github.com/SonarOpenCommunity/sonar-cxx/releases)
- [Documentation](https://github.com/SonarOpenCommunity/sonar-cxx/wiki)
- [Issue Tracker](https://github.com/SonarOpenCommunity/sonar-cxx/issues)
- [Continuous Integration Unix](https://travis-ci.org/SonarOpenCommunity/sonar-cxx)
- [Continuous Integration Windows](https://ci.appveyor.com/project/SonarOpenCommunity/sonar-cxx)
- [Sample project](https://github.com/SonarOpenCommunity/sonar-cxx/tree/master/sonar-cxx-plugin/src/samples/SampleProject)


## Alternatives:
That's not the only choice when you are looking for C++ support in SonarQube there is also
* the commercial [C/C++ plugin from SonarSource](http://www.sonarsource.com/products/plugins/languages/cpp/).
* the commercial [C/C++ plugin from CppDepend](http://www.cppdepend.com/sonarplugin)
* the [Coverity plugin](https://github.com/coverity/coverity-sonar-plugin)
* the commercial [PVS-Studio plugin](https://www.viva64.com/en/pvs-studio-download/)

Choose whatever fits your needs.

## Subscribe
Subscribe our [release feed](https://github.com/SonarOpenCommunity/sonar-cxx/releases.atom)
