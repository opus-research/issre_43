Azure SDK for Java Contributing Guide
-------------------------------------

Thank you for your interest in contributing to Azure SDK for Java.

- For reporting bugs, requesting features, or asking for support, please file an issue in the [issues](https://github.com/Azure/azure-sdk-for-java/issues) section of the project.

- If you would like to become an active contributor to this project please follow the instructions provided in [Microsoft Azure Projects Contribution Guidelines](http://azure.github.com/guidelines.html).

- To make code changes, or contribute something new, please follow the [GitHub Forks / Pull requests model](https://help.github.com/articles/fork-a-repo/): Fork the repo, make the change and propose it back by submitting a pull request.

- Refer to the [wiki](https://github.com/Azure/azure-sdk-for-java/wiki/Building#testing-for-spotbugs-and-checkstyle-issues) to learn about how Azure SDK for java generates CheckStyle, SpotBugs, Jacoco, and JavaDoc reports.

- There are two Maven projects in the repo. Refer to the [wiki](https://github.com/Azure/azure-sdk-for-java/wiki/Building#pomclientxml-vs-pomdataxml) to learn about project structure for each.

Pull Requests
-------------

* **DO** submit all code changes via pull requests (PRs) rather than through a direct commit. PRs will be reviewed and potentially merged by the repo maintainers after a peer review that includes at least one maintainer.
* **DO NOT** submit "work in progress" PRs.  A PR should only be submitted when it is considered ready for review and subsequent merging by the contributor.
* **DO** give PRs short-but-descriptive names (e.g. "Improve code coverage for Azure.Core by 10%", not "Fix #1234")
* **DO** refer to any relevant issues, and include [keywords](https://help.github.com/articles/closing-issues-via-commit-messages/) that automatically close issues when the PR is merged.
* **DO** tag any users that should know about and/or review the change.
* **DO** ensure each commit successfully builds.  The entire PR must pass all tests in the Continuous Integration (CI) system before it'll be merged.
* **DO** address PR feedback in an additional commit(s) rather than amending the existing commits, and only rebase/squash them when necessary.  This makes it easier for reviewers to track changes.
* **DO** assume that ["Squash and Merge"](https://github.com/blog/2141-squash-your-commits) will be used to merge your commit unless you request otherwise in the PR.
* **DO NOT** fix merge conflicts using a merge commit. Prefer `git rebase`.
* **DO NOT** mix independent, unrelated changes in one PR. Separate real product/test code changes from larger code formatting/dead code removal changes. Separate unrelated fixes into separate PRs, especially if they are in different assemblies.

Merging Pull Requests (for project contributors with write access)
----------------------------------------------------------

* **DO** use ["Squash and Merge"](https://github.com/blog/2141-squash-your-commits) by default for individual contributions unless requested by the PR author.
  Do so, even if the PR contains only one commit. It creates a simpler history than "Create a Merge Commit".
  Reasons that PR authors may request "Merge and Commit" may include (but are not limited to):

  - The change is easier to understand as a series of focused commits. Each commit in the series must be buildable so as not to break `git bisect`.
  - Contributor is using an e-mail address other than the primary GitHub address and wants that preserved in the history. Contributor must be willing to squash
    the commits manually before acceptance.



## Developer Guide

### Pre-requisites

- Install Java Development Kit 8
  - add `JAVA_HOME` to environment variables
- Install [Maven](http://maven.apache.org/download.cgi)
  - add `MAVEN_HOME` to environment variables


>**Note:** If you are on `Windows`, enable paths longer than 260 characters by: <br><br>
1.- Run this as Administrator on a command prompt:<br> 
`REG ADD HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1`<br>*(might need to type `yes` to override key if it already exists)*<br><br>
2.- Set up `git` by running:<br> `git config --system core.longpaths true`

### Building and Testing

The easiest way to build is by running the following command from the root folder:
```
mvn -f pom.client.xml -Dgpg.skip -DskipTests clean install
```
- `-f pom.client.xml`: tells maven to target latest Azure SDK for Java project.
- `-Dgpg.skip`: disables [gpg](https://mran.microsoft.com/snapshot/2016-12-19/web/packages/gpg/vignettes/intro.html) signing.
- `-DskipTests:` Building without running unit tests would speed operation up, however, make sure all tests pass before creating a new PR.
- `clean:` will remove any previous generated output.
- `install:`  compiles project and installs it in the local Maven cache.

>**Note**: Refer to [wiki](https://github.com/Azure/azure-sdk-for-java/wiki/Building) for learning about how to build using Java 11

### Compiling one project only

```
mvn -f sdk/{projectForlderDir}/pom.xml -Dgpg.skip clean install

//example: mvn -f sdk/keyvault/azure-security-keyvault-keys/pom.xml clean install
```

## Versions and versioning

Tooling has been introduced to centralize versioning and help ease the pain of updating artifact versions in POM and README files. Under the eng\versioning directory there exists version text files, one for client ([version_client.txt](./eng/versioning/version_client.txt)) and one for data ([version_data.txt](./eng/versioning/version_data.txt)). The format of the version files is as follows:

`groupId:artifactId;dependency-version;current-version`

The dependency-version should be set to the most recent released version and the current-version is set to the next version to be released. For example:

`com.azure:azure-identity;1.0.0-preview.4;1.0.0-preview.5`

Note: In the case of a new artifact both versions will be the same. In the case of a released artifact, the dependecny version should be the latest released version.

### Libraries vs External Dependencies

Libraries refer to things that are built and released as part of the Azure SDK. Libraries have a current version and a dependency version.

External Dependencies refer to dependencies for things that are not built and released as part of the Azure SDK regardless of the source. External Dependencies will only ever have a dependency version.

### Current version, Dependency version and Unreleased Dependency version

Current version - This is the version we should be using when defining a component in its POM file and also when dependent components are built within the same pipeline. The current version is the version currently in development.
Dependency version - This is the version we should be using when a given library is a dependency outside of a particular area. This should be the latest released version of the package whenever possible.
Unreleased Dependency version – Whenever possible, libraries should be using the latest released version for dependencies but there is the case where active development in one library is going to be needed by another library or libraries that are built in separate pipelines. These types of changes are specifically additive and not breaking. Once a library has GA’d, nothing short of breaking changes should ever force the dependency versions across the repo to an unreleased version. The reason for this is that it would prevent other libraries, that don’t need this change, from releasing.

An example of Current vs Dependency versions: `com.azure:azure-storage-blob-batch` has dependencies on `com.azure:azure-core`, `com.azure:azure-core-http-netty` and `com.azure:azure-storage-blob`. Because `com.azure:azure-core` and `com.azure:azure-core-http-netty` are both built outside of azure-storage pipeline we should be using the released or *Dependency* versions of these when they're dependencies of another library. Similarly, libraries built as part of the same pipeline, that have interdependencies, should be using the Current version. Since `com.azure:azure-storage-blob-batch` and `com.azure:azure-storage-blob` are both built part of the azure-batch pipeline when `com.azure:azure-storage-blob` is declared as a dependency of `com.azure:azure-storage-blob-batch` it should be the *Current* version.

An example of an Unreleased Dependency version: Additive, not breaking, API changes have been made to `com.azure:azure-core`. `com.azure:azure-storage-blob` has a dependency on `com.azure:azure-core` and requires the additive API change that has not yet been released. An unreleased entry needs to be created in [version_client.txt](./eng/versioning/version_client.txt), under the unreleased section, with the following format: `unreleased_<groupId>:<artifactId>;dependency-version`, in this example that would be `unreleased_com.azure:azure-core;1.2.0` (this should match the 'current' version of core). The dependency update tags in the pom files that required this dependency would now reference `{x-version-update;unreleased_com.azure:azure-core;dependency}`. Once the updated library has been released the unreleased dependency version should be removed and the POM file update tags should be referencing the released version.

### Tooling, version files and marker tags

All of the tooling lives under the **eng\versioning** directory.

- version_client.txt - Contains the Client library and versions
- version_data.txt - Contains Data library and versions
- external_dependencies.txt - Contains the external dependency versions
- update_versions.py - This is just a basic python script that will climb through the source tree and update POM and README files. The script utilizes tags within the files to do replacements and the tags are slightly different between the POM and README files.
- set_versions.py - This script should only be used by the build system when we start producing nightly ops builds.

In POM files this is done by inserting a specifically formatted comment on the same line as the version element.

```xml
  <groupId>MyGroup</groupId>
  <artifactId>MyArtifact</artifactId>
  <version>1.0.0-preview.1</version> <!-- {x-version-update;MyGroup:MyArtifact;[current|dependency]} -->
```

The last element of the tag would be current or dependency depending on the criteria previously explained.

In README files this ends up being slightly different. Because the version tag is inside an XML element that we're explicitly telling a user to copy/paste into their product the comment tag really didn't make sense here. Instead there are tags before and after the XML element tags which effectively says "there's a version somewhere in between these two tags, when you find the line that matches replace it with the appropriate version of the group:artifact defined in the tag."

    [//]: # ({x-version-update-start;MyGroup:MyArtifact;dependency})
    ```xml
      <groupId>MyGroup</groupId>
      <artifactId>MyArtifact</artifactId>
      <version>1.0.0-preview.1</version>
    ```
    [//]: # ({x-version-update-end})

### What does the process look like?

Let's say we've GA'd and I need to tick up the version of azure-storage libraries how would I do it? Guidelines for incrementing versions after release can be found [here](https://github.com/Azure/azure-sdk/blob/master/docs/policies/releases.md#incrementing-after-release).

1. I'd open up eng\versioning\version_client.txt and update the current-versions of the libraries that are built and released as part of the azure storage pipeline. This list can be found in pom.service.xml under the sdk/storage directory. It's worth noting that any module entry starting with "../" are external module dependencies and not something that's released as part of the pipeline. Dependencies for library components outside of a given area would be downloading the appropriate dependency from Maven like we do for external dependencies.
2. Execute the update_versions python script from the root of the enlistment. The exact syntax and commands will vary based upon what is being changed and some examples can be found in the use cases in the [update_versions.py](./eng/versioning/update_versions.py#L6) file.
3. Review and submit a PR with the modified files.

### Next steps: Management plane

- Management plane. Management is in the process of being moved to service pipeline builds. The versioning work needs to wait until that work is finished.

### Making changes to an already GA'd library that require other libraries to depend on the unreleased version

This is where the `unreleased_` dependency tags come into play. Using the Unreleased Dependency example above, where `com.azure:azure-storage-blob` has a dependency on an unreleased `com.azure:azure-core`:

- [ ] Make the additive changes to `com.azure:azure-core`
- [ ] In [version_client.txt](./eng/versioning/version_client.txt) add the entry for the unreleased azure core in the unreleased section at the bottom of the file. The entry would look like `unreleased_com.azure:azure-core;<version>`.
      Note: The version of the library referenced in the unreleased version tag should match the current version of that library.
- [ ] In the pom.xml file for `com.azure:azure-storage-blob`, the dependency tag for `com.azure:azure-core` which was originally `{x-version-update;com.azure:azure-core-test;dependency}` would now become `{x-version-update;unreleased_com.azure:azure-core-test;dependency}`
After the unreleased version of `com.azure:azure-core` was released but before `com.azure:azure-storage-blob` has been released.
- [ ] In [version_client.txt](./eng/versioning/version_client.txt) the the dependency version of `com.azure:azure-core` would become the released version and the "unreleased_" entry, at this time, would be removed.
- [ ] In the pom.xml file for `com.azure:azure-storage-blob`, the dependency tag for `com.azure:azure-core` would get changed back to `{x-version-update;com.azure:azure-core-test;dependency}`

### Nightly package builds

Each night our engineering system produces a set of packages for each component of the SDK. These can be used by other projects to test updated builds of our libraries prior to their release. The packages are published to an Azure Artifacts public feed hosted at the following URL:

>> https://dev.azure.com/azure-sdk/public/_packaging?_a=feed&feed=azure-sdk-for-java

For developers working within the repo, refer to the instructions above for updating versions numbers correctly. The parent POM for the Azure SDK already contains a repository reference to the daily feed and can download the packages.

For developers wishing to use the daily packages for other purposes, refer to the [connect to feed instructions](https://dev.azure.com/azure-sdk/public/_packaging?_a=connect&feed=azure-sdk-for-java) in Azure Artifacts.

Note: the daily package feed is considered volatile and taking dependencies on a daily package should be considered a temporary arrangement. We reserve the right to remove packages from this feed at any point in time.
