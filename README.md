# StockFlow Backend Case Study

## Overview
This project is part of a Backend Engineering Intern case study for an Inventory Management System.

## Features Implemented
- Product creation with validation
- Inventory management
- Low stock alert API

## API Endpoint
GET /api/companies/{company_id}/alerts/low-stock

## Approach
- Designed scalable database structure
- Used transaction handling for consistency
- Considered multiple warehouses and suppliers

## Assumptions
- Recent sales = last 30 days
- Default threshold = 10
- One supplier per product

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python app.py

## Note
This is a simplified implementation focusing on backend logic and structure.
