use std::cmp::Ordering::{Equal, Greater, Less};

pub fn find<D, T>(data: D, target: T) -> Option<usize>
where
    D: AsRef<[T]>,
    D: std::fmt::Debug,
    T: Ord,
    T: std::fmt::Debug,
{
    let arr = data.as_ref();    //   converted generic type D into  type ref[T]
     
    let mut high = arr.len();
  
    let mut low = 0;
 
    let mut mid = high / 2;
 
    while low < high {
        match &target.cmp(&arr[mid]) {
            Less => high = mid - 1,
            Greater => low = mid + 1,
            Equal => return Some(mid),
        };

        mid = (high + low) / 2;
    }

    if low < arr.len() && target == arr[low] {
        Some(low)
    } else {
        None
    }
}
