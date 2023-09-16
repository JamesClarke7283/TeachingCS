pub enum Conversion {
    MetricToImperial,
    ImperialToMetric,
}

impl Conversion {
    pub fn variants() -> [&'static str; 2] {
        ["Metric To Imperial", "Imperial To Metric"]
    }
}


pub enum UnitType {
    Length,
    Weight,
    Volume,
    Temperature,
}

impl UnitType {
    pub fn variants() -> [&'static str; 4] {
        ["Length", "Weight", "Volume", "Temperature"]
    }
}

pub enum UnitUnit {
    Imperial,
    Metric,
}

impl UnitUnit {
    pub fn variants() -> [&'static str; 2] {
        ["Imperial", "Metric"]
    }
}

pub struct Unit {
    pub name: &'static str,
    pub unit_type: UnitType,
    pub unit_unit: UnitUnit
}