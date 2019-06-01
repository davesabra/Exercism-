use std::fmt;
use modulo::Mod;
use num::Integer;
const MINUTES_PER_HOUR: i32 = 60;
const MINUTES_PER_DAY: i32 = 24*60;

#[derive(PartialEq, Debug)]
pub struct Clock { minutes: i32,}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        //write!(f, "{:02}:{:02}", self.minutes/MINUTES_PER_HOUR, self.minutes % MINUTES_PER_HOUR)
        let (hours, minutes) = self.minutes.div_rem(&MINUTES_PER_HOUR);
        write!(f, "{:02}:{:02}", hours, minutes)
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {

        Clock {
            minutes: (minutes + hours*MINUTES_PER_HOUR).modulo(MINUTES_PER_DAY)
        }
    }

    pub fn add_minutes(self, minutes: i32) -> Self {
        return Clock::new(0, self.minutes + minutes);
    }
}
