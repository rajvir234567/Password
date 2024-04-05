#include <Keypad.h>

#define row_num     4 // four rows
#define col_num  4 // four columns



char keys[row_num][col_num] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte row_pins[row_num] = {19, 18, 5, 17}; // GIOP19, GIOP18, GIOP5, GIOP17(TX0) connect to the row pins
byte col_pins[col_num] = {16, 4, 2, 15};   // GIOP16,(RX0) GIOP4, GIOP0, GIOP2 connect to the column pins

Keypad keypad = Keypad( makeKeymap(keys), row_pins, col_pins, row_num, col_num);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char key = keypad.getKey();

  if (key) {
    Serial.println(key);
  }
}