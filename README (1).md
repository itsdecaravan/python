# Triangle Calculator

A Python desktop calculator by Enys, built as a learning project. It uses a Tkinter window and the sine rule to calculate a missing side of a triangle, including non-right-angle triangles.

## Current features

- Calculates side **b** from side **a** and angles **A** and **B**.
- Displays the result to two decimal places.
- Includes a labelled triangle diagram and a Clear button.
- Shows helpful messages for empty or non-numeric inputs.
- Checks for finite numbers, positive side lengths and angles, and an angle sum below 180°.

## Requirements

- Python 3 with Tkinter available.
- Python's built-in `math` library.

No third-party Python packages are required. Tkinter is included with many Python installations; some Linux distributions provide it separately.

## Running the calculator

Download `calculater.py`, open it in your Python editor and run it. Alternatively, from the folder containing the file, run:

```bash
python calculater.py
```

The calculator opens in a separate window. All inputs and results are handled in that window.

## How to use it

1. Enter a known side length in **a**.
2. Enter its opposite angle in **A**, in degrees.
3. Enter the angle opposite the side you want to find in **B**, in degrees.
4. Leave **b**, **c** and **C** blank.
5. Click **Calculate** to find side **b**.
6. Click **Clear** to reset the inputs.

Lowercase letters represent side lengths. Uppercase letters represent the opposite angles. The answer uses the same length unit as side **a**.

### Example

| Input | Value |
| --- | --- |
| Side a | 5 |
| Angle A | 30° |
| Angle B | 45° |

Expected result: **b = 7.07**.

## The maths

The sine rule gives:

```text
a / sin(A) = b / sin(B)

b = a × sin(B) / sin(A)
```

The program converts the angles from degrees to radians before passing them to Python's sine function.

## Current limitations

This first version only calculates **b** from **a**, **A** and **B**. Although the interface has six input boxes, other combinations are not supported yet. The triangle drawing is a fixed guide and does not change to match the inputs.

## Possible next steps

- Calculate the remaining angle C and side c.
- Add the cosine rule for other combinations of known values.
- Update the drawing to match the calculated triangle.

## About the project

Created as a Python learning project by Enys. ChatGPT helped with the interface, explanations, debugging and input validation. The calculation was developed step by step while learning to use Python's `math` library.
