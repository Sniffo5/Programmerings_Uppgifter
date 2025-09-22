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
       
        if self._size < (self._capacity // 2) and self._capacity > 5:
            print (self._data)
            tempArray = self._data
            self._data = [None] * (self._capacity // 2)
            for i in range(self._size):
                self._data[i] = tempArray[i]
            self._capacity = int(self._capacity / 2)
            print (self._data)

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

        if index < 0:
            print (f"Error: index out of bounds")
            return

        if index >= self._capacity:
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
        
        print (f"Du är en idiot, '{value}' är inte med i listan.")
      
        # TODO: hitta index för värdet, flytta elementen åt vänster
   

    def pop(self, index):
        """Ta bort och returnera elementet på en viss position (eller sist)."""
        
        for i in range(self._size):
            if i == index:
                self.remove((self._data[i]))
                print (self._data[i])
 
    def get(self, index):
        """Returnera värdet på en viss position."""

        if self._capacity < index:
            return

        print (self._data[index])

 
    def set(self, index, value):
        """Ändra värdet på en viss position."""

        if self.size < index:
            return

        self._data[index] = value

 
    def size(self):
        """Returnerar antal element."""
        size = 0
        
        for i in range(self._size):
            size += 1
        
        print (f"{size} elements in the list")
 
    def isEmpty(self):
        """Returnerar True/False beroende på om listan är tom."""
        pass
 
    def __str__(self):
        """Returnerar en strängrepresentation, t.ex. [1, 2, 3]."""

        string = f"["
        for i in range(self._size-1):
            string += f"{self._data[i]}, "
        string += f"]"
        return string
    pass


lista = My_list(5)
lista.append("1")
lista.append("2")
lista.append("3")
lista.append("4")
lista.append("5")

lista.remove("2")





