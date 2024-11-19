import cv2
import mediapipe as mp

# Inizializzazione di Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Apertura della webcam
cap = cv2.VideoCapture(0)

# Variabili per tracciare il movimento
posizione_precedente = None
direzione = None

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Impossibile accedere alla webcam.")
        break

    # Conversione dell'immagine in RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calcolo del centroide della mano
            x_totale = 0
            y_totale = 0
            for landmark in hand_landmarks.landmark:
                x_totale += landmark.x
                y_totale += landmark.y

            # Coordinate medie per trovare il centroide
            centro_x = x_totale / len(hand_landmarks.landmark)
            centro_y = y_totale / len(hand_landmarks.landmark)

            # Determina la direzione basata sul movimento
            if posizione_precedente:
                delta_x = centro_x - posizione_precedente[0]
                delta_y = centro_y - posizione_precedente[1]

                if abs(delta_x) > abs(delta_y):  # Movimento orizzontale
                    if delta_x > 0.02:  # Sensibilità
                        direzione = "sinistra"
                    elif delta_x < -0.02:
                        direzione = "destra"
                else:  # Movimento verticale
                    if delta_y > 0.02:  # Sensibilità
                        direzione = "indietro"
                    elif delta_y < -0.02:
                        direzione = "avanti"
            else:
                direzione = "Nessun movimento"

            # Aggiorna la posizione precedente
            posizione_precedente = (centro_x, centro_y)

            # Mostra la direzione sullo schermo
            cv2.putText(image, f"Direzione: {direzione}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostra il feed della webcam
    cv2.imshow("Controllo del robot con movimento della mano", image)

    # Esci premendo 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia risorse
cap.release()
cv2.destroyAllWindows()
hands.close()
