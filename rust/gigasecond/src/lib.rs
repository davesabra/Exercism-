extern crate chrono;
use chrono::{DateTime, Duration, Utc};

pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
    println!("What time is a gigasecond later than {} ?", start);

    start + Duration::seconds(1_000_000_000)
}
