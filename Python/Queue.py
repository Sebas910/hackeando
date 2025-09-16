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

            Node_aux = self.header
            
            while busqueda:
            
            
                if Node_aux.next != None:
                
                    Node_aux = Node_aux.next
                
                else:
                
                    busqueda =  False
                
                    Node_aux.next = new_node 


    def dequeue(self):
            
            
            while True:
                        
                if self.header.next != None:
                
                    value = self.header.next.value
                    self.header.next = self.header.next.next
                    return value
                
                else:
                    
                    return None
