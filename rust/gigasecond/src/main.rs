extern crate chrono;
use chrono::{TimeZone, Utc};
//use std::time::{SystemTime};
use gigasecond::after;
fn main() {
    //let start_date = Utc.now(); doesnt work
    let start_date = Utc.ymd(2019, 4, 27).and_hms(16, 1, 0);
    println!("{:?}", start_date);
    println!("{:?}", after(start_date));
    
}
