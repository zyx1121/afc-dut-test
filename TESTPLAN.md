```
Use https://pdf2md.morethan.io/ to convert `AFC Device (DUT) Compliance Test Plan v1.7.pdf` to md.
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

### AFC Device (AFC DUT)

### Compliance Test Plan

### Version 1. 7

**WI-FI ALLIANCE PROPRIETARY – SUBJECT TO CHANGE WITHOUT NOTICE**

This document may be used with the permission of Wi-Fi Alliance under the terms set forth herein.

By your use of the document, you are agreeing to these terms. Unless this document is clearly designated

as an approved specification, this document is a work in process and is not an approved Wi-Fi Alliance

specification. This document is subject to revision or removal at any time without notice. Information

contained in this document may be used at your sole risk. Wi-Fi Alliance assumes no responsibility for

errors or omissions in this document. This copyright permission does not constitute an endorsement of

the products or services. Wi-Fi Alliance trademarks and certification marks may not be used unless

specifically allowed by Wi-Fi Alliance.

Wi-Fi Alliance has not conducted an independent intellectual property rights ("IPR") review of this

document and the information contained herein, and makes no representations or warranties regarding

IPR, including without limitation patents, copyrights or trade secret rights. This document may contain

inventions for which you must obtain licenses from third parties before making, using or selling the

inventions.

Wi-Fi Alliance owns the copyright in this document and reserves all rights therein. A user of this document

may duplicate and distribute copies of the document in connection with the authorized uses described

herein, provided any duplication in whole or in part includes the copyright notice and the disclaimer text

set forth herein. Unless prior written permission has been received from Wi-Fi Alliance, any other use of

this document and all other duplication and distribution of this document are prohibited. Unauthorized

use, duplication, or distribution is an infringement of Wi-Fi Alliance’s copyright.

NO REPRESENTATIONS OR WARRANTIES (WHETHER EXPRESS OR IMPLIED) ARE MADE BY WI-FI ALLIANCE

AND WI-FI ALLIANCE IS NOT LIABLE FOR AND HEREBY DISCLAIMS ANY DIRECT, INDIRECT, PUNITIVE,

SPECIAL, INCIDENTAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES ARISING OUT OF OR IN CONNECTION

WITH THE USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

### Document revision history

**Version Date YYYY-MM-DD Remarks**

1.0 2021 - 06 - 22 Approved Specification

##### 1.1 2021 - 12 - 06

```
Approved Specification, with following updates:
```

- Added list of compliance requirements to Section 1
- Updated Reference
- Updated Section 2 to add DUT Log File option
- Added Test Case IDs to Section 3 and revised all test sections accordingly
- Added a Compliance Requirement sub-section to all test sections
- Updated some Test Procedures
- Editorial updates

##### 1.2 2022 - 04 - 14

```
Approved Specification with following updates
```

- Inserted new subsection "1.3.1 Shall/should/may/might word usage”
- Applied clarification on available spectrum; updated Table 7, Section 3,
  Tables 8, 9, 13 & 15
- Editorial updates

##### 1.3 2022 - 11 - 01

```
Approved Specification, with following updates:
```

- Added Section 1.2, definition of device under test (DUT)
- Revised Figure 1 Test Configuration
- Corrected FCC Requirement references in Table 2
- Added Section 2.2.1 AFC DUT BSS Configuration
- Updated Section 3 text as related to compliance to spectral emissions
  when AFC DUT is using frequency-based requests
- Updated Test Procedures in Section 3 to include Initial Pre-test State

##### 1.4 2023 - 06 - 12

```
Approved Specification, with following updates:
```

- Added server validation security test case
- Updated test setup figures
- Updated test procedures for Fixed Client Device testing
- Updated Fixed Client device test procedure to indicate it can use In-band or
  Out-of-band methods for sending an Available Inquiry Request message.
- Added AFC DUT Test Harness package information to the references
- Editorial changes

##### 1.5 2023 - 06 - 27

```
Approved Specification, with following updates:
```

- Updated 3.1 test case to cover 47 CFR 15.407(k)(8)(iv) requirement
- Editorial changes

##### 1.6 2024 - 04 - 18

```
Approved Specification, with following updates:
```

- Updated to support ISED RSS-248 requirements for AFC Device certification
- Updated references to FCC KDB for 6GHz (Unlicensed Service Rules and
  Procedures)
- Corrected Maximum channel bandwidth to Occupied Channel bandwidth in
  Table 4

1. 7 2024 - 0616 Updated to support 320 MHz channel bandwidth

## © 20 24 Wi-Fi Alliance. All Rights Reserved.

Used with the permission of Wi-Fi Alliance under the terms as stated in this document.

© 20 24 Wi-Fi Alliance. All Rights Reserved.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

- 1 OVERVIEW Table of contents
  - 1.1 Scope and purpose
    - 1.1.1 NRA Compliance test requirements
    - 1.1.2 Out-of-scope requirements for AFC Devices
  - 1.2 AFC Device Under Test (DUT) Capabilities Declaration
  - 1.3 References
  - 1.4 Definitions, acronyms and abbreviations
    - 1.4.1 Shall/should/may/might word usage
    - 1.4.2 Abbreviations and acronyms
    - 1.4.3 Regulatory definitions
    - 1.4.4 AFC DUT compliance test plan definitions
- 2 TEST CONFIGURATION AND EQUIPMENT
  - 2.1 Test configuration
  - 2.2 AFC DUT equipment
    - 2.2.1 AFC DUT BSS Configuration
  - 2.3 Test equipment and test harness
    - 2.3.1 AFC DUT Test Harness
    - 2.3.2 RF test equipment
- 3 AFC DUT COMPLIANCE TESTS
  - 3.1 AFCD.RSA: Successful registration and spectrum access request
    - 3.1.1 Purpose and objective
    - 3.1.2 Compliance requirements
    - 3.1.3 Test method
    - 3.1.4 Test procedure.............................................................................................................................
  - 3.2 AFCD.USA: Unsuccessful spectrum access request
    - 3.2.1 Purpose and objective
    - 3.2.2 Compliance requirements
    - 3.2.3 Test method
  - 3.2.4 Test procedure............................................................................................................................. Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
- 3.3 AFCD.SAU: Successful spectrum access update
  - 3.3.1 Purpose and objective
  - 3.3.2 Compliance requirements
  - 3.3.3 Test method
  - 3.3.4 Test procedure.............................................................................................................................
- 3.4 AFCD.UAU: Unsuccessful spectrum access update
  - 3.4.1 Purpose and objective
  - 3.4.2 Compliance requirements
  - 3.4.3 Test method
  - 3.4.4 Test procedure.............................................................................................................................
- 3.5 AFCD.USV: Unsuccessful server validation
  - 3.5.1 Purpose and objective
  - 3.5.2 Compliance requirements
  - 3.5.3 Test method
  - 3.5.4 Test procedure.............................................................................................................................
- Table 1. FCC Compliance test requirements List of tables
- Table 2. ISED Compliance test requirements
- Table 3. Properties covered by manufacturer's test report for FCC
- Table 4. Properties covered by manufacturer's test report for ISED
- Table 5. Properties covered by manufacturer's test report or declaration for FCC
- Table 6. Properties covered by manufacturer's test report or declaration for ISED
- Table 7. Properties covered by manufacturer's declaration for FCC
- Table 8. Properties covered by manufacturer's declaration for ISED
- Table 9. AFCD general capabilities declaration
- Table 10. Abbreviations and acronyms
- Table 11. FCC definitions
- Table 12. ISED definitions
- Table 13. Definitions
- Table 14. AFC DUT BSS Configuration
- Table 15. FCC requirements tested in AFCD.RSA
- Table 16. ISED requirements tested in AFCD.RSA
- Table 17. Successful registration and spectrum access request
- Table 18. FCC requirements tested in AFCD.USA
- Table 19. ISED requirements tested in AFCD.USA
- Table 20. Unsuccessful spectrum access request
- Table 21. FCC requirements tested in AFCD.SAU
- Table 22. ISED requirements tested in AFCD.SAU
- Table 23. Successful spectrum access update
- Table 24. FCC requirements tested in AFCD.UAU
- Table 25. ISED requirements tested in AFCD.UAU
- Table 26. Unsuccessful spectrum access update
- Table 27. FCC requirements tested in AFCD.USV
- Table 28. ISED requirements tested in AFCD.RSA

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

Table 29. Unsuccessful server validation ............................................................................................................... 33

### List of figures

Figure 1. Standard Power Access Point Test Setup ........................................................................................... 17

Figure 2. Proxy representing one or more Standard Power Access Points Test Setup ................................ 18

Figure 3. Fixed Client Device Test Setup .............................................................................................................. 19

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

# 1 Overview

## This document describes a test methodology, equipment, and procedures based on the AFC System to AFC Device

## Interface Specification [4] that are recommended by Wi-Fi Alliance® used to ensure compliance of Standard Power

## Access Points (APs) and Fixed Client Devices subject to Automated Frequency Coordination (AFC) with requirements

## defined by regulatory bodies, such as the Federal Communications Commission (FCC) [3], Innovation, Science and

## Economic Development Canada (ISED) [6], for unlicensed operation in the 6 GHz band.

### 1.1 Scope and purpose

## This document defines test procedures for Standalone APs, Fixed Client Devices and Proxy components. Test vectors

## descriptions corresponding to the test procedures for AFC DUT, a compliance test plan for the AFC System (AFC SUT),

## and test vectors corresponding to the test procedure for AFC SUT are not in the scope of this document.

## This document describes procedures necessary to establish compliance with regulatory requirements, such as those

## established by the FCC, ISED or other regulatory bodies. Although based on the Wi-Fi Alliance AFC System to AFC Device

## Interface Specification [4], this document does not define conformance tests for that specification or guarantee

## interoperability. In particular, the procedures defined in this document do not exercise all optional information elements

## defined in [4] or include any tests of vendor-specific extensions.

## Discovery and authentication are not tested by the procedures described in this document. The AFC DUT and AFC DUT

## Test Harness used to perform the testing specified in this document are required to support and follow the

## authentication methods and procedures described in [4].

## RF performance requirements are not tested by the procedures described in this document.

## The ability of the AFC DUT to independently determine its location and location uncertainty are not tested by the

## procedures described in this document.

## The ability of the AFC DUT to contact the AFC system at least once per day, and cease transmission if it is unable to

## contact the AFC System after a grace period, is not tested by the procedures described in this document, and it is a

## manufacturer’s responsibility to demonstrate compliance.

#### 1.1.1 NRA Compliance test requirements

1.1.1.1 FCC

## Table 1 identifies the specific FCC requirements covered by each test defined in this document.

## Table 1. FCC Compliance test requirements

```
Test Description Test Case Identifier FCC Requirement Short Description
```

```
Successful registration and
spectrum access request
```

```
AFCD.RSA (3.1) 47 CFR Section 15.407(k)(1) Transmit only as instructed by AFC System
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System prior to initial transmission
```

```
47 CFR Section 15.407(k)(8)(ii) Provide required registration parameters
```

```
47 CFR Section 15.407(k)(8)(iii) Registration either directly or via proxy
```

```
47 CFR Section 15.407(l)(ii) Determination of appropriate channel configuration implied by
AFC System response
47 CFR 15.407(k)(8)(iv) Must contact an AFC system at least once per day to obtain the
latest list of available frequencies and the maximum permissible
power
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Test Description Test Case Identifier FCC Requirement Short Description
```

```
Unsuccessful spectrum
access request
```

```
AFCD.USA (3.2) 47 CFR Section 15.407(k)(1) Transmit only as instructed by AFC System
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System prior to initial transmission
```

```
47 CFR Section 15.407(k)(8)(ii) Provide required registration parameters
```

```
47 CFR Section 15.407(k)(8)(iii) Registration either directly or via proxy
```

```
Successful spectrum
access update
```

```
AFCD.SAU (3.3) 47 CFR Section 15.407(k)(8)(i) Register with AFC System after change of location
```

```
47 CFR Section 15.407(k)(8)(ii) Update AFC System upon change of registration parameters
```

```
47 CFR Section 15.407(k)(9)(i) Report location and uncertainty from power-off condition
```

```
Unsuccessful spectrum
access update
```

```
AFCD.UAU (3.4) 47 CFR Section 15.407(k)(8)(i) Register with AFC System after change of location
```

```
47 CFR Section 15.407(k)(8)(ii) Update AFC System upon change of registration parameters
```

```
47 CFR Section 15.407(k)(9)(i) Report location and uncertainty from power-off condition
```

```
Unsuccessful server
validation
```

```
AFCD.USV (3.5) 47 CFR Section 15.407(k)(8)(v) Incorporate adequate security measurements to prevent it from
accessing AFC systems not approved by the FCC
```

1.1.1.2 ISED

Table 2 identifies the specific ISED requirements [6] covered by each test defined in this document.

## Table 2. ISED Compliance test requirements

```
Test Description Test Case Identifier ISED Requirement Short Description
```

```
Successful registration and
spectrum access request
```

```
AFCD.RSA (3.1) RSS-248 Issue 2 Section 6 Prior to transmitting, a standard-power access point or fixed
client device shall access an AFC system to obtain both the
available frequencies and the maximum permissible power level
in each frequency range at its geographic coordinates.
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall only
transmit on the available range of frequencies and at their
respective maximum permissible power levels as specified by
the AFC system
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall
provide the registration information to the AFC system either
directly and individually, or through a combined registration
information representing multiple devices from the same
operating network.
RSS-248 Issue 2 Section 6 The standard-power access point, fixed client device or its
network element shall register with the AFC system via any
communication link, wired or wireless, outside the 5925-
6875 MHz frequency band
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
connect and register with and be authorized by an ISED
designated AFC system prior to its initial service transmission
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
provide the following device information to an AFC system:
```

- geographic coordinates (latitude and longitude) that
  lie within Canada
- geolocation uncertainty in meters with a confidence
  level of 95% or greater
- antenna height above ground level or above mean sea
  level (in meters)

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Test Description Test Case Identifier ISED Requirement Short Description**

- ISED identification number (IC ID) and
- manufacturer’s serial number

```
RSS-248 Issue 2 Section 6.2 A standard-power access point or fixed client device shall
contact an AFC system at least once every 24 hours to verify
that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 6. 2 If the AFC system indicates that the frequencies are no longer
available at the current power levels, the standard-power access
point or fixed client device shall immediately reduce its power
to permissible levels, as determined by the AFC system
RSS-248 Issue 2 Section 5 The geographic coordinates of the standard-power access point
or fixed client device shall be determined at the first activation
from a power-off condition
```

Unsuccessful spectrum
access request

```
AFCD.USA (3.2) RSS-248 Issue 2 Section 6 Prior to transmitting, a standard-power access point or fixed
client device shall access an AFC system to obtain both the
available frequencies and the maximum permissible power level
in each frequency range at its geographic coordinates.
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall only
transmit on the available range of frequencies and at their
respective maximum permissible power levels as specified by
the AFC system
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall
provide the registration information to the AFC system either
directly and individually, or through a combined registration
information representing multiple devices from the same
operating network.
RSS-248 Issue 2 Section 6 The standard-power access point, fixed client device or its
network element shall register with the AFC system via any
communication link, wired or wireless, outside the 5925-
6875 MHz frequency band
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
connect and register with and be authorized by an ISED
designated AFC system prior to its initial service transmission
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
provide the following device information to an AFC system:
```

- geographic coordinates (latitude and longitude) that
  lie within Canada
- geolocation uncertainty in meters with a confidence
  level of 95% or greater
- antenna height above ground level or above mean sea
  level (in meters)
- ISED identification number (IC ID) and
- manufacturer’s serial number

```
RSS-248 Issue 2 Section 6. 2 If the AFC system indicates that the frequencies are no longer
available at the current power levels, the standard-power access
point or fixed client device shall immediately stop operating at
those frequencies, as determined by the AFC system.
```

Successful spectrum
access update

```
AFCD.SAU (3.3) RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
connect and register with and be authorized by an ISED
designated AFC system prior to its initial service transmission
after installation or after a location change.
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Test Description Test Case Identifier ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 6.1 If any of the registered information changes, prior to resuming
operation, the standard-power access point or fixed client
device shall provide the updated information to an AFC system
RSS-248 Issue 2 Section 6. 2 A standard-power access point or fixed client device shall
contact an AFC system at least once every 24 hours to verify
that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 6. 1 If any of the registration information changes, prior to resuming
operation, the standard-power access point or fixed client
device shall provide the updated information to an AFC system.
RSS-248 Issue 2 Section 5 The geographic coordinates of the standard-power access point
or fixed client device shall be determined at the first activation
from a power-off condition
Unsuccessful spectrum
access update
```

```
AFCD.UAU (3.4) RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall
connect and register with and be authorized by an ISED
designated AFC system prior to its initial service transmission
after installation or after a location change.
RSS-248 Issue 2 Section 6.1 If any of the registered information changes, prior to resuming
operation, the standard-power access point or fixed client
device shall provide the updated information to an AFC system
RSS-248 Issue 2 Section 6.2 A standard-power access point or fixed client device shall
contact an AFC system at least once every 24 hours to verify
that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 6.1 If any of the registration information changes, prior to resuming
operation, the standard-power access point or fixed client
device shall provide the updated information to an AFC system.
RSS-248 Issue 2 Section 6.2 If the AFC system indicates that the frequencies are no longer
available at the current power levels, the standard-power access
point or fixed client device shall immediately stop operating at
those frequencies, as determined by the AFC system.
Unsuccessful server
validation
```

```
AFCD.USV (3.5) RSS-248 Issue 2 Section 8.1 Incorporate adequate security measurements to prevent it from
accessing AFC systems not approved by the ISED
```

#### 1.1.2 Out-of-scope requirements for AFC Devices

1.1.2.1 AFC Device properties covered by manufacturer device test report

The Part 15 requirements for AFC Devices in Table 3 are expected to be the subject of a customary manufacturer's test

report required by the FCC KDB for AFC Device Certification [8] and, as such, fall outside the scope of this document.

## Table 3. Properties covered by manufacturer's test report for FCC

```
Property Description FCC Requirement
```

```
Maximum transmit power 47 CFR Section 15.407(a)(4)
```

```
Maximum channel bandwidth 47 CFR Section 15.407(a)(10)
```

```
Out of band emissions 47 CFR Section 15.407(b)(5)
```

```
47 CFR Section 15.407(b)( 6 )
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Property Description FCC Requirement
```

```
Out of channel emissions 47 CFR Section 15.407(b)( 7 )
```

The RSS 248 requirements for AFC Devices [6] in Table 3 are expected to be the subject of a customary manufacturer's

test report required ISED RSS-248 for AFC Device Certification and, as such, fall outside the scope of this document.

## Table 4. Properties covered by manufacturer's test report for ISED

```
Property Description ISED Requirement
```

```
Maximum transmit power RSS-248 Issue 2 Section 4.
```

```
Occupied channel bandwidth RSS-248 Issue 2 Section 4. 4
```

```
Out of band emissions RSS-248 Issue 2 Section 4.6.
```

```
Out of channel emissions RSS-248 Issue 2 Section 4.6.
```

1.1.2.2 AFC Device properties covered by either manufacturer device test report or declaration

Part 15 requirements for AFC Devices in Table 5 may be tested in house or are considered not testable and therefore

subject to a customary manufacturer's product declaration. As such, they fall outside the scope of this document.

## Table 5. Properties covered by manufacturer's test report or declaration for FCC

```
Property Description FCC Requirement
```

```
Daily contact with AFC system and grace period 47 CFR Section 15.407(k)(8)(iv)
```

```
Automatic determination of geo-location 47 CFR Section 15.407(k)(9)(i)
```

```
Geo-location accuracy and uncertainty determination 47 CFR Section 15.407(k)(9)(iv)
```

For ISED AFC Device Certification [6], the RSS-248 requirements for AFC Devices in Table 5 may be tested or are

considered not testable and therefore subject to a customary manufacturer's product declaration. As such, they fall

outside the scope of this document.

## Table 6. Properties covered by manufacturer's test report or declaration for ISED

```
Property Description ISED Requirement
```

```
Daily contact with AFC system and grace period RSS-248 Issue 2 Section 6.
```

```
Automatic determination of geo-location RSS-248 Issue 2 Section 5.
```

```
Geo-location accuracy and uncertainty determination RSS-248 Issue 2 Section 5.
```

1.1.2.3 AFC Device properties covered by manufacturer declaration

The Part 15 requirements for AFC Devices in Table 7 are not testable and therefore subject to a customary

manufacturer's product declaration. As such, they fall outside the scope of this document.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

## Table 7. Properties covered by manufacturer's declaration for FCC

```
Property Description FCC Requirement
```

```
Security of AFC System and AFC devices, other than server certificate validation
of the AFC System (see AFCD.USV)
```

```
47 CFR Section 15.407(k)(8)(v)
```

```
Security of connection to external geo-location source 47 CFR Section 15.407(n)
```

```
Operating environment of AFC Device 47 CFR Section 15.407(d)
```

```
True, complete, correct, good faith provision of registration information 47 CFR Section 15.407(k)(8)(ii)
```

RSS-248 requirements for AFC Devices in Table 8 are not testable and therefore subject to a customary manufacturer's

product declaration. As such, they fall outside the scope of this document.

## Table 8. Properties covered by manufacturer's declaration for ISED

```
Property Description ISED Requirement
```

```
Security of AFC System and AFC devices, other than server certificate validation
of the AFC System (see AFCD.USV)
```

```
RSS- 248 Issue 2 Section 8 and 8.
```

```
Security of connection to external geo-location source RSS- 248 Issue 2 Section 5.
```

```
Operating environment of AFC Device RSS-248 Issue 2 Section 4.8.
```

```
True, complete, correct, good faith provision of registration information RSS-248 Issue 2 Section 6.
```

### 1.2 AFC Device Under Test (DUT) Capabilities Declaration

The Device Under Test shall be the AFC Device, designated as AFCD. The submitter of the AFCD shall declare its

capabilities per Table 9.

## Table 9. AFCD general capabilities declaration

```
Item Question Vendor response
```

```
1 AFC DUT Type Standalone AP/Proxy/Fixed Client
```

```
2 Does the AFC DUT supports sending an Available Spectrum Inquiry Request
based on the inquiredFrequencyRange field?
```

```
Yes/No
```

```
3 Does the AFC DUT supports sending an Available Spectrum Inquiry Request
based on the inquired Channels fields?
```

```
Yes/No
```

```
4 If the Answer to Items 2 and 3 is "Yes", what is AFC DUT's default inquiry type? Frequency based/Channel based/Both
```

```
5 Does the AFC DUT need to be supplied with BSS configuration parameters? Yes/No
```

```
6 Does the AFC DUT manufacturer attest to AFC DUT compliance with rules for
LPI operation?
```

```
Yes/No
```

```
7 Does the AFC DUT need to be supplied with mandatory registration
information to formulate an Available Spectrum Inquiry Request
```

```
Yes/No
```

```
8 If the Answer to Item 7 is "Yes". What is the geographic Supported by the AFC
DUT?
```

```
Ellipse/LinearPolygon/RadialPolygon
```

```
9 Does the AFC DUT support 160 MHz channel width operation? Yes/No
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Item Question Vendor response
```

```
10 Which method does AFC DUT acting as a Fixed Client uses for sending an
Available Spectrum Inquiry Request?
```

```
In-band/Out-of-band
```

```
11 Does the AFC DUT support 320 MHz channel width operation? Yes/No
```

### 1.3 References

Knowledge of the documents listed in this section is required for understanding this specification. If a reference includes

a date or a version identifier, only that specific version of the document is required. If the listing includes neither a date

nor a version identifier, then the latest version of the document is assumed. In the event of a conflict between this

specification and the following referenced documents, the contents of this specification take precedence.

[1] IEEE Std 802.11™- 2020 , IEEE Standard for Information Technology—Telecommunications and Information Exchange

```
between Systems Local and Metropolitan Area Networks—Specific Requirements, Part 11: Wireless LAN Medium
Access Control (MAC) and Physical Layer (PHY) Specifications Developed by the LAN/MAN Standards Committee of
the IEEE Computer Society, IEEE Std 802.11™- 2020 , Approved 3 December 2020,
https://ieeexplore.ieee.org/document/
```

[2] IEEE Std 802.11ax- 2021 , IEEE Standard for Information technology— Telecommunications and information exchange
between systems. Local and metropolitan area networks—Specific requirements, Part 11: Wireless LAN Medium
Access Control (MAC) and Physical Layer (PHY) Specifications, Amendment 1: Enhancements for High Efficiency
WLAN, Approved 9 February 2021, https://ieeexplore.ieee.org/document/

[3] 47 CFR § Section 15.407 - General technical requirements, https://www.ecfr.gov/cgi-bin/text-
idx?SID=dd52c4e608f6d7fac0d341398a32aeeb&mc=true&node=se47.1.15_1407&rgn=div

[4] Wi-Fi Alliance, AFC System to AFC Device Interface Specification, https://www.wi-fi.org/file/afc-specification-and-test-

plans

[5] AFC DUT Test Harness, https://www.wi-fi.org/file/afc-test-harness-package

[6] RSS- 248 - Radio Local Area Network (RLAN) Devices Operating in the 5925-7125 MHz— Band https://ised-

```
isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-
standards/radio-standards-specifications-rss/rss- 248 - radio-local-area-network-rlan-devices-operating- 5925 - 7125 -
mhz-band
```

[7] DBS- 06 — Automated Frequency Coordination (AFC) System Specifications for the 6 GHz (5925-6875 MHz)

```
Frequency Band — https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-
equipment/radio-equipment-standards/database-specifications-dbs/dbs- 06 - automated-frequency-coordination-afc-
system-specifications- 6 - ghz- 5925 - 6875 - mhz-frequency-band
```

[8] 987594 Unlicensed Service Rules and Procedures, UNII devices- 15.401, 08/22/2023,

https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=277034&switch=P

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

### 1.4 Definitions, acronyms and abbreviations

#### 1.4.1 Shall/should/may/might word usage

The words shall, should, and may are used intentionally throughout this document to identify the requirements for the

AFC Device (DUT) Compliance Test program. The words can and might shall not be used to define requirements.

The word _shall_ indicates a mandatory requirement. The word _must_ is used here in explicit reference to a text for a

regulatory requirement. In these cases, the word [shall] is added adjacent to these occurrences in the document.

The word _should_ denotes a recommended approach or action.

The word _may_ indicates a permitted approach or action with no implied preference.

The words _might_ and _can_ indicate a possibility or suggestion.

#### 1.4.2 Abbreviations and acronyms

Table 10 defines the abbreviations and acronyms used throughout this document. Some are commonly used in

publications and standards defining the operation of wireless local area networks, while others have been generated by

Wi-Fi Alliance.

## Table 10. Abbreviations and acronyms

```
Acronyms Definition
```

```
AFC Automated Frequency Coordination
```

```
AP Access Point
```

```
DUT Device Under Test
```

```
FCC Federal Communications Commission
```

```
LPI Low Power Indoor
```

```
NRA National Regulatory Authority
```

```
SP Standard Power
```

```
SUT System Under Test
```

#### 1.4.3 Regulatory definitions

The terms defined by regulatory domains are described in this section.

The terms defined by the FCC [3] described in Table 11 are used in this document.

## Table 11. FCC definitions

```
Term Definition
```

```
Access Point (AP) A U-NII transceiver that operates either as a bridge in a peer-to-peer connection or as a connector between the wired
and wireless segments of the network.
NOTE: For the purpose of this document, the terms "Access Point" or "AP" refer to those operating in the bands that
require AFC (i.e., 5.925-6.425 GHz and 6.525-6.875 GHz). Bands requiring AFC are subject to the rules adopted by the
FCC or other regulatory body.
Automated Frequency Coordination
(AFC) System
```

```
A system that automatically determines and provides lists of which frequencies and their associated maximum
permissible transmission power levels which are available for use by those access points operating in in the 5.925-
6.425 GHz and 6.525-6.875 GHz bands.
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Term Definition
```

```
Client Device A U-NII device whose transmissions are generally under the control of an access point and that is not capable of
initiating a network.
Fixed Client Device A client device intended as customer premise equipment that is permanently attached to a structure, operates only
on channels provided by an AFC System, has a geolocation capability, and complies with antenna pointing angle
requirements.
```

The terms defined by the ISED [6] described in Table 12 are used in this document.

## Table 12. ISED definitions

```
Term Definition
```

```
Access Point (AP) A transceiver that operates as either:
```

- a bridge in a peer-to-peer connection
- a connector between the wired and wireless segments of the network
- a relay between wireless network segments
  Automated Frequency Coordination
  (AFC) System

```
An ISED-designated database system that maintains records of protected licensed systems. The AFC system
determines a list of available frequencies and associated maximum power levels for use by a standard-power access
point or a fixed client device at a specific time and geographic location.
Client Device A device whose transmissions are under the control of an access point or an indoor subordinate device. Client devices
shall not be capable of initiating a network. Client devices include dual client devices, fixed client devices, low-power
client devices, and standard client devices.
Fixed Client Device A client device, intended as a customer premise equipment, that is permanently attached to a structure, has a
geolocation capability, operates as directed by an AFC system, and is only capable of connecting to a standard-power
access point.
```

#### 1.4.4 AFC DUT compliance test plan definitions

Table 13 lists the additional definitions that are applicable to this document.

## Table 13. Definitions

```
Term Definition
```

```
AFC Device Generic name of entities accessing AFC System and such entity includes a Standalone AP, a Proxy representing one or
more Non-standalone APs, and a Fixed Client Device.
AFC Device Under Test (AFC DUT) A Standalone AP, a Fixed Client Device, or a Proxy representing one or more Non-standalone APs, subjected to the
tests described in this document to establish compliance with requirements such as those specified by the FCC, ISED
or other regulatory body.
AFC DUT Test Harness An automated program or script exercised by a test operator to interact with an AFC DUT using interfaces defined in
[4]. The AFC DUT Test Harness emulates behavior of an AFC System and is used to automate procedures described in
this document.
Available Spectrum A radio frequency range in which a Standalone AP, Non-standalone AP or Fixed Client Device can operate at its
location within the power limits provided by the AFC, provided it does not exceed the lowest applicable regulatory
limits for in-band emissions and complies with regulatory limits for out-of-band emissions. For example, in the United
States, in-band (592 5 - 7125 MHz) power spectral density shall be suppressed by at least 40 dB relative to maximum in-
channel power spectral density, and out-of-band emissions (below 5925 MHz and above 7125 MHz) shall not exceed -
27 dBm/MHz (47 CFR 15.407(b)(6) and (7))[3]], RSS-248 Issue 2 Section 4.6.2 [6].
Non-standalone AP An Access Point which does not communicate with the AFC System directly and operates based on the information of
Available Spectrum provided by the AFC System via the Proxy.
Proxy An entity engaging in communications with the AFC System on behalf of one or more Non-standalone APs.
```

```
Regulatory Database A database that is managed by the NRA and that contains the information necessary for the calculation of Available
Spectrum.
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Term Definition**

Standalone AP An Access Point which communicates with the AFC System directly and operates based on the information of
Available Spectrum provided by the AFC System.

Initial Pre-test State The AFC DUT is required to configure its Radio to use the maximum DUT power capability that complies with
maximum permissible EIRP/PSD provided by the AFC DUT Test harness. Optionally, AFC DUT may have a test
regulatory identifier (e.g., FCC ID or IC ID), geographic coordinates, antenna height, and uncertainty, etc. to initiate an
Available Spectrum Inquiry Request when triggered from AFC DUT Test Harness. The AFC DUT is required to configure
only one chain active and turn off all remaining chains.

In-band For an AFC DUT seeking to be a Fixed Client: AFC DUT, acting as a Standard Client Device of an SP Access Point in 6
GHz band, transmitting an Available Spectrum Inquiry Request to the AFC DUT Test Harness.
Otherwise not applicable

Out-of-band For an AFC DUT seeking to be a Fixed Client: AFC DUT transmitting an Available Spectrum Inquiry Request to the AFC
DUT Test Harness via any wireless backhaul other than 6 GHz Wi-Fi.
Otherwise not applicable

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

## 2 TEST CONFIGURATION AND EQUIPMENT

This section introduces the test configurations and testbed components, of the Test Plan.

### 2.1 Test configuration

```
This document assumes the test configuration illustrated in Figure 1,Figure 2,Figure 3 support by the AFC DUT Test
Harness and AFC DUT for all mandatory elements of the Wi-Fi Alliance AFC System to AFC Device Interface Specification
[4], and RF test equipment capable of detecting and measuring transmissions in the 6 GHz band.
```

**Figure 1. Standard Power Access Point Test Setup**

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Figure 2. Proxy representing one or more Standard Power Access Points Test Setup**

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Figure 3. Fixed Client Device Test Setup**

### 2.2 AFC DUT equipment

The following equipment and methods are required to perform the test procedures described in this document:

- One Standalone AP, or one Fixed Client or one Proxy and one Non-standalone AP under its control
- A method to provide the AFC DUT with information it requires to identify the AFC DUT Test Harness as the AFC
  System with which it will communicate for the purposes of these tests
- A method to configure parameters used by the AFC DUT in the test procedures
- A method to trigger the AFC DUT to convey to the AFC DUT Test Harness an Available Spectrum Inquiry Request
  containing all mandatory information elements
- A method to return the AFC DUT to its Initial Pre-test State

#### 2.2.1 AFC DUT BSS Configuration

The BSS Configuration for Step 1 of compliance tests

## Table 14. AFC DUT BSS Configuration

```
Parameter Description Default Values
```

```
SSID Service Set Identifier AFC_Wi-Fi
```

```
Channel/Bandwidth Channel and Bandwidth ACS (Automatic Channel Selection)
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Parameter Description Default Values
```

```
Security 802.11 Security Method WPA3-Personal (SAE)
```

```
Password Password 12345678
```

### 2.3 Test equipment and test harness

The following test equipment is required to perform the procedures specified in this document.

#### 2.3.1 AFC DUT Test Harness

The AFC DUT Test Harness [5] shall be capable of sending predefined messages to the AFC DUT, validating the data in

mandatory fields with the expected (or pre-programmed) values defined in [4] for the requirements specified in each

test case, and generating a report indicating whether each test case passed or failed.

The AFC Test Harness is configured with the following TLS server configuration by default:

- TLS version 1.
- The mandatory cipher suites specified in Section 3.4.2 of [4] enabled
- A valid TLS server certificate with SAN entry equal to the domain name of the AFC System URL, signed by a root
  certificate
- OCSP stapling enabled

#### 2.3.2 RF test equipment

A spectrum analyzer shall be used to determine when, whether, at what power levels, and within what frequency ranges

an AFC DUT is transmitting throughout the duration of the tests.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

## 3 AFC DUT COMPLIANCE TESTS

This section provides the detailed test cases including test objectives, test environments, test configurations, test

procedures and pass/fail requirements relevant to this document.

Each test case is identified using the following format:

<Unit Under Test>.<Purpose>.<Test Case Number>

The Device Under Test shall be the AFC Device, designated as AFCD. The Purpose shall be a three-letter code

representing a purpose identified below.

- AFCD.RSA: Successful registration and spectrum access request
- AFCD.USA: Unsuccessful registration and spectrum access request
- AFCD.SAU: Successful spectrum access update
- AFCD.UAU: Unsuccessful spectrum access update
- AFCD.USV: Unsuccessful server validation

Where multiple tests are defined for a common purpose, sequential integers are used to identify each test case.

Each of the following test cases is mandatory for ensuring compliance of the AFC DUT with regulatory requirements for

operation in the 6 GHz band. Failure of any test case indicates non-compliance.

When AFC DUT is using frequency-based requests, its spectral emissions shall not exceed the power spectral density

contained in the availableFrequencyInfo field of an Available Spectrum Inquiry Response within the 3/2 channel

bandwidth from its channel center frequency. AFC DUT shall request and have power spectral density information within

3/2 channel bandwidth from its channel center frequency except for the frequency ranges that fall outside the bands

where Standard Power operation is available.

### 3.1 AFCD.RSA: Successful registration and spectrum access request

#### 3.1.1 Purpose and objective

Prior to its initial service transmission, an AFC DUT shall register with and be authorized by an AFC System and receive a

list of available frequencies and the maximum permissible power in each. This test validates compliance to the

registration requirement. This test also includes a second spectrum access request from AFC DUT to receive different set

of available frequencies and maximum permissible power levels. This second request is to verify conformance of AFC

DUT to spectrum access update in lieu of the 24 - hour refresh requirement.

#### 3.1.2 Compliance requirements

This test case validates that the AFC DUT meets the FCC requirements in Table 15 and ISED requirements in Table 16.

## Table 15. FCC requirements tested in AFCD.RSA

```
FCC Requirement Short Description
```

```
47 CFR Section 15.407(k)(1) Transmit only as instructed by AFC System
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System prior to initial transmission
```

```
47 CFR Section 15.407(k)(8)(ii) Provide required registration parameters
```

```
47 CFR Section 15.407(k)(8)(iii) Registration either directly or via proxy
```

```
47 CFR Section 15.407(l)(ii) Determination of appropriate channel configuration implied by AFC System response
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
FCC Requirement Short Description
```

```
47 CFR 15.407(k)(8)(iv) Must contact an AFC system at least once per day to obtain the latest list of available frequencies and
the maximum permissible power
```

## Table 16. ISED requirements tested in AFCD.RSA

```
ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 6 Prior to transmitting, a standard-power access point or fixed client device shall access an AFC system
to obtain both the available frequencies and the maximum permissible power level in each frequency
range at its geographic coordinates.
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall only transmit on the available range of
frequencies and at their respective maximum permissible power levels as specified by the AFC system
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall provide the registration information to
the AFC system either directly and individually, or through a combined registration information
representing multiple devices from the same operating network.
RSS-248 Issue 2 Section 6 The standard-power access point, fixed client device or its network element shall register with the
AFC system via any communication link, wired or wireless, outside the 5925- 6875 MHz frequency
band
RSS-248 Issue 2 Section 6. 1 A standard-power access point or fixed client device shall connect and register with and be
authorized by an ISED designated AFC system prior to its initial service transmission
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall provide the following device information to
an AFC system:
```

- geographic coordinates (latitude and longitude) that lie within Canada
- geolocation uncertainty in meters with a confidence level of 95% or greater
- antenna height above ground level or above mean sea level (in meters)
- ISED identification number (IC ID) and
- manufacturer’s serial number

```
RSS-248 Issue 2 Section 6.2 If the AFC system indicates that the frequencies are no longer available at the current power levels,
the standard-power access point or fixed client device shall immediately reduce its power to
permissible levels, as determined by the AFC system
RSS-248 Issue 2 Section 6.2 A standard-power access point or fixed client device shall contact an AFC system at least once every
24 hours to verify that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 5 The geographic coordinates of the standard-power access point or fixed client device shall be
determined at the first activation from a power-off condition
```

#### 3.1.3 Test method

Because the Wi-Fi Alliance AFC System to AFC Device Interface Specification [4] supports stateless implementations of

the AFC, each Available Spectrum Inquiry Request contains all of the information necessary for registration, including

geographic coordinates, antenna height, identification number, and unique manufacturer’s serial number.

In this test case, the AFC DUT Test Harness validates the registration information and all other mandatory fields of the

Available Spectrum Inquiry Request received from the AFC DUT and responds with an Available Spectrum Inquiry

Response containing a list of available frequencies and the maximum permissible power in each.

The RF Test Equipment monitors to determine that the AFC DUT transmission does not exceed LPI limits for DUT whose

manufacturer attests to its compliance with rules for LPI operation or the DUT does not begin transmission in the band

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

for SP only operation prior to AFC System authorization and that any subsequent transmissions conform to the

conditions of the Available Spectrum Inquiry Response.

#### 3.1.4 Test procedure.............................................................................................................................

\*If an AFC DUT supports sending an Available Spectrum Inquiry Request based on both the inquiredFrequencyRange and

the inquired Channels fields, but by default uses only one of the two fields, the test is repeated where the AFC DUT is

configured to use the other field.

Note: This test is repeated for all channel widths ((20 MHz, 40 MHz, 80 MHz, 160 MHz, and/or 320 MHz (if AFC DUT

declared support for 160 MHz, 320 MHz channel width in Table 9)) supported by the AFC DUT

Table 17 describes the successful registration and spectrum access request test procedure.

## Table 17. Successful registration and spectrum access request

```
Step Description Results
```

```
1 If the AFC DUT is Standard Power Access Point, go to Step 2, else go to Step 12 - -
```

```
2 AFC DUT set to Initial Pre-test State.
If needed (see Table 9 declaration), configure the AFC DUT with BSS parameters per Table 14 and a temporary test regulatory
identifier (e.g., FCC ID), geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request.
```

##### - -

```
3 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*.
```

```
Pass Fail
```

```
4 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail
```

```
5 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.
```

##### - -

```
6 Throughout Step 1 to Step 4, RF Test Equipment monitors the output of the AFC DUT to confirm that the AFC DUT does not
transmit:
```

- In the band if the AFC DUT supports only SP operation
  Or
- Above LPI limits for AFC DUT whose manufacturer attests to its compliance with rules for LPI operation
  Wait for 60 seconds
  RF Test Equipment monitors any transmission by the AFC DUT conforms to the following:
- For SP only operation, AFC DUT conforms to the conditions contained in the Available Spectrum Inquiry Response and
  does not exceed emissions limits in adjacent frequencies.
- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, AFC DUT transmit power in the
  band is less than CEILING [LPI limits, SP limits contained in the Available Spectrum Inquiry Response] and does not
  exceed emissions limits in adjacent frequencies.

```
Pass Fail
```

```
7 Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request.
```

```
8 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*.
```

```
Pass Fail
```

```
9 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail
```

```
10 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields which
are significantly different from Step 5.
```

##### - -

```
11 Wait for 5 minutes (configurable)
RF Test Equipment monitors any transmission by the AFC DUT conforms to the following:
```

- For SP only operation, AFC DUT conforms to the conditions contained in the latest Available Spectrum Inquiry Response
  and does not exceed emissions limits in adjacent frequencies.

```
Pass Fail
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Step Description Results
```

- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, AFC DUT transmit power in the
  band is less than CEILING [LPI limits, SP limits contained in the latest Available Spectrum Inquiry Response] and does not
  exceed emissions limits in adjacent frequencies.
  12 If the AFC DUT is Fixed Client, go to Step 13 else Stop the test - -

```
13 The AFC DUT set to Initial Pre-test State. - -
```

```
14 If needed (see Table 9 declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID), geographic
coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-
band methods.
```

##### - -

```
15 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*
```

```
Pass Fail
```

```
16 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail
```

```
17 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.
```

##### - -

```
18 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor
```

##### - -

```
19 Wait for 60 seconds
RF Test Equipment monitors any transmission by the AFC DUT conforms to the conditions contained in the Available Spectrum
Inquiry Response and does not exceed emissions limits in adjacent frequencies
```

```
Pass Fail
```

```
20 Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-
band methods
```

##### - -

```
21 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*
```

```
Pass Fail
```

```
22 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail
```

```
23 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields which
are significantly different from Step 17.
```

##### - -

```
24 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor
```

##### - -

```
25 Wait for 60 seconds (configurable)
RF Test Equipment monitors any transmission by the AFC DUT conforms to the conditions contained in the latest Available
Spectrum Inquiry Response and does not exceed emissions limits in adjacent frequencies
```

```
Pass Fail
```

### 3.2 AFCD.USA: Unsuccessful spectrum access request

#### 3.2.1 Purpose and objective

This test case validates that the AFC DUT refrains from operating in the band when the AFC System indicates that no

spectrum is available.

#### 3.2.2 Compliance requirements

This test case validates that the AFC DUT meets the FCC requirements in Table 18 and ISED requirements in Table 19:

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

## Table 18. FCC requirements tested in AFCD.USA

```
FCC Requirement Short Description
```

```
47 CFR Section 15.407(k)(1) Transmit only as instructed by AFC System
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System prior to initial transmission
```

```
47 CFR Section 15.407(k)(8)(ii) Provide required registration parameters
```

```
47 CFR Section 15.407(k)(8)(iii) Registration either directly or via proxy
```

## Table 19. ISED requirements tested in AFCD.USA

```
ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 6 Prior to transmitting, a standard-power access point or fixed client device shall access an AFC system
to obtain both the available frequencies and the maximum permissible power level in each frequency
range at its geographic coordinates.
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall only transmit on the available range of
frequencies and at their respective maximum permissible power levels as specified by the AFC system
RSS-248 Issue 2 Section 6 Standard-power access points and fixed client devices shall provide the registration information to
the AFC system either directly and individually, or through a combined registration information
representing multiple devices from the same operating network.
RSS-248 Issue 2 Section 6 The standard-power access point, fixed client device or its network element shall register with the
AFC system via any communication link, wired or wireless, outside the 5925- 6875 MHz frequency
band
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall connect and register with and be
authorized by an ISED designated AFC system prior to its initial service transmission
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall provide the following device information to
an AFC system:
```

- geographic coordinates (latitude and longitude) that lie within Canada
- geolocation uncertainty in meters with a confidence level of 95% or greater
- antenna height above ground level or above mean sea level (in meters)
- ISED identification number (IC ID) and
- manufacturer’s serial number

```
RSS-248 Issue 2 Section 6.2 If the AFC system indicates that the frequencies are no longer available at the current power levels,
the standard-power access point or fixed client device shall immediately stop operating at those
frequencies, as determined by the AFC system.
```

#### 3.2.3 Test method

The AFC Test Harness validates the registration information and all other mandatory fields of the Available Spectrum

Inquiry Request received from the AFC DUT. The AFC DUT Test Harness responds with an Available Spectrum Inquiry

Response indicating that no frequencies are available.

The RF Test Equipment monitors AFC DUT transmissions to determine that it refrains from operating within the band.

#### 3.2.4 Test procedure

For Available Spectrum Inquiry Request containing the inquiredFrequencyRange field, the AFC DUT Test Harness sets a

maxPsd value corresponding to the test procedure for AFC DUT.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

\*If an AFC DUT supports sending an Available Spectrum Inquiry Request based on both the inquiredFrequencyRange and

the inquired Channels fields, but by default uses only one of the two fields, the test is repeated where the DUT is

configured to use the other field.

Table 20 describes the unsuccessful spectrum access request test procedure.

## Table 20. Unsuccessful spectrum access request

```
Step Description Results
```

```
1 If the AFC DUT is Standard Power Access Point, go to Step 2, else go to Step 7
```

```
2 AFC DUT set to Initial Pre-test State.
If needed (see Table 9 declaration), configure the AFC DUT with BSS parameters per Table 14 and a temporary test regulatory
identifier (e.g., FCC ID), geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request.
```

##### - -

```
3 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*.
```

```
Pass Fail
```

```
4 AFC DUT Test Harness validates mandatory registration information. Pass Fail
```

```
5 AFC DUT Test Harness sends an Available Spectrum Inquiry Response indicating that no frequency ranges and/or channels are
available.
```

##### - -

```
6 Throughout Step 2 to Step 5 and subsequent to Step 5 , RF Test Equipment monitors the output of the AFC DUT to confirm the
following:
```

- For SP only operation, AFC DUT does not transmit in the band.
- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, the AFC DUT does not transmit
  above LPI limits.

```
Pass Fail
```

```
7 If the AFC DUT is Fixed Client, go to Step 8 else Stop the test - -
```

```
8 The AFC DUT set to Initial Pre-test State.
```

- -

```
9 If needed (see Table 9 declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID or IC ID),
geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request.
```

##### - -

```
10 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*.
```

```
Pass Fail
```

```
11 AFC DUT Test Harness validates mandatory registration information. Pass Fail
```

```
12 AFC DUT Test Harness sends an Available Spectrum Inquiry Response indicating that no frequency ranges and/or channels are
available using either In-band or Out-of-band methods.
```

##### - -

```
13 If AFC DUT used Out-of-band method, initiate connection procedure between Fixed Client and SP Access Point by following
instructions provided by the AFC DUT Vendor
13 Wait for 60 seconds
RF Test Equipment monitors that the AFC DUT does not transmit above maximum transmit power limits advertised by the
Standard Power Access Point for Standard Client Devices in the channel.
```

```
Pass Fail
```

## 3.3 AFCD.SAU: Successful spectrum access update

### 3.3.1 Purpose and objective

If any of the registration parameters of an AFC DUT change, it shall provide the updated parameters to the AFC System.

This test case validates that the AFC DUT meets these requirements and follows changes in spectrum availability

indicated by the AFC System.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

### 3.3.2 Compliance requirements

This test case validates that the AFC DUT meets the FCC requirements in Table 21 and ISED requirements in Table 22:

## Table 21. FCC requirements tested in AFCD.SAU

```
FCC Requirement Short Description
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System after change of location
```

```
47 CFR Section 15.407(k)(8)(ii) Update AFC System upon change of registration parameters
```

```
47 CFR Section 15.407(k)(9)(i) Report location and uncertainty from power-off condition
```

## Table 22. ISED requirements tested in AFCD.SAU

```
ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall connect and register with and be
authorized by an ISED designated AFC system prior to its initial service transmission after installation
or after a location change.
RSS-248 Issue 2 Section 6.1 If any of the registered information changes, prior to resuming operation, the standard-power access
point or fixed client device shall provide the updated information to an AFC system
RSS-248 Issue 2 Section 6.2 A standard-power access point or fixed client device shall contact an AFC system at least once every
24 hours to verify that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 6.1 If any of the registration information changes, prior to resuming operation, the standard-power
access point or fixed client device shall provide the updated information to an AFC system.
RSS-248 Issue 2 Section 5 The geographic coordinates of the standard-power access point or fixed client device shall be
determined at the first activation from a power-off condition
```

### 3.3.3 Test method

The AFC DUT Test Harness validates mandatory registration information provided by the AFC DUT and responds with an

Available Spectrum Inquiry Response containing significantly different list of available frequencies and the maximum

permissible power in each.

The RF Test Equipment monitors to determine that the AFC DUT transmission does not exceed LPI limits for AFC DUT

whose manufacturer attests to its compliance with rules for LPI operation or the AFC DUT does not begin transmission in

the band for SP only operation prior to initial AFC authorization and that any subsequent transmissions conform to the

conditions of the Available Spectrum Inquiry Response.

### 3.3.4 Test procedure.............................................................................................................................

\*If an AFC DUT supports sending an Available Spectrum Inquiry Request based on both the inquiredFrequencyRange and

the inquired Channels fields, but by default uses only one of the two fields, the test is repeated where the AFC DUT is

configured to use the other field.

Table 23 describes the successful spectrum access update test procedure.

## Table 23. Successful spectrum access update

```
Step Description Results
```

```
1 If the AFC DUT is Standard Power Access Point, go to Step 2, else go to Step 12
```

```
2 AFC DUT set to Initial Pre-test State.
If needed (see Table 9 declaration), configure the DUT with BSS parameters per Table 14 and a temporary test regulatory identifier
(e.g., FCC ID), geographic coordinates, antenna height, and uncertainty parameters.
```

##### - -

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Step Description Results**

```
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request.
```

3 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields\*.

```
Pass Fail
```

4 AFC DUT Harness validates mandatory registration information. Pass Fail

5 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.

##### - -

6 Throughout the preceding steps, RF Test Equipment monitors the output of the AFC DUT to confirm that the AFC DUT does not
transmit:

- In the band if the AFC DUT supports only SP operation
  Or
- Above LPI limits for AFC DUT whose manufacturer attests to its compliance with rules for LPI operation
  Wait for 60 seconds
  RF Test Equipment monitors any transmission by the AFC DUT conforms to the following:
- For SP only operation, AFC DUT conforms to the conditions contained in the Available Spectrum Inquiry Response and
  does not exceed emissions limits in adjacent frequencies.
- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, AFC DUT transmit power in the
  band is less than CEILING [LPI limits, SP limits contained in the Available Spectrum Inquiry Response] and does not
  exceed emissions limits in adjacent frequencies.

```
Pass Fail
```

7 AFC DUT is power cycled.

```
If needed (see Table 9declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID), new geographic
coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
```

##### - -

8 Wait for 60 seconds

```
If the AFC DUT does not send an Available Spectrum Inquiry Request, RF Test Equipment monitors the output of the AFC DUT to
verify the following and STOP the test
```

- For SP only operation, AFC DUT does not transmit in the band.
- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, the AFC DUT does not transmit
  above LPI limits.
  If the AFC DUT sends an Available Spectrum Inquiry Request, then CONTINUE with Step 9

```
Pass Fail
```

9 AFC DUT Test Harness evaluates validity of mandatory registration information Pass Fail

10 AFC DUT Test Harness waits for 60 seconds before sending an Available Spectrum Inquiry Response containing a list of available
frequency ranges and/or channels and the maximum permissible transmit power in the availableFrequencyInfo and/or
availableChannelInfo fields which are significantly different from Step 5.

- During the 60 seconds wait time:
  ▪ For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, RF Test Equipment monitors
  the output of the AFC DUT to confirm that AFC DUT does not transmit above LPI threshold limits
  ▪ For SP only operation, RF Test Equipment monitors the output of the AFC DUT to confirm that AFC DUT doesn’t
  transmit in the band

##### - -

11 Wait for 60 seconds

```
RF Test Equipment monitors any transmission by the AFC DUT conforms to the following:
```

- For SP only operation, AFC DUT conforms to the conditions contained in the Available Spectrum Inquiry Response and
  does not exceed emissions limits in adjacent frequencies.
- For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, AFC DUT transmit power in the
  band is less than CEILING [LPI limits, SP limits contained in the Available Spectrum Inquiry Response] and does not
  exceed emissions limits in adjacent frequencies.

```
Pass Fail
```

12 If the AFC DUT is Fixed Client, go to Step 13 else Stop the test

13 The AFC DUT set to Initial Pre-test State.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Step Description Results
```

```
14 If needed (see Table 9 declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID), geographic
coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-
band methods.
15 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields*
```

```
Pass Fail
```

```
16 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail
```

```
17 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.
18 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor
19 Wait for 60 seconds
RF Test Equipment monitors any transmission by the AFC DUT conforms to the conditions contained in the Available Spectrum
Inquiry Response and does not exceed emissions limits in adjacent frequencies
```

```
Pass Fail
```

```
20 AFC DUT is power cycled.
If needed (see Table 9 declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID), new
geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate
21 Wait for 60 seconds
If the AFC DUT does not send an Available Spectrum Inquiry Request, RF Test Equipment monitors the output of the AFC DUT to
verify the AFC DUT does not transmit above maximum transmit power limits advertised by the Standard Power Access Point for
Standard Client Devices in the channel and STOP the test.
If the AFC DUT sends an Available Spectrum Inquiry Request, then CONTINUE with Step 2 1
```

```
Pass Fail
```

```
22 AFC DUT Test Harness evaluates validity of mandatory registration information Pass Fail
```

```
23 AFC DUT Test Harness waits for 60 seconds before sending an Available Spectrum Inquiry Response containing a list of available
frequency ranges and/or channels and the maximum permissible transmit power in the availableFrequencyInfo and/or
availableChannelInfo fields which are significantly different from step 17.
During the 60 seconds wait time, RF Test Equipment monitors the output of the AFC DUT to confirm that the AFC DUT does not
transmit above maximum transmit power limits advertised by the Standard Power Access Point for Standard Client Devices in the
channel.
```

```
Pass Fail
```

```
24 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor
25 Wait for 60 seconds
RF Test Equipment monitors any transmission by the AFC DUT conforms to the conditions contained in the Available Spectrum
Inquiry Response and does not exceed emissions limits in adjacent frequencies
```

```
Pass Fail
```

## 3.4 AFCD.UAU: Unsuccessful spectrum access update

### 3.4.1 Purpose and objective

This test case validates that the AFC DUT refrains from operating in the band when the AFC System indicates that no

spectrum is available following a change in registration parameters.

### 3.4.2 Compliance requirements

This test case validates that the AFC DUT meets the FCC requirements in Table 24 and ISED requirements in Table 25:

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

## Table 24. FCC requirements tested in AFCD.UAU

```
FCC Requirement Short Description
```

```
47 CFR Section 15.407(k)(8)(i) Register with AFC System after change of location
```

```
47 CFR Section 15.407(k)(8)(ii) Update AFC System upon change of registration parameters
```

```
47 CFR Section 15.407(k)(9)(i) Report location and uncertainty from power-off condition
```

## Table 25. ISED requirements tested in AFCD.UAU

```
ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 6.1 A standard-power access point or fixed client device shall connect and register with and be
authorized by an ISED designated AFC system prior to its initial service transmission after installation
or after a location change.
RSS-248 Issue 2 Section 6.1 If any of the registered information changes, prior to resuming operation, the standard-power access
point or fixed client device shall provide the updated information to an AFC system
RSS-248 Issue 2 Section 6.2 A standard-power access point or fixed client device shall contact an AFC system at least once every
24 hours to verify that the available frequencies and power levels are up to date.
RSS-248 Issue 2 Section 6.1 If any of the registration information changes, prior to resuming operation, the standard-power
access point or fixed client device shall provide the updated information to an AFC system.
RSS-248 Issue 2 Section 6.2 If the AFC system indicates that the frequencies are no longer available at the current power levels,
the standard-power access point or fixed client device shall immediately stop operating at those
frequencies, as determined by the AFC system.
```

### 3.4.3 Test method

The AFC DUT Test Harness validates mandatory registration information provided by the AFC DUT and responds with an

Available Spectrum Inquiry Response containing significantly different list of available frequencies and the maximum

permissible power in each.

The RF Test Equipment monitors to determine that the AFC DUT transmission does not exceed LPI limits for AFC DUT

whose manufacturer attests to its compliance with rules for LPI operation or the AFC DUT does not begin transmission in

the band prior to initial AFC authorization and that any subsequent transmissions conform to the conditions of the

Available Spectrum Inquiry Response.

### 3.4.4 Test procedure.............................................................................................................................

Table 26 describes the unsuccessful spectrum access update test procedure.

## Table 26. Unsuccessful spectrum access update

```
Step Description Results
```

```
1 If the AFC DUT is Standard Power Access Point, go to Step 2, else go to Step 12
```

```
2 AFC DUT set to Initial Pre-test State.
If needed (see Table 5 declaration), configure the AFC DUT with BSS parameters per Table 9 and a temporary test regulatory
identifier (e.g., FCC ID), geographic coordinates, antenna height, and uncertainty parameters.
Configure the DUT with AFC System URL and server root certificate.
Trigger the DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-band
methods.
```

##### - -

```
3 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields.
```

```
Pass Fail
```

```
4 AFC DUT Test Harness validates mandatory registration information Pass Fail
```

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

**Step Description Results**

5 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.

##### - -

6 Throughout the Step 2 to 5, RF Test Equipment monitors the output of the AFC DUT to confirm that the AFC DUT does not
transmit:

- In the band if the AFC DUT supports only SP operation
  Or
- Above LPI limits for AFC DUT whose manufacturer attests to its compliance with rules for LPI operation
  Wait for 60 seconds
  RF Test Equipment monitors any transmission by the AFC DUT conforms to the following:
- For SP only operation, AFC DUT conforms to the conditions contained in the Available Spectrum Inquiry Response and
  does not exceed emissions limits in adjacent frequencies.
  For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, AFC DUT transmit power in the band is less
  than CEILING [LPI limits, SP limits contained in the Available Spectrum Inquiry Response] and does not exceed emissions limits in
  adjacent frequencies

```
Pass Fail
```

7 AFC DUT is power cycled.

```
If needed (see Table 9declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID), new geographic
coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
```

##### - -

8 Wait for 60 seconds

- If the AFC DUT does not send an Available Spectrum Inquiry Request, RF Test Equipment monitors the output of the DUT
  to verify the following and STOP the test:
  ▪ For SP only operation, AFC DUT does not transmit in the band,
  ▪ For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, the AFC DUT does not
  transmit above LPI limits.
- If the AFC DUT sends an Available Spectrum Inquiry Request, then CONTINUE with Step 8

```
Pass Fail
```

9 AFC DUT Test Harness evaluates validity of mandatory registration information. Pass Fail

10 AFC DUT Test Harness sends an Available Spectrum Inquiry Response indicating that no frequency ranges and/or channels are
available.

##### - -

11 Throughout Step 7 to 10 and subsequent to Step 10 Test Equipment monitors the output of the AFC DUT to confirm that:

```
For SP only operation, AFC DUT does not transmit in the band.
For AFC DUT whose manufacturer attests to its compliance with rules for LPI operation, the AFC DUT does not transmit above LPI
limits.
```

```
Pass Fail
```

12 If the AFC DUT is Fixed Client, go to Step 13 else Stop the test

13 The AFC DUT set to Initial Pre-test State.

14 If needed (see Table 9 declaration), configure the DUT with a temporary test regulatory identifier (e.g., FCC ID), geographic
coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate.
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-
band methods.

15 AFC DUT sends a valid Available Spectrum Inquiry Request containing the inquiredFrequencyRange and/or the inquiredChannels
fields\*

```
Pass Fail
```

16 AFC DUT Test Harness validates the presence of mandatory registration information Pass Fail

17 AFC DUT Test Harness sends an Available Spectrum Inquiry Response containing a list of available frequency ranges and/or
channels and the maximum permissible transmit power in the availableFrequencyInfo and/or availableChannelInfo fields.

18 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor

19 Wait for 60 seconds Pass Fail

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

```
Step Description Results
RF Test Equipment monitors any transmission by the AFC DUT conforms to the conditions contained in the Available Spectrum
Inquiry Response and does not exceed emissions limits in adjacent frequencies
20 AFC DUT is power cycled.
If needed (see Table 9 declaration), configure the AFC DUT with a temporary test regulatory identifier (e.g., FCC ID or IC ID), new
geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT with AFC System URL and server root certificate
21 Wait for 60 seconds
If the AFC DUT does not send an Available Spectrum Inquiry Request, RF Test Equipment monitors that the AFC DUT does not
transmit above maximum transmit power limits advertised by the Standard Power Access Point for Standard Client Devices in the
channel.,
If the AFC DUT sends an Available Spectrum Inquiry Request, then CONTINUE with Step 2 2 else STOP the test
```

```
Pass Fail
```

```
22 AFC DUT Test Harness evaluates validity of mandatory registration information. Pass Fail
```

```
23 AFC DUT Test Harness sends an Available Spectrum Inquiry Response indicating that no frequency ranges and/or channels are
available.
24 If AFC DUT used Out-of-band method, initiate connection procedure between AFC DUT and SP Access Point by following
instructions provided by the AFC DUT Vendor
25 Wait for 60 seconds
RF Test Equipment monitors that the AFC DUT does not transmit above maximum transmit power limits advertised by the
Standard Power Access Point for Standard Client Devices in the channel.
```

```
Pass Fail
```

## 3.5 AFCD.USV: Unsuccessful server validation

### 3.5.1 Purpose and objective

This test case validates that the AFC DUT correctly performs server certificate validation and refrains from sending a

spectrum access request to an AFC System if that validation fails.

### 3.5.2 Compliance requirements

This test case validates that the AFC DUT meets the FCC requirements in Table 27 and ISED requirements in Table 28:

## Table 27. FCC requirements tested in AFCD.USV

```
FCC Requirement Short Description
```

```
47 CFR Section 15.407(k)(8)(v) Incorporate adequate security measurements to prevent it from accessing AFC systems not approved
by the FCC
```

## Table 28. ISED requirements tested in AFCD.RSA

```
ISED Requirement Short Description
```

```
RSS-248 Issue 2 Section 8.1 Incorporate adequate security measurements to prevent it from accessing AFC systems not approved
by the ISED
```

Note, in production it is assumed that the AFC system URL and trust root are securely configured and maintained on the

AFC DUT, and that they identify an AFC system approved by FCC or ISED.

```
© 20 24 Wi-Fi Alliance. All Rights Reserved.
Used with the permission of Wi-Fi Alliance under the terms as stated in this document.
```

### 3.5.3 Test method

The AFC DUT Test Harness and/or AFC DUT are configured with various combinations of server certificates that are

expected to fail server certificate validation. For each case, the AFC DUT is triggered to connect to the configured AFC

server, and the AFC DUT Test Harness confirms that the AFC DUT does not send a spectrum access request to it.

### 3.5.4 Test procedure.............................................................................................................................

Table 29 describes the unsuccessful server validation test procedure.

**Table 29. Unsuccessful server validation**

```
Step Description Results
```

```
1 The AFC DUT set to Initial Pre-test State.
If needed (see Table 9 declaration), configure the AFC DUT with BSS parameters per Table 14 and a temporary test regulatory
identifier (e.g., FCC ID), geographic coordinates, antenna height, and uncertainty parameters.
Configure the AFC DUT Test Harness with TLS configuration that is the same as the default configuration defined in Section 2.3.1
except for the following:
Run 1: A different server certificate (and private key) with SAN domain name entry "badafc.com" (i.e. that does not match
AFC system URL's domain name); signed by the same root certificate as per Section 2.3.1
Run 2: A different server certificate (and private key) where all attributes other than Public Key are the same as the server
certificate per Section 2.3.1, but the certificate is signed by a different root certificate
Run 3: A different server certificate (and private key) with SAN domain name entry "wfatestorg.org" only (i.e. SAN domain
name only matches suffix of AFC server's hostname); signed by the same root certificate as per Section 2.3.1
Run 4: A different server certificate (and private key) where all attributes other than Public Key are the same as the server
certificate per Section 2.3.1signed by the same root certificate as per Section 2.3.1, but the server certificate is revoked as
indicated in stapled OCSP response
Run 5: Same configuration as per Section 2.3.1, except OCSP stapling is disabled and CRL/OCSP servers are not available
Run 6: Same configuration as per Section 2.3.1, except stapled OCSP response has expired and CRL/OCSP servers are not
available
Run 7: Same configuration as per Section 2.3.1, except only the TLS cipher suite "eNULL" (no encryption) is enabled
Run 8: N/A (same configuration as per Section 2.3.1)
Configure the AFC DUT with the AFC System URL and the following root certificate:
Runs 1-7: Root certificate as per Section 2.3.1
Run 8: No root certificate
Trigger the AFC DUT to send to the AFC DUT Test Harness an Available Spectrum Inquiry Request using either In-band or Out-of-
band methods.
```

##### - -

```
2 AFC DUT Test Harness waits 10 seconds, and verifies no Available Spectrum Inquiry Request is sent to it. Pass Fail
```

```
3 Steps 1 and 2 are repeated for each of the remaining Runs Pass Fail
```
