# Units, Measurements, and Error Analysis in Physics

## 1. Physical Quantities and Units

### 1.1 Basic Concepts
- test
- **Physical Quantity**: Consists of a numerical value and a unit
- **Types of Physical Quantities**:
  - Fundamental/Base quantities
  - Derived quantities

### 1.2 SI Base Units
| Physical Quantity | SI Unit | Symbol |
|------------------|---------|---------|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric Current | ampere | A |
| Temperature | kelvin | K |
| Amount of Substance | mole | mol |
| Luminous Intensity | candela | cd |

### 1.3 SI Derived Units
| Physical Quantity | SI Unit | Symbol | Formula |
|------------------|---------|---------|----------|
| Force | newton | N | kg⋅m/s² |
| Pressure | pascal | Pa | N/m² |
| Energy | joule | J | N⋅m |
| Power | watt | W | J/s |
| Electric Potential | volt | V | W/A |
| Electric Resistance | ohm | Ω | V/A |

### 1.4 SI Prefixes
| Prefix | Symbol | Power of 10 |
|--------|---------|-------------|
| tera- | T | 10¹² |
| giga- | G | 10⁹ |
| mega- | M | 10⁶ |
| kilo- | k | 10³ |
| milli- | m | 10⁻³ |
| micro- | μ | 10⁻⁶ |
| nano- | n | 10⁻⁹ |
| pico- | p | 10⁻¹² |

## 2. Measurement and Precision

### 2.1 Types of Measurements
1. **Direct Measurements**
   - Measured directly using measuring instruments
   - Example: Length using ruler, mass using balance

2. **Indirect Measurements**
   - Calculated from direct measurements
   - Example: Density (mass/volume)

### 2.2 Characteristics of Measuring Instruments
1. **Range**: Maximum and minimum values that can be measured
2. **Least Count**: Smallest measurement that can be taken
3. **Zero Error**: Error when instrument shows non-zero reading at zero input
4. **Random Error**: Fluctuations in readings due to random causes
5. **Systematic Error**: Consistent deviation in measurements

## 3. Error Analysis

### 3.1 Types of Errors
1. **Systematic Errors**
   - Instrumental errors
   - Environmental errors
   - Personal errors
   - Can be corrected through calibration

2. **Random Errors**
   - Due to unpredictable fluctuations
   - Can be minimized by taking multiple readings

3. **Gross Errors**
   - Human mistakes
   - Can be avoided through careful observation

### 3.2 Error Calculations

#### Absolute Error
- Difference between measured value and true value
- Formula: |Measured Value - True Value|

#### Relative Error
- Ratio of absolute error to true value
- Formula: (Absolute Error/True Value) × 100%

#### Mean Absolute Error
```
Mean Absolute Error = Σ|xi - x̄|/n
where:
xi = individual measurements
x̄ = mean value
n = number of measurements
```

### 3.3 Significant Figures
- Rules for counting significant figures:
  1. All non-zero digits are significant
  2. Zeros between non-zero digits are significant
  3. Leading zeros are not significant
  4. Trailing zeros after decimal point are significant

### 3.4 Error Propagation

#### Addition and Subtraction
- Absolute errors are added
```
If Z = X + Y or Z = X - Y
ΔZ = ΔX + ΔY
```

#### Multiplication and Division
- Relative errors are added
```
If Z = X × Y or Z = X/Y
(ΔZ/Z) = (ΔX/X) + (ΔY/Y)
```

## 4. Dimensional Analysis

### 4.1 Basic Dimensions
- Length [L]
- Mass [M]
- Time [T]
- Temperature [K]
- Electric Current [A]
- Luminous Intensity [J]
- Amount of Substance [mol]

### 4.2 Applications of Dimensional Analysis
1. **Checking Equation Correctness**
   - Dimensions on both sides must be equal

2. **Deriving Relations**
   - Finding relationship between physical quantities

3. **Converting Units**
   - Using dimensional equations to convert between unit systems

### 4.3 Limitations of Dimensional Analysis
1. Cannot determine dimensionless constants
2. Cannot distinguish between scalar and vector quantities
3. Cannot determine trigonometric functions

## 5. Practical Applications

### 5.1 Laboratory Best Practices
1. Always check instrument calibration
2. Take multiple readings when possible
3. Record all units and significant figures
4. Maintain consistent environmental conditions
5. Document all procedures and observations

### 5.2 Data Presentation
1. **Tables**
   - Include units
   - Show uncertainties
   - Use appropriate significant figures

2. **Graphs**
   - Error bars when applicable
   - Clear axes labels with units
   - Appropriate scales
   - Best fit lines/curves

### 5.3 Writing Scientific Results
Format: Result = (Mean Value ± Uncertainty) Unit
Example: Length = (10.5 ± 0.1) cm
