from collections import deque

class EventQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)
        print(f"Event '{event}' added.")

    def process_next_event(self):
        if self.queue:
            event = self.queue.popleft()
            print(f"Processing event: '{event}'")
        else:
            print("No events to process.")

    def display_pending_events(self):
        if self.queue:
            print("Pending Events:")
            for idx, event in enumerate(self.queue, start=1):
                print(f"{idx}. {event}")
        else:
            print("No pending events.")

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Event '{event}' canceled.")
        else:
            print(f"Event '{event}' not found or already processed.")

# Example usage
if __name__ == "__main__":
    eq = EventQueue()
    eq.add_event("UserLogin")
    eq.add_event("DataSync")
    eq.add_event("SendEmail")
    
    eq.display_pending_events()
    eq.cancel_event("DataSync")
    eq.display_pending_events()
    eq.process_next_event()
    eq.display_pending_events()

