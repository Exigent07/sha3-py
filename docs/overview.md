# SHA3 Implementation Overview

This document provides an overview of the SHA3 implementation in this package.

## Architecture

The implementation consists of two main components:

1. **Keccak Core (keccak.py)**
   - Implements the core Keccak-f[1600] permutation
   - Handles the sponge construction
   - Manages state and transformations
   - Implements padding

2. **SHA3 Interface (hash.py)**
   - Provides user-friendly interface
   - Implements standard SHA3 variants
   - Handles input processing
   - Manages output formatting

## Implementation Details

### Keccak State

The state is represented as a 5×5 array of 64-bit words. The implementation follows the "lanes" perspective of the Keccak state.

### Core Operations

1. **θ (Theta)**
   - Diffusion step
   - Computes column parities
   - Applies lane-wise XOR

2. **ρ (Rho)**
   - Rotation operation
   - Applies fixed rotation to each lane
   - Uses predefined rotation constants

3. **π (Pi)**
   - Permutation step
   - Rearranges lanes
   - Fixed permutation pattern

4. **χ (Chi)**
   - Non-linear step
   - Applies lane-wise non-linear function
   - Provides confusion property

5. **ι (Iota)**
   - Adds round constant
   - Breaks symmetry
   - Uses LFSR-based constants

### Sponge Construction

The implementation uses the sponge construction with:
- Rate (r) = 1600 - 2×output_length
- Capacity (c) = 2×output_length

### Security Considerations

The implementation maintains security through:
- Proper capacity/rate split
- Complete round execution
- Secure padding rule
- No truncation of security-critical operations

## Testing

The test suite includes:
- NIST test vectors
- Empty string cases
- Long input cases
- Binary input cases
- Edge cases and error conditions