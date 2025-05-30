![](Logo/header.png)
#### Reactive extensions to Cocoa frameworks, built on top of [ReactiveSwift][].

[![Carthage compatible](https://img.shields.io/badge/Carthage-compatible-4BC51D.svg?style=flat)](#carthage) [![CocoaPods compatible](https://img.shields.io/cocoapods/v/ReactiveCocoa.svg)](#cocoapods) [![GitHub release](https://img.shields.io/github/release/ReactiveCocoa/ReactiveCocoa.svg)](https://github.com/ReactiveCocoa/ReactiveCocoa/releases) ![Swift 3.0.x](https://img.shields.io/badge/Swift-3.0.x-orange.svg) ![platforms](https://img.shields.io/badge/platforms-iOS%20%7C%20OS%20X%20%7C%20watchOS%20%7C%20tvOS%20-lightgrey.svg)

⚠️ [Looking for the Objective-C API?][] ⚠️ [Still using Swift 2.x?][]

## What is ReactiveSwift?
__ReactiveSwift__ offers composable, declarative and flexible primitives that are built around the grand concept of ___streams of values over time___. These primitives can be used to uniformly represent common Cocoa and generic programming patterns that are fundamentally an act of observation.

For more information about the core primitives, see [ReactiveSwift][].

## What is ReactiveCocoa?

__ReactiveCocoa__ wraps various aspects of Cocoa frameworks with the declarative [ReactiveSwift][] primitives.

1. **UI Bindings**

	UI components exposes [`BindingTarget`][]s, which accept bindings from any
	kind of streams of values via the `<~` operator.

	```swift
	// Bind the `name` property of `person` to the text value of an `UILabel`.
	nameLabel.text <~ person.name
	```

1. **Controls and User Interactions**

	Interactive UI components expose [`Signal`][]s for control events
	and updates in the control value upon user interactions.
	
	A selected set of controls provide a convenience, expressive binding
	API for [`Action`][]s.
	
	
	```swift
	// Update `allowsCookies` whenever the toggle is flipped.
	preferences.allowsCookies <~ toggle.reactive.isOnValues 
	
	// Compute live character counts from the continuous stream of user initiated
	// changes in the text.
	textField.reactive.continuousTextValues.map { $0.characters.count }
	
	// Trigger `commit` whenever the button is pressed.
	button.reactive.pressed = CocoaAction(viewModel.commit)
	```
	
1. **Declarative Objective-C Dynamism**

	Create signals that are sourced by intercepting Objective-C objects,
	e.g. method call interception and object deinitialization.
	
	```swift
	// Notify after every time `viewWillAppear(_:)` is called.
	let appearing = view.reactive.trigger(for: #selector(viewWillAppear(_:)))
	
	// Observe the lifetime of `object`.
	object.reactive.lifetime.ended.observeCompleted(doCleanup)
	```

1. **Expressive, Safe Key Path Observation**

	Establish key-value observations in the form of [`SignalProducer`][]s and
	`DynamicProperty`s, and enjoy the inherited composability.
	
	```swift
	// A producer that sends the current value of `keyPath`, followed by
	// subsequent changes.
	//
	// Terminate the KVO observation if the lifetime of `self` ends.
	let producer = object.reactive.values(forKeyPath: #keyPath(key))
		.take(during: self.reactive.lifetime)
	
	// A parameterized property that represents the supplied key path of the
	// wrapped object. It holds a weak reference to the wrapped object.
	let property = DynamicProperty<String>(object: person,
	                                       keyPath: #keyPath(person.name))
	```

But there are still more to be discovered, and more to be introduced. Read our in-code documentations and release notes to
find out more.

## Getting started

ReactiveCocoa supports macOS 10.9+, iOS 8.0+, watchOS 2.0+, and tvOS 9.0+.

#### Carthage

If you are using [Carthage][] to manage your dependencies, simply add
ReactiveCocoa to your `Cartfile`:

```
github "ReactiveCocoa/ReactiveCocoa"
```

If you use Carthage to build your dependencies, make sure you have added `ReactiveCocoa.framework`, `ReactiveSwift.framework`, and `Result.framework` to the "_Linked Frameworks and Libraries_" section of your target, and have included them in your Carthage framework copying build phase.

#### CocoaPods

If you are using [CocoaPods][] to manage your dependencies, simply add
ReactiveCocoa to your `Podfile`:

```
pod 'ReactiveCocoa', :git => 'https://github.com/ReactiveCocoa/ReactiveCocoa.git'
```

#### Git submodule

 1. Add the ReactiveCocoa repository as a [submodule][] of your
    application’s repository.
 1. Run `git submodule update --init --recursive` from within the ReactiveCocoa folder.
 1. Drag and drop `ReactiveCocoa.xcodeproj`,
    `Carthage/Checkouts/ReactiveSwift/ReactiveSwift.xcodeproj`, and
    `Carthage/Checkouts/Result/Result.xcodeproj` into your application’s Xcode
    project or workspace.
 1. On the “General” tab of your application target’s settings, add
    `ReactiveCocoa.framework`, `ReactiveSwift.framework`, and `Result.framework`
    to the “Embedded Binaries” section.
 1. If your application target does not contain Swift code at all, you should also
    set the `EMBEDDED_CONTENT_CONTAINS_SWIFT` build setting to “Yes”.

## Have a question?
If you need any help, please visit our [GitHub issues][] or [Stack Overflow][]. Feel free to file an issue if you do not manage to find any solution from the archives.


[ReactiveSwift]: https://github.com/ReactiveCocoa/ReactiveSwift
[ReactiveObjC]: https://github.com/ReactiveCocoa/ReactiveObjC
[GitHub issues]: https://github.com/ReactiveCocoa/ReactiveCocoa/issues?q=is%3Aissue+label%3Aquestion+
[Stack Overflow]: http://stackoverflow.com/questions/tagged/reactive-cocoa
[CHANGELOG]: CHANGELOG.md
[Carthage]: https://github.com/Carthage/Carthage
[CocoaPods]: https://cocoapods.org/
[submodule]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[Looking for the Objective-C API?]: https://github.com/ReactiveCocoa/ReactiveObjC
[Still using Swift 2.x?]: https://github.com/ReactiveCocoa/ReactiveCocoa/tree/v4.0.0
[`Signal`]: https://github.com/ReactiveCocoa/ReactiveSwift/blob/master/Documentation/FrameworkOverview.md#signals
[`SignalProducer`]: https://github.com/ReactiveCocoa/ReactiveSwift/blob/master/Documentation/FrameworkOverview.md#signal-producers
[`Action`]: https://github.com/ReactiveCocoa/ReactiveSwift/blob/master/Documentation/FrameworkOverview.md#actions
[`BindingTarget`]: https://github.com/ReactiveCocoa/ReactiveSwift/blob/master/Documentation/FrameworkOverview.md#binding-target
