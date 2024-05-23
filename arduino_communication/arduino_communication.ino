#define led 7 // Define pin 7 as the led pin
int data; // Variable to store incoming serial data

void setup() {
  pinMode(led, OUTPUT); // Set pin 7 as an output
  pinMode(LED_BUILTIN, OUTPUT);   // Set the built-in LED as an output
  Serial.begin(9600);             // Initialize serial communication at 9600 baud
  digitalWrite(led, LOW);         // Turn off the LED at pin 7
  digitalWrite(LED_BUILTIN, LOW); // Turn off the built-in LED
}

void loop() {
  // Check if data is available to read from the serial port
  while (Serial.available()) {
    data = Serial.read();  // Read the incoming data

    // If the data is '1', turn on both LEDs
    if (data == '1') {
      digitalWrite(led, HIGH);         // Turn on the LED at pin 7
      digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED
    }
    // If the data is '0', turn off both LEDs
    else if (data == '0') {
      digitalWrite(led, LOW);          // Turn off the LED at pin 7
      digitalWrite(LED_BUILTIN, LOW);  // Turn off the built-in LED
    }
  }
}
