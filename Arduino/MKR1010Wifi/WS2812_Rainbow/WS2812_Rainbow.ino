#include <Adafruit_NeoPixel.h>

// Anzahl der LEDs und der Pin, an den sie angeschlossen sind
#define NUM_LEDS 15
#define LED_PIN 6

// Erstelle ein NeoPixel-Objekt
Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  // Initialisiere die LED-Streifen

 pinMode(LED_PIN, OUTPUT);

  strip.begin();
  strip.setBrightness(100);
  strip.show(); // Alle LEDs ausschalten

   pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Beispiel: Ein einfacher Farbwechsel-Effekt
  colorWipe(strip.Color(255, 0, 0), 50); // Rot
  colorWipe(strip.Color(0, 255, 0), 50); // Grün
  colorWipe(strip.Color(0, 0, 255), 50); // Blau
  rainbow(20);                          // Regenbogen-Effekt
}

// Funktion: Füllt die LEDs nacheinander mit einer Farbe
void colorWipe(uint32_t color, int wait) {
  for (int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color); // Setzt die Farbe für LED i
    strip.show();                  // Zeige die Änderungen
    delay(wait);                   // Wartezeit zwischen den LEDs
  }
}

// Funktion: Erzeugt einen Regenbogen-Effekt
void rainbow(int wait) {
  for (long firstPixelHue = 0; firstPixelHue < 5 * 65536; firstPixelHue += 256) {
    for (int i = 0; i < strip.numPixels(); i++) {
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show();
    delay(wait);
  }
}
