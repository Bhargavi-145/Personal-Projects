import pytesseract
import cv2
from googletrans import Translator
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translator = Translator()

cap = cv2.VideoCapture(r'C:\Users\Bhargavi\Downloads\Realtime-OCR-Text-Detection-main\Realtime-OCR-Text-Detection-main\test-video\why (1).mp4q') 

start_time = time.time()
frame_count = 0
skip_frames = 10  # Process every 10th frame
while True:
    ret, frame = cap.read()

    if not ret:
        break  # Break the loop if there are no more frames to read

    frame_count += 1
    if frame_count % skip_frames != 0:
        continue  # Skip frames if not multiple of skip_frames

    imgH, imgW, _ = frame.shape

    # Detecting Words
    d = pytesseract.image_to_data(frame, lang='eng', output_type=pytesseract.Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 50:  # Adjust confidence threshold as needed
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            detected_text = d['text'][i]
            try:
                # Use Google Translate for translation
                detected_text = translator.translate(detected_text, src='en', dest='en').text
            except Exception as e:
                print("Translation failed for text:", detected_text)
                print("Error:", e)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
            cv2.putText(frame, detected_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 50, 255), 2)

    cv2.imshow('Text-Detection', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

end_time = time.time()
elapsed_time = end_time - start_time
print("Total processing time:", elapsed_time, "seconds")

