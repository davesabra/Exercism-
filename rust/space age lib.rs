
const SECONDS_IN_EARTH_YEAR: f64 = 31557600.0;

pub struct Duration {
    seconds: f64,
}

impl From<u64> for Duration {
	
    fn from(s: u64) -> Self { 
        Duration { seconds: s as f64 / SECONDS_IN_EARTH_YEAR }    //normalise to Earth time 
    }
}

pub trait Planet {
    const ORBITAL: f64; // assoc const of trait Planet
   
    fn years_during(d: &Duration) -> f64 {
        (d.seconds  / Self::ORBITAL)
    }
}

macro_rules! planet {
    ($name:ident, $orbital:expr) => {       // when I find this pattern  ( see lines 33...  )
        
        pub struct $name;                         // I insert this code
       
        impl Planet for $name { 
			const ORBITAL: f64 = $orbital; }           //   and I insert this code implementing Planet for Duration struct
    }
}     

planet!(Mercury, 0.2408467);     // this call will expand into the code block of the macro
planet!(Venus, 0.61519726);         // this call will expand into the code block of the macro
planet!(Earth, 1.0);                      // .....as above
planet!(Mars, 1.8808158);
planet!(Jupiter, 11.862615);
planet!(Saturn, 29.447498);
planet!(Uranus, 84.016846);
planet!(Neptune, 164.79132);





	
	
	
	
	
	
	
	
	 
