import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Gagal membuka webcam")
        break

    results = model(frame)

    detections = results.pred[0]

    jumlah_ayam = (detections[:, -1] == 0).sum().item()

    rendered = results.render()[0]

    annotated_frame = np.array(rendered, copy=True)

    cv2.putText(
        annotated_frame,
        f'Jumlah Ayam: {int(jumlah_ayam)}',
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    cv2.imshow('Deteksi Ayam Broiler (Tekan Q untuk keluar)', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()