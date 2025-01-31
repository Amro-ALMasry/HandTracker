# HandTracker

Un'applicazione Python che utilizza **OpenCV** e **MediaPipe** per tracciare il movimento delle mani e determinare la direzione del movimento basata sul loro spostamento nello spazio.

## Funzionalità
- Tracciamento della mano in tempo reale utilizzando la webcam.
- Rilevamento della posizione centrale della mano (centroide).
- Determinazione della direzione del movimento (sinistra, destra, avanti, indietro) in base al cambiamento delle coordinate del centroide.
- Visualizzazione delle connessioni tra i punti chiave della mano e del movimento rilevato.
  
## Note
- La sensibilità del rilevamento del movimento può essere modificata regolando i valori di delta_x e delta_y (attualmente impostati a 0.02).
- tasto q: Chiude l'applicazione.

## Dipendenze
Assicurati di avere installate le seguenti librerie Python:
- `opencv-python`
- `mediapipe`

Puoi installare le dipendenze con il comando:
```bash
pip install opencv-python mediapipe
