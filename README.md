# StockFlow Backend Case Study

## Overview
This project is part of a backend engineering case study for an Inventory Management System designed for B2B SaaS platforms.

## Features Implemented
- Product creation with validation
- Inventory management system
- Low stock alert API for companies

## API Endpoint
GET /api/companies/{company_id}/alerts/low-stock

## Approach
- Designed a scalable relational database schema
- Ensured data consistency using transactions
- Considered real-world constraints like multiple warehouses and suppliers

## Assumptions
- Recent sales activity is considered within the last 30 days
- Default low stock threshold is 10
- One primary supplier per product

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run application:
   python app.py
