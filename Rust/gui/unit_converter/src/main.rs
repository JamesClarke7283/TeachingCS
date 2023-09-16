use fltk::{app, button::Button, frame::Frame, prelude::*, window::Window, menu::Choice};

mod units;
use units::{Conversion, UnitType, Unit};

fn main() {
    // Add units
    let mut units: Vec<Unit> = Vec::new();
    units.push(Unit { name: "Inches", unit_type: UnitType::Length, unit_unit: UnitUnit::Imperial });
    units.push(Unit { name: "Centimeters", unit_type: UnitType::Length, unit_unit: UnitUnit::Metric });

    let app = app::App::default().with_scheme(app::Scheme::Gtk);
    let mut wind = Window::new(100, 100, 400, 300, "Unit Converter");

    let mut frame = Frame::new(0, 0, 400, 200, "");
    let mut but = Button::new(160, 210, 80, 40, "Submit");

    // Create a choice/dropdown
    let mut conv_direction = Choice::new(100, 50, 120, 25, "");

    // Add options to the choice/dropdown
    for &variant in Conversion::variants().iter() {
        conv_direction.add_choice(variant);
    }

    let mut conv_unit_type = Choice::new(120, 80, 120, 25, "");

    // Add options to the choice/dropdown
    for &variant in UnitType::variants().iter() {
        conv_unit_type.add_choice(variant);
    }

    let mut conv_unit = Choice::new(140, 110, 120, 25, "");
    // iterate through units
    for unit in units.iter() {
        if unit.unit_unit == conv_direction.value().starts_with()
        conv_unit.add_choice(unit.name);
    }

    // Set the default value (by index, starting from 0)
    conv_direction.set_value(0);
    conv_unit_type.set_value(0);

    but.set_callback(move |_| {
        frame.set_label("Submitted");
    });

    wind.end();
    wind.show();

    app.run().unwrap();
}
