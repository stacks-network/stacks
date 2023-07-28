# Verifiable Delay Function (VDF)

Implement VDF for tenure extensions with calibration and validation functions.

## Dependencies

- none

## Requirements

- A workable VDF implementation
- An initial VDF calibration, based on benchmarks on commodity hardware
- Validation and testing of the negative feedback loop for dynamically adjusting the VDF
- It may very well be that the negative feedback loop defined above will need to be changed

## Testable interfaces

- The VDF functions (setup(), prove(), verify())
