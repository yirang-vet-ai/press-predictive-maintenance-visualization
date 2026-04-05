# press-predictive-maintenance-visualization
AI-based predictive maintenance visualization for press manufacturing using AI4I dataset

# Press Predictive Maintenance Visualization

AI-based predictive maintenance visualization project for press manufacturing systems.

Athor: Yirang Jung
All right is reserved

## Overview

This project demonstrates how machine sensor data can be used to predict equipment failures before they occur.

The goal is to move from:
- Reactive maintenance (fix after failure)
to
- Predictive maintenance (prevent before failure)

## Key Concept

Machine condition data → Pattern analysis → Failure prediction → Real-time alert

## Dataset

- AI4I 2020 Predictive Maintenance Dataset (Kaggle)
- Press AI Dataset (KAMP)

## Visualizations

This project includes 5 core visualizations:

1. Machine Failure Count  
   - Shows imbalance between normal and failure data  

2. Failure Type Distribution  
   - Identifies major failure causes  

3. Tool Wear vs Failure  
   - Demonstrates wear accumulation as failure signal  

4. Torque vs Failure  
   - Shows machine load impact  

5. Sensor Average Comparison  
   - Compares normal vs failure conditions  

## Why This Matters

- Prevent unexpected machine downtime  
- Reduce maintenance cost  
- Improve production stability  
- Enhance worker safety  

## Tech Stack

Python, Pandas, Matplotlib

## How to Run

```bash
conda activate dl_env
python ai4i_example_visualizations.py
