# Azure SDK for Java

[![Build Status](https://dev.azure.com/azure-sdk/public/_apis/build/status/17?branchName=master)](https://dev.azure.com/azure-sdk/public/_build/latest?definitionId=17) [![Build Documentation](https://img.shields.io/badge/documentation-published-blue.svg)](https://azuresdkartifacts.blob.core.windows.net/azure-sdk-for-java/index.html) [![Dependencies](https://img.shields.io/badge/dependencies-analyzed-blue.svg)](https://azuresdkartifacts.blob.core.windows.net/azure-sdk-for-java/staging/dependencies.html) [![SpotBugs](https://img.shields.io/badge/SpotBugs-Clean-success.svg)](https://azuresdkartifacts.blob.core.windows.net/azure-sdk-for-java/staging/spotbugsXml.html) [![CheckStyle](https://img.shields.io/badge/CheckStyle-Clean-success.svg)](https://azuresdkartifacts.blob.core.windows.net/azure-sdk-for-java/staging/checkstyle-aggregate.html)


This repository contains official Java libraries for Azure services. For reference documentation go to [Azure SDK for Java documentation](http://aka.ms/java-docs), and tutorials, samples, quick starts and other documentation, go to [Azure for Java Developers](https://docs.microsoft.com/java/azure/).

You can find a complete list of all the packages for these libraries [here](packages.md).

### Important 
The Azure SDK team is pleased to make available the November 2019 client library General Availability (GA) release. We strongly recommend using the GA libraries in all production environments as these libraries are well tested and officially supported by Microsoft. More details, including installation instructions can be found here [here](https://azure.github.io/azure-sdk/releases/2019-11/java.html).

## Getting started

To get started with a specific library, see the **README.md** file located in the library's project folder. You can find service libraries in the `/sdk` directory.

For tutorials, samples, quick starts and other documentation, visit [Azure for Java Developers](https://docs.microsoft.com/java/azure/).

### Prerequisites
Java 8 or later is required to use the November 2019 client libraries, otherwise Java 7 or later is required.

## Release branches (Release tagging)

### Master branch
The master branch has the most recent code with new features and bug fixes. It does **not** represent latest released **GA** SDK. See [below](#Client-GA-November-2019-Releases) for latest **GA** release.<br/>
For each package we release there will be a unique git tag created that contains the name and the version of the package to mark the commit of the code that produced the package. This tag will be used for servicing via hotfix branches as well as debugging the code for a particular preview or stable release version.
Format of the release tags are \<package-name\>_\<package-version\>. For more information please [see](https://github.com/Azure/azure-sdk/blob/master/docs/policies/repobranching.md#release-tagging)

## Latest Release
Each service might have a number of libraries available from each of the following categories:

- [Client: GA November 2019 Releases](#Client-GA-November-2019-Releases)
- [Client - Previous Versions](#Client-Previous-Versions)
- [Management](#Management)

### [Client: GA November 2019 Releases]
New wave of packages that were released in November 2019 client library as General Availability (GA) and several others that were released in **preview**. These libraries follow the [Azure SDK Design Guidelines for Java](https://azure.github.io/azure-sdk/java/guidelines/) and share a number of core features such as HTTP retries, logging, transport protocols, authentication protocols, etc., so that once you learn how to use these features in one client library, you will know how to use them in other client libraries. You can learn about these shared features [here](sdk/core/README.md). 

These libraries can be easily identified by sdk/ folder, package, and namespaces names starting with `azure-`, e.g. `azure-keyvault`.

The libraries released in the GA November 2019 release:
- [Identity](https://github.com/Azure/azure-sdk-for-java/blob/azure-identity_1.0.0/sdk/identity/azure-identity/README.md)
- [Key Vault Keys](https://github.com/Azure/azure-sdk-for-java/blob/azure-security-keyvault-keys_4.0.0/sdk/keyvault/azure-security-keyvault-keys/README.md)
- [Key Vault Secrets](https://github.com/Azure/azure-sdk-for-java/blob/azure-security-keyvault-secrets_4.0.0/sdk/keyvault/azure-security-keyvault-secrets/README.md)
- [Storage Blobs](https://github.com/Azure/azure-sdk-for-java/blob/azure-storage-blob_12.0.0/sdk/storage/azure-storage-blob/README.md)
- [Storage Blobs Batch](https://github.com/Azure/azure-sdk-for-java/blob/azure-storage-blob_12.0.0/sdk/storage/azure-storage-blob-batch/README.md)
- [Storage Blobs Cryptography](https://github.com/Azure/azure-sdk-for-java/blob/azure-storage-blob_12.0.0/sdk/storage/azure-storage-blob-cryptography/README.md)
- [Storage Queues](https://github.com/Azure/azure-sdk-for-java/blob/azure-storage-blob_12.0.0/sdk/storage/azure-storage-queue/README.md)

The libraries released in the November 2019 preview:
- [App Configuration](https://github.com/Azure/azure-sdk-for-java/tree/azure-data-appconfiguration_1.0.0-preview.6/sdk/appconfiguration/azure-data-appconfiguration)
- [Event Hubs](https://github.com/Azure/azure-sdk-for-java/blob/azure-messaging-eventhubs_5.0.0-preview.5/sdk/eventhubs/azure-messaging-eventhubs/README.md)
- [Event Hubs Checkpoint Store](https://github.com/Azure/azure-sdk-for-java/blob/azure-messaging-eventhubs-checkpointstore-blob_1.0.0-preview.3/sdk/eventhubs/azure-messaging-eventhubs-checkpointstore-blob/README.md)
- [Storage File Share](https://github.com/Azure/azure-sdk-for-java/blob/azure-storage-file-share_12.0.0-preview.5/sdk/storage/azure-storage-file-share/README.md)
- [Key Vault Certificates](https://github.com/Azure/azure-sdk-for-java/blob/azure-security-keyvault-certificates_4.0.0-preview.5/sdk/keyvault/azure-security-keyvault-certificates/README.md)
- [OpenCensus Tracing](https://github.com/Azure/azure-sdk-for-java/blob/azure-core-tracing-opencensus_1.0.0-preview.4/sdk/core/azure-core-tracing-opencensus/README.md)

> NOTE: If you need to ensure your code is ready for production use one of the stable, non-preview libraries.

### Client: Previous Versions
Last stable versions of packages that have been provided for usage with Azure and are production-ready. These libraries provide similar functionalities to the preview libraries, as they allow you to use and consume existing resources and interact with them, for example: upload a blob. Stable library directories start with `microsoft-azure-`, e.g. `microsoft-azure-keyvault`. They might not implement the [guidelines](https://azure.github.io/azure-sdk/java_introduction.html) or have the same feature set as the Novemeber releases. They do however offer wider coverage of services. 

### Management
Libraries which enable you to provision specific resources. They are responsible for directly mirroring and consuming Azure service's REST endpoints. Management library directories contain `-mgmt-`, e.g. `azure-mgmt-keyvault`.

## Need help?
* For reference documentation visit the [Azure SDK for Java documentation](http://aka.ms/java-docs).
* For tutorials, samples, quick starts and other documentation, visit [Azure for Java Developers](https://docs.microsoft.com/java/azure/).
* For build reports on code quality, test coverage, etc, visit [Azure Java SDK](https://azuresdkartifacts.blob.core.windows.net/azure-sdk-for-java/index.html).
* File an issue via [Github Issues](https://github.com/Azure/azure-sdk-for-java/issues/new/choose).
* Check [previous questions](https://stackoverflow.com/questions/tagged/azure-java-sdk) or ask new ones on StackOverflow using `azure-java-sdk` tag.

## Contributing
For details on contributing to this repository, see the [contributing guide](CONTRIBUTING.md).

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

![Impressions](https://azure-sdk-impressions.azurewebsites.net/api/impressions/azure-sdk-for-java%2FREADME.png)
