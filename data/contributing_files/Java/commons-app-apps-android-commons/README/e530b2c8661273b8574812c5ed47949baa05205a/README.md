# Wikimedia Commons Android app [![Build status](https://api.travis-ci.org/commons-app/apps-android-commons.svg)](https://travis-ci.org/commons-app/apps-android-commons)

The Wikimedia Commons Android app allows users to upload pictures from their Android phone/tablet to Wikimedia Commons. Download the app [here][8], or view our [website][9].

Initially started by the Wikimedia Foundation, this app is now maintained by volunteers. Anyone is welcome to improve it, just choose among the [open issues](https://github.com/commons-app/apps-android-commons/issues) and send us a pull request :-) 

We are currently applying for an [IEG renewal][15] to work on the app for the next 6 months. Feedback is very much welcomed.

<a href="https://f-droid.org/repository/browse/?fdid=fr.free.nrw.commons" target="_blank">
<img src="https://f-droid.org/badge/get-it-on.png" alt="Get it on F-Droid" height="90"/></a>
<a href="https://play.google.com/store/apps/details?id=fr.free.nrw.commons" target="_blank">
<img src="https://play.google.com/intl/en_us/badges/images/generic/en-play-badge.png" alt="Get it on Google Play" height="90"/></a>


## Develop with Android Studio or IntelliJ ##

[Download Android Studio][1] (recommended) or [IntelliJ][2].

1. Open Android Studio/IntelliJ. Open the project:
	``File`` > ``New`` > ``Project from Version Control...`` > ``Git``  
	or  
	(From Quick Start menu): ``Check out project from Version Control``
2. Enter ``https://github.com/commons-app/apps-android-commons/`` as Git Repository URL. Specify a (new) local directory you would like to clone into and select ``OK``.

## Build Manually ##

### Requirements ###

1. Java SDK 8 (OpenJDK 8 or Oracle Java SE 8)
2. [Android SDK][3] (Level 23)
3. [Gradle][4]

### Build Instructions ###

1. Set the environment variable `ANDROID_HOME` to be the path to your Android SDK
2. Set the environment variable `JAVA_HOME` to the path to your Java SDK
3. Run `gradlew.bat assembleDebug` (Windows) or `./gradlew assembleDebug` (Mac / Linux) to build an unisgned apk
4. Alternatively, you can also connect your Android device via USB and install the app on it directly by running `gradlew.bat installDebug` (Windows) or `./gradlew installDebug` (Mac / Linux)

There are more thorough instructions on the [Android Developers website][5]

## License ##

This software is open source, licensed under the [Apache License 2.0][6].

## Code Structure ##

Key breakdowns:

Activities started within the UI:
* ContributionsActivity (ContributionsListFragment, MediaDetailPagerFragment, MediaDetailFragment) - main "my uploads" list and detail view
* LoginActivity - login screen when setting up an account
* SettingsActivity - settings screen
* AboutActivity - about screen

Activities receiving intents:
* ShareActivity (SingleUploadFragment, CategorizationFragment) - handles receiving a file from another app, accepting a title/desc, and slating it for upload
* MultipleShareActivity (MultipleUploadListFragment, CategorizationFragment) - handles receiving a batch of multiple files from another app, accepting a title/desc, and slating them for upload

Services:
* WikiAccountAuthenticatorService - authentication service
* UploadService - performs actual file uploads in background
* ContributionsSyncService - polls for updated contributions list from server
* ModificationsSyncService - pushes category additions up to server

Content providers:
* ContributionsContentProvider - private storage for local copy of user's contribution list
* ModificationsContentProvider - private storage for pending category and template modifications
* CategoryContentProvider - private storage for recently used categories


## On-Device Storage ##

Account credentials are encapsulated in an account provider. Currently only one Wikimedia Commons account is supported at a time. (Question: what is the actual storage for credentials?)

Preferences are stored in Android's SharedPreferences.

Information about past and pending uploads is stored in the Contributions content provider, which uses an SQLite database on the backend.

A list of recently-used categories is stored in the Categories content provider, which uses an SQLite database on the backend.

Captured files are not currently stored within the app, but are passed by content: or file: URI from other apps.

Thumbnail images are not currently cached.

## Translating the app ## 

Thanks to the translation work of many volunteers this app is available in a multitude of languages.

Translation of the text content of the Wikimedia Commons Android app happens on the [Commons Android App project][10] on [translatewiki.net][11]. If you want to help translate the app please create an account there (to get "translate rights" edit 20 [random keys][13] or ask in their [chat][14]). 

The translations from the translatewiki project are [periodically committed directly to this project][12] by the translatewiki team and later released with the normal updates to the Play Store.




[1]: https://developer.android.com/studio/index.html
[2]: http://www.jetbrains.com/idea/download/index.html
[3]: https://developer.android.com/sdk/index.html
[4]: http://gradle.org/gradle-download/
[5]: https://developer.android.com/studio/build/building-cmdline.html
[6]: https://www.apache.org/licenses/LICENSE-2.0
[7]: https://github.com/commons-app/apps-android-commons/issues
[8]: https://play.google.com/store/apps/details?id=fr.free.nrw.commons
[9]: https://commons-app.github.io/
[10]: https://translatewiki.net/w/i.php?title=Special:Translate&group=commons-android
[11]: https://translatewiki.net
[12]: https://github.com/commons-app/apps-android-commons/commits/master?author=translatewiki
[13]: https://translatewiki.net/wiki/Special:TranslationStash?
[14]: https://translatewiki.net/wiki/Special:WebChat
[15]: https://meta.wikimedia.org/wiki/Grants:Project/Improve_%27Upload_to_Commons%27_Android_App/Renewal
