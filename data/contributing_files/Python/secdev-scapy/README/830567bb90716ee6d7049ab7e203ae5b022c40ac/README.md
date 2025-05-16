<p align="center">
<img src="doc/scapy_logo.png" width=200>
</p>

<!-- start_ppi_description -->

# Scapy

[![Travis Build Status](https://travis-ci.com/secdev/scapy.svg?branch=master)](https://travis-ci.com/secdev/scapy)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/secdev/scapy?svg=true)](https://ci.appveyor.com/project/secdev/scapy)
[![Codecov Status](https://codecov.io/gh/secdev/scapy/branch/master/graph/badge.svg)](https://codecov.io/gh/secdev/scapy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/30ee6772bb264a689a2604f5cdb0437b)](https://www.codacy.com/app/secdev/scapy?utm_source=github.com&utm_medium=referral&utm_content=secdev/scapy&utm_campaign=Badge_Grade)
[![PyPI Version](https://img.shields.io/pypi/v/scapy.svg)](https://pypi.python.org/pypi/scapy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/scapy.svg)](https://pypi.python.org/pypi/scapy/)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](LICENSE)
[![Join the chat at https://gitter.im/secdev/scapy](https://badges.gitter.im/secdev/scapy.svg)](https://gitter.im/secdev/scapy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Scapy is a powerful Python-based interactive packet manipulation program and
library.

It is able to forge or decode packets of a wide number of protocols, send them
on the wire, capture them, store or read them using pcap files, match requests
and replies, and much more. It is designed to allow fast packet prototyping by
using default values that work.

It can easily handle most classical tasks like scanning, tracerouting, probing,
unit tests, attacks or network discovery (it can replace `hping`, 85% of `nmap`,
`arpspoof`, `arp-sk`, `arping`, `tcpdump`, `wireshark`, `p0f`, etc.). It also
performs very well at a lot of other specific tasks that most other tools can't
handle, like sending invalid frames, injecting your own 802.11 frames, combining
techniques (VLAN hopping+ARP cache poisoning, VoIP decoding on WEP protected
channel, ...), etc.

Scapy supports Python 2.7 and Python 3 (3.4 to 3.7). It's intended to
be cross platform, and runs on many different platforms (Linux, OSX,
\*BSD, and Windows).

## Getting started

Head over to [the documentation](https://scapy.readthedocs.io/) to get started.

### Resources

The [documentation](http://scapy.readthedocs.io/en/latest/) contains more
advanced use cases, and examples.

Other useful resources:

- [the notebook hands-on](https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb)
-  [interactive tutorial](http://scapy.readthedocs.io/en/latest/usage.html#interactive-tutorial).
- [the quick demo: an interactive session](http://scapy.readthedocs.io/en/latest/introduction.html#quick-demo)
(some examples may be outdated)
- [HTTP/2 notebook](doc/notebooks/HTTP_2_Tuto.ipynb)
- [TLS notebook](doc/notebooks/tls)
notebooks.

## [Installation](http://scapy.readthedocs.io/en/latest/installation.html)

Scapy works without any external Python modules on Linux and BSD like operating
systems. On Windows, you need to install some mandatory dependencies as
described in [the
documentation](http://scapy.readthedocs.io/en/latest/installation.html#windows).

On most systems, using Scapy is as simple as running the following commands:

```bash
git clone https://github.com/secdev/scapy
cd scapy
./run_scapy
```

To benefit from all Scapy features, such as plotting, you might want to install
Python modules, such as `matplotlib` or `cryptography`. See the
[documentation](http://scapy.readthedocs.io/en/latest/installation.html) and
follow the instructions to install them.

<!-- stop_ppi_description -->

## Contributing

Want to contribute? Great! Please take a few minutes to
[read this](CONTRIBUTING.md)!
