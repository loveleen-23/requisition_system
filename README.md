# Requisition System — Assessment 2

A Python-based requisition management system built using Object-Oriented Programming (`RequisitionSystem` class) to automate staff purchase requests, approval workflows, and summary reporting.

## Features
- **Submit Requisitions (`add_requisition`):** Records staff details (`staff_id`, `staff_name`, `date`), calculates the total cost of requested items, and generates a unique requisition ID starting from `10001`[cite: 1].
- **Approval Workflow (`respond_requisition`):** Updates requisition status to `Approved` or `Not approved` and updates tracking counters[cite: 9].
- **Display Requisitions (`display_requisitions`):** Prints all submitted requisitions with their ID, date, staff information, total cost, and status[cite: 9].
- **Summary Statistics (`requisition_statistics`):** Displays overall totals for submitted, approved, pending, and not approved requisitions[cite: 1, 9].

## How to Run
1. Ensure Python 3 is installed on your computer.
2. Open a terminal in the project folder and run:
   ```bash
   python requisition_system.py
