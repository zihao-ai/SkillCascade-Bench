# Technical Specification — MEMS Inertial Navigation Gyroscope
## Product: NGY-4800 Series High-Performance Angular Rate Sensor

### 1. Product Identification
- **Part Number**: NGY-4800-HG
- **Product Name**: High-Accuracy MEMS Angular Rate Sensor (Gyroscope)
- **Manufacturer**: Apex Inertial Systems LLC
- **Revision**: Rev C, 2026-03-15
- **Export Classification (to be determined)**: Pending Review

---

### 2. Functional Description
The NGY-4800-HG is a tactical-grade MEMS angular rate sensor designed for inertial navigation, platform stabilization, guided munitions, unmanned aerial vehicles (UAVs), and precision-guided systems. The device leverages a thermally-compensated resonating silicon proof mass with capacitive readout and onboard ASIC signal conditioning. The sensor provides calibrated angular rate output over a full temperature range without external compensation hardware.

---

### 3. Electrical and Mechanical Specifications

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| Input Range | — | ±450 | — | deg/s |
| Bias Instability | — | 0.28 | 0.40 | deg/hr |
| Angle Random Walk | — | 0.12 | — | deg/√hr |
| Scale Factor Nonlinearity | — | 25 | 50 | ppm |
| Bandwidth (-3 dB) | — | 100 | — | Hz |
| Operating Temperature | -55 | — | +125 | °C |
| Shock Survival | — | — | 2000 | g |
| Input Voltage | 3.0 | 3.3 | 3.6 | V |
| Current Consumption | — | 28 | 35 | mA |
| Mass | — | 4.5 | — | g |
| Package | — | LCC-28 | — | — |

---

### 4. Technology Details
- **Sensing Technology**: Tuning-fork MEMS resonator, in-plane differential capacitance
- **Compensation**: Built-in temperature-compensated calibration table (±0.003 deg/s/°C residual)
- **Interface**: SPI (4-wire), programmable 16/24-bit resolution, configurable ODR 50–2000 Hz
- **Self-Test**: Factory-traceable self-test capability per MIL-STD-883 Method 1019
- **Operating Environment**: MIL-STD-810H vibration and shock qualification
- **EMC**: MIL-STD-461G conducted and radiated emissions compliant

---

### 5. Intended Applications
Navigation-grade inertial measurement for guided munitions, UAV autopilots, platform stabilization for electro-optical/infrared (EO/IR) sensor systems, attitude heading reference systems (AHRS), and anti-jam GPS-denied navigation.

---

### 6. Regulatory Notes
This product is subject to review under the Export Administration Regulations (EAR). Preliminary specification review pending assignment of Export Control Classification Number (ECCN). Prior authorization may be required prior to export, reexport, or transfer (in-country) depending on final classification outcome.
