# WGUPS Routing Program

## Project Overview
The **Western Governors University Parcel Service (WGUPS) Routing Program** is an optimized package delivery system designed to ensure **efficient last-mile delivery** while meeting strict constraints such as package deadlines, truck assignments, and real-time tracking. The program employs the **Nearest Neighbor Algorithm** for route optimization and dynamically updates package statuses to track deliveries.

## Technologies Used
- **Python** – Core language for program logic
- **Data Structures**: Hash Tables (`ChainingHashTable`) for fast package retrieval
- **Algorithm**: Nearest Neighbor for optimized package routing
- **File Handling**: CSV processing for package, address, and distance data
- **Error Handling & Debugging**: Ensured robust input validation and debugging utilities

## Features
✅ **Optimized Package Routing** – Uses the **Nearest Neighbor Algorithm** to find the most efficient delivery path  
✅ **Truck Assignments & Scheduling** – Handles special package constraints, delayed arrivals, and truck-specific assignments  
✅ **Real-Time Status Updates** – Tracks packages as **"At Hub," "En Route," or "Delivered"** with accurate timestamps  
✅ **CSV Data Integration** – Reads and processes package, distance, and address data for dynamic routing  
✅ **User-Friendly Interface** – CLI-based system allowing users to query package statuses at any time and view total truck mileage

## File Structure
- `Main.py` – Runs the program and provides an intuitive CLI for tracking packages and mileage
- `Package.py` – Defines the **Package** class with attributes for tracking delivery details
- `Truck.py` – Implements the **Truck** class, managing routes, mileage, and time tracking
- `Hashmap.py` – Implements a **Chaining Hash Table** for efficient package storage and retrieval
- `WGUPS_Distance_Table.csv` – Stores distance data between locations
- `WGUPS_Package_File.csv` – Contains package details such as addresses, deadlines, and special constraints
- `WGUPS_Address_File.csv` – Stores the list of known addresses used in routing

## How to Run the Program
1. **Clone the Repository**:
   ```sh
   git clone [repository-link]
   cd WGUPS-Routing-Program
   ```
2. **Run the Program**:
   ```sh
   python Main.py
   ```
3. **Follow On-Screen Prompts**:
   - Enter a time to check package statuses
   - Query by individual package or all packages
   - View truck-specific details, including mileage and package list

## Testing Scenarios
**✔ Status at Different Times:** Query package statuses at different timestamps (before and after package delays or address corrections).  
**✔ Truck-Specific Queries:** Retrieve details on truck mileage and assigned packages.  
**✔ Address Correction:** Verify that Package 9 updates to `410 S State St` at **10:20 AM**.

## Project Impact
This project demonstrates **efficient data structures**, **algorithm implementation**, and **real-world problem-solving** in logistics. Designed for scalability, it showcases expertise in **Python, data structures, and algorithmic optimization** for **dynamic routing and delivery management**.

## Author
Developed by **Manuel Marcano**
