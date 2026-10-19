# Technical Specification — GaN MMIC Power Amplifier Module
## Product: PXA-9200 High-Power Microwave Amplifier

### 1. Product Identification
- **Part Number**: PXA-9200-PA
- **Product Name**: GaN-on-SiC MMIC Power Amplifier, X-Band
- **Manufacturer**: Meridian RF Systems Inc.
- **Revision**: Rev B, 2026-02-20
- **Export Classification (to be determined)**: Pending Review

---

### 2. Functional Description
The PXA-9200-PA is a Gallium Nitride on Silicon Carbide (GaN-on-SiC) monolithic microwave integrated circuit (MMIC) power amplifier designed for X-band radar front-end, electronic warfare, satellite uplink, and high-power pulsed waveform generation. The device provides wideband coverage from 8 GHz to 12 GHz with a saturated output power of 50 W (47 dBm) and a power-added efficiency (PAE) exceeding 40% across the operating band. An on-chip drain bias sequencing network and integrated thermal management substrate ensure stable operation under continuous wave (CW) and pulsed conditions.

---

### 3. Electrical and RF Performance Specifications

| Parameter | Min | Typ | Max | Unit |
|---|---|---|---|---|
| Frequency Range | 8.0 | — | 12.0 | GHz |
| Saturated Output Power (Psat) | 46 | 47 | — | dBm |
| Small-Signal Gain (S21) | 28 | 32 | — | dB |
| Power-Added Efficiency (PAE) | 38 | 42 | — | % |
| Noise Figure | — | 3.5 | 4.2 | dB |
| Input VSWR | — | 1.8:1 | 2.2:1 | — |
| Output VSWR | — | 1.9:1 | 2.4:1 | — |
| 3rd-Order Intercept (OIP3) | 58 | 60 | — | dBm |
| Supply Voltage (Vdd) | 27 | 28 | 30 | V |
| Quiescent Drain Current (Idq) | — | 1.8 | 2.1 | A |
| Gate Bias (Vgg) | -3.2 | -2.8 | -2.4 | V |

---

### 4. Technology and Construction
- **Process**: GaN-on-SiC HEMT (High Electron Mobility Transistor), 0.25 µm gate length
- **Die Size**: 6.2 mm × 4.1 mm
- **Substrate**: SiC (Silicon Carbide), 100 µm thickness
- **Matching Networks**: Integrated thin-film resistors, MIM capacitors, spiral inductors
- **Gate Count**: 12 unit cells, each with 8×125 µm gate periphery (12 mm total gate width)
- **Packaging Options**: Bare die, QFN-48 (hermetic), drop-in module (SMA connectors)
- **Operating Temperature**: -55°C to +150°C (junction), -40°C to +85°C (case)

---

### 5. Pulsed Operation Parameters
- **Maximum Pulse Width**: 100 µs
- **Minimum Pulse Repetition Interval**: 500 µs (20% duty cycle maximum)
- **Pulsed Psat**: 50 W minimum at 10% duty cycle
- **Rise/Fall Time**: < 150 ns

---

### 6. Intended Applications
Primary design targets include airborne and shipborne active electronically scanned array (AESA) radar transmit/receive (T/R) modules, electronic countermeasures (ECM) jamming sub-systems, synthetic aperture radar (SAR) payloads, and high-power satellite command uplinks. The device is rated for operation in MIL-STD-810H environmental conditions.

---

### 7. Compliance and Standards
- MIL-PRF-38534 Class H (hermetic screening for military electronics)
- MIL-STD-883 Method 2019 (physical dimensions)
- MIL-STD-461G (electromagnetic compatibility)
- JEDEC JESD22 reliability qualification (temperature cycling, shock, vibration)
- RoHS exempt (military application, Annex III waiver)
