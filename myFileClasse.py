class DataProcessor:
    def __init__(self, data=None):
        """
        Initialize the processor with optional data.
        """
        self.data = data if data is not None else []

    def add_item(self, item):
        """
        Add a single item to the data list.
        """
        self.data.append(item)

    def remove_item(self, item):
        """
        Remove an item from the data list.
        Raises ValueError if the item does not exist.
        """
        #TODO: FIX FUNCTION
        #original = [1, 2, 3, 2]
        if self.data !=[]:
            temp = self.data.copy()   # Kopie erstellen
            temp.remove(item)           # Änderung nur an der Kopie

            print("original:", self.data)
            print("preview:", temp)

            answer = input("proceed removing? (y): ")
            if answer.lower() == "y": 
                self.data.remove(item) 
                print("new list:", self.data)

            
            

        #return 

    def get_count(self):
        """
        Return the number of stored items.
        """
        print("TESTING")
        #TODO: FIX FUNCTION
        return

    def clear(self):
        """
        Remove all items.
        """
        self.data.clear()

    # -------- Unimplemented Methods --------

    def process(self):
        """
        Process the stored data.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'process' method.")

    def export(self, filepath):
        """
        Export the processed data to a file.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'export' method.")