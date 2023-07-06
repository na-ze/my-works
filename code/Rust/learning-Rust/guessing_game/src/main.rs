use std::io;

fn main() {
    println!("Угадай число!");

    println!("Пожалуйста, выскажите свое предположение.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("Ты угадал: {guess}");
}
