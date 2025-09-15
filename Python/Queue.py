class Node:
    
 def __init__(self, value):
    
    self.value = value 
    self.next = None
 
    
class Queue:
    
    def __init__(self):
        
        self.header = Node(None)
            
    def enqueue(self, Element):
        
        new_node = Node(Element)
        
        if self.header.next == None:
            
            self.header.next = new_node
        
        else:
            busqueda = True
        
            while busqueda:
            
                Node_aux = self.header
            
                if Node_aux.next != None:
                
                    Node_aux = Node_aux.next
                
                else:
                
                    busqueda =  False
                
                    Node.aux.next = new_node 


        def dequeue(self, Element):
            
            busqueda = True
            while busqueda:
                        
                if self.header.next != None:
                
                    value = self.header.next.value
                    self.header.next = self.header.next.next
                    return value
                
                else:
                    
                    print("La cola se encuentra vacia")
                        
                    
                
                    