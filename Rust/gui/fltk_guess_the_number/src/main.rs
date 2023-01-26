extern crate fltk;

use fltk::{app, button::*, input::*, window::*, prelude::*, text::*};
fn main() {
    let app = app::App::default();
    let mut win = Window::new(100, 100, 400, 300, "Guess the Number Game");
    let mut input = IntInput::new(120, 50, 150, 30, "Enter a number:");
    let mut message = TextDisplay::new(120, 100, 150, 30, "");
    let mut submit = Button::new(180, 130, 80, 30, "Submit");
    let mut new_game = Button::new(120, 170, 150, 30, "New Game");

    let mut secret_number = &rand::random::<u32>() % 20;

    /* 
    new_game.set_callback(move |_| {
        secret_number = rand::random::<u32>() % 100;
        input.set_value("0");
        message.set_label("");
    });
    */
    
    
     
    submit.set_callback(move |_| {
        let guess = input.value().parse::<u32>().unwrap();
        if guess == secret_number {
            message.set_label("Congratulations! You guessed the correct number.");
        } else if guess < secret_number {
            message.set_label("Too low. Try again.");
        } else {
            message.set_label("Too high. Try again.");
        }
    });
    
    
    win.end();
    win.show();
    app.run().unwrap();
}
