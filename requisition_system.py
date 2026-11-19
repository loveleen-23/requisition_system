requisition_id_counter = 10001


class requisition_system:
    def __init__(self, date="", staff_id="", staff_name="", status="Pending"):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.status = status
        self.requisitions = []
        self.total_submitted = 0
        self.total_approved = 0
        self.total_pending = 0
        self.total_not_approved = 0

    def add_requisition(self, date, staff_id, staff_name, items):
        global requisition_id_counter

        total = sum(cost for _, cost in items)
        req_id = requisition_id_counter
        requisition_id_counter += 1

        requisition = {
            "date": date,
            "requisition_id": req_id,
            "staff_id": staff_id,
            "staff_name": staff_name,
            "items": items,
            "total": total,
            "status": "Pending",
            "approval_ref": "Not available",
        }

        self.requisitions.append(requisition)
        self.total_submitted += 1
        self.total_pending += 1

        self.approve_requisition(requisition)
        return total

    def approve_requisition(self, requisition):
        if requisition["total"] < 500:
            requisition["status"] = "Approved"
            requisition["approval_ref"] = f"{requisition['staff_id']}{str(requisition['requisition_id'])[-3:]}"
            self.total_pending -= 1
            self.total_approved += 1
        else:
            requisition["status"] = "Pending"
            requisition["approval_ref"] = "Not available"

    def respond_requisition(self, req_id, decision):
        choice = decision.strip().lower()
        for req in self.requisitions:
            if req["requisition_id"] == req_id and req["status"] == "Pending":
                if choice == "approved":
                    req["status"] = "Approved"
                    req["approval_ref"] = f"{req['staff_id']}{str(req['requisition_id'])[-3:]}"
                    self.total_pending -= 1
                    self.total_approved += 1
                elif choice in ("not approved", "not_approved", "rejected"):
                    req["status"] = "Not approved"
                    req["approval_ref"] = "Not available"
                    self.total_pending -= 1
                    self.total_not_approved += 1

    def display_requisitions(self):
        for req in self.requisitions:
            print(f"Date: {req['date']}")
            print(f"Requisition ID: {req['requisition_id']}")
            print(f"Staff ID: {req['staff_id']}")
            print(f"Staff Name: {req['staff_name']}")
            print(f"Total: ${req['total']}")
            print(f"Status: {req['status']}")
            print(f"Approval Reference Number: {req['approval_ref']}")
            print()

    def requisition_statistics(self):
        stats = {
            "total_submitted": self.total_submitted,
            "total_approved": self.total_approved,
            "total_pending": self.total_pending,
            "total_not_approved": self.total_not_approved,
        }
        print("Statistics:")
        print("Displaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {stats['total_submitted']}")
        print(f"The total number of approved requisitions: {stats['total_approved']}")
        print(f"The total number of pending requisitions: {stats['total_pending']}")
        print(f"The total number of not approved requisitions: {stats['total_not_approved']}")
        print()
        

        return stats


    if __name__ == "__main__":
     system = requisition_system()

    num_reqs = int(input("How many requisitions do you want to enter? "))

    for i in range(num_reqs):
        print(f"\n--- Enter details for Requisition {i + 1} ---")
        date = input("Enter Date (DD/MM/YYYY): ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")

        items = []
        num_items = int(input("How many items for this requisition? "))
        for j in range(num_items):
            item_name = input(f"  Enter item {j + 1} name: ")
            item_price = float(input(f"  Enter item {j + 1} price: "))
            items.append((item_name, item_price))

        system.add_requisition(date, staff_id, staff_name, items)

    print("\n--- Initial Statistics ---")
    system.requisition_statistics()

    num_responses = int(input("\nHow many requisitions do you want to respond to? "))
    for _ in range(num_responses):
        req_id = int(input("Enter Requisition ID: "))
        decision = input("Enter status (Approved / Not approved): ")
        system.respond_requisition(req_id, decision)

    print("\n--- All Requisitions ---")
    system.display_requisitions()

    print("\n--- Final Statistics ---")
    system.requisition_statistics()
