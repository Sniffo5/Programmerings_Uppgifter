class My_list:
    def __init__(self, capacity=4):
        """Skapar en ny lista med given startkapacitet."""
        self._data = [None] * capacity   # "array" med defaultvärden
        self._size = 0                   # antal faktiska element
        self._capacity = capacity        # antal finns platser det finns
 
    def _extend(self):
        if self._size == self._capacity:
            tempArray = self._data
            self._data = [None] * (self._capacity * 2)
            for i in range(self._size):
                self._data[i] = tempArray[i]
            self._capacity *= 2
    
    def _shrink(self):
       
        if self._size < (self._capacity // 2) and self._capacity > 4:
            print (self._data)
            tempArray = self._data
            self._data = [None] * (self._capacity // 2)
            for i in range(self._size):
                self._data[i] = tempArray[i]
            self._capacity = (self._capacity // 2)
            print (self._data)

    def _check_index_range(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

    def append(self, value):
        print (self._data)
        """Lägg till ett värde sist i listan."""
        self._extend()

        self._data[self._size] = value  
        self._size += 1
         # Kolla om arrayen är full -> skapa ny, större array och kopiera
        print (self._data)

    def insert(self, index, value):

        print (self._data)

        """Lägg in ett värde på en viss position"""

        self._check_index_range(index)

        if index >= self._size:
            self.append(value)
        
        self._extend()
       
        for i in range( self._size, index, -1):     # flytta elementen åt höger, sätt in värdet på rätt plats
            self._data[i] = self._data[i-1]
        
        self._data[index] = value 
        self._size += 1
        print (self._data)
 
    def remove(self, value):
        """Ta bort första förekomsten av ett värde."""

        print (self._data)

        for i in range(self._size):
            if self._data[i] == value:
                for j in range(i, (self._size -1)):
                    self._data[j] = self._data[j+1]
                self._data[self._size-1] = None
                self._shrink()
                self._size -= 1
                print (self._data)
                return
        
        print (f"{value} is not in list")
      
        # TODO: hitta index för värdet, flytta elementen åt vänster
   
    def pop(self, index = None):
        """Ta bort och returnera elementet på en viss position (eller sist)."""
        if index:
            self._check_index_range(index)

            data = self._data[index]
            self.remove((self._data[index]))
            return (data)
            
        else:
            data = self._data[self._size - 1]
            self.remove(self._data[self._size - 1])
            return (data)

    def get(self, index):
        """Returnera värdet på en viss position."""

        self._check_index_range(index)

        print (self._data[index])
        return self._data[index]
 
    def set(self, index, value):
        """Ändra värdet på en viss position."""

        self._check_index_range(index)
        self._data[index] = value

    def size(self):
        """Returnerar antal element."""
        return (self._size)
 
    def isEmpty(self):
        """Returnerar True/False beroende på om listan är tom."""

        return True if self._size == 0 else False
        
    def __str__(self):
        """Returnerar en strängrepresentation, t.ex. [1, 2, 3]."""
        position = 0
        string = f"["
        for i in range(self._size):
            if position == 0:
                string += f"{self._data[i]}"
                position += 1
            else:
                string += f", {self._data[i]}"
                position += 1
        string += f"]"
        return string
    
    def __getitem__(self,index):
        self._check_index_range(index)
        return self.get(index)
    
    def __setitem__(self,index,value):
        self._check_index_range(index)
        self.set(index, value)
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        return self
    
    def __next__(self):

        return

l = My_list(2)

l.append(5)
l.append(3)
l.append(4)

l.get(2)

print(l)



