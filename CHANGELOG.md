# v3.3.0
### Version highlights:
1. Added CHANGELOG to track versions, issues and improvements.

### New features:
- User

# v3.2.2
#### Notes
Minor fixes. Changed raise exception in case of unsupported Python version for warning to allow users that have TTL backported to run the SDK.

# v3.2.1
#### Notes
Improvements and refactoring.

# v3.1.1
#### Notes
Bugfixes and corrections.


# v3.1.0
#### Major changes
 1. Updated support for OneView API V300 and HPE Synergy.
 2. Updated support for HPE Synergy Image Streamer REST API.

# v3.0.0
#### Major changes
 1. Added support for OneView API300 and HPE Synergy to resources previously supported.
 2. Added support for new HPE Synergy exclusive resources.
 3. Partial support for HPE Synergy Image Streamer REST API.

# v2.0.0
#### Major changes
 1. HPE Rebranding
 2. Core Architecture Refactoring
   - PEP8 compliant
   - Support for both Python 2.7 and 3.x
   - Developer friendly interface
   - Standardization for building new endpoint clients
   - Core client implementation
   - Support for Python’s logging library
   - Added possibility to load connection settings from configuration file
   - Simple access to OneView API endpoints through OneViewClient module
 3. Added developer-focused samples
 4. Continuous Integration
   - Integration with Travis-CI Server
   - Automatized build / unit test execution on every Pull Request

# v1.0.0
#### Notes
 This is the first release of the OneView SDK in Python and it adds support to core features listed bellow.
 This version of the SDK supports OneView appliances with versions 2.00.00 or higher, using the OneView Rest API version 120 or 200.

#### Features supported
 - Ethernet network
 - FC network
 - FCOE network
 - Network set
 - Connection template
 - Fabric
 - SAN manager
 - Managed SAN
 - Interconnect
 - Logical interconnect
 - Logical interconnect group
 - Uplink set
 - Logical downlink
 - Enclosure
 - Logical enclosure
 - Enclosure group
 - Firmware bundle
 - Firmware driver
 - Storage system
 - Storage pool
 - Volume
 - Volume template
 - Datacenter
 - Racks
 - Logical switch group
 - Logical switch
 - Switch
 - Power devices
 - Server profile
 - Server profile template
 - Server hardware
 - Server hardware type
 - Unmanaged devices