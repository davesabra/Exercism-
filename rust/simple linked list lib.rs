
type Link <T> = Option<Box<Node <T>>>;

#[derive(Debug)]
pub struct SimpleLinkedList<T> {
        head: Link <T>,
        len:   usize,
}

#[derive(Clone, Debug)]
struct Node <T> {
    elem: T,
    next: Link <T>,
}

impl<T> SimpleLinkedList<T> {
    pub fn new() -> Self {
        SimpleLinkedList { head: None, len: 0 } 
    }

    pub fn len(&self) -> usize {
        self.len
    }

    pub fn push(&mut self, elem: T) {
        let new_node = Box::new( Node {
			  elem: elem,
			  next: self.head.take(),
		 } ) ;
		 self.head = Some(new_node);
		 
		 self.len += 1;
    }

    pub fn pop(&mut self) -> Option<T> {
        self.head.take().map( |node| {
			
				self.head = node.next;              
                self.len -= 1;
                node.elem           
             })   
    }
    
    pub fn peek(&self) -> Option<&T> {
         self.head.as_ref().map(|node| {          
            &node.elem                  
        })
    }
    
    
    pub fn into(mut self) -> Vec<T> {     // consumes the list structure and moves the data into a vector
        let mut vec = Vec::new();
        
        while let Some(node) = self.head {
            vec.push(node.elem);
            self.head = node.next;
        }
        vec.reverse();
        vec
    }
        
}

impl<T: Clone> SimpleLinkedList<T> {
    
    pub fn rev(&mut self) -> SimpleLinkedList<T> {
        let mut list = Self::new();
       
		while let Some(node) = &self.head {
            list.push(node.elem.clone());
            self.head = node.next.clone();
        }
        list
        }
}

impl<'a, T: Clone> From<&'a [T]> for SimpleLinkedList<T> {
   
    fn from(item: &[T]) -> Self  {
            let mut list = SimpleLinkedList::new();
            
            item.iter().for_each(|i| {          // moves items, by value, from a T-generic array into the list 
                list.push(i.clone());                      
            });
            list
    }
}



