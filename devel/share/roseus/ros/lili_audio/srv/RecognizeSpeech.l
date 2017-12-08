;; Auto-generated. Do not edit!


(when (boundp 'lili_audio::RecognizeSpeech)
  (if (not (find-package "LILI_AUDIO"))
    (make-package "LILI_AUDIO"))
  (shadow 'RecognizeSpeech (find-package "LILI_AUDIO")))
(unless (find-package "LILI_AUDIO::RECOGNIZESPEECH")
  (make-package "LILI_AUDIO::RECOGNIZESPEECH"))
(unless (find-package "LILI_AUDIO::RECOGNIZESPEECHREQUEST")
  (make-package "LILI_AUDIO::RECOGNIZESPEECHREQUEST"))
(unless (find-package "LILI_AUDIO::RECOGNIZESPEECHRESPONSE")
  (make-package "LILI_AUDIO::RECOGNIZESPEECHRESPONSE"))

(in-package "ROS")





(defclass lili_audio::RecognizeSpeechRequest
  :super ros::object
  :slots ())

(defmethod lili_audio::RecognizeSpeechRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass lili_audio::RecognizeSpeechResponse
  :super ros::object
  :slots (_speech ))

(defmethod lili_audio::RecognizeSpeechResponse
  (:init
   (&key
    ((:speech __speech) "")
    )
   (send-super :init)
   (setq _speech (string __speech))
   self)
  (:speech
   (&optional __speech)
   (if __speech (setq _speech __speech)) _speech)
  (:serialization-length
   ()
   (+
    ;; string _speech
    4 (length _speech)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _speech
       (write-long (length _speech) s) (princ _speech s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _speech
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _speech (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass lili_audio::RecognizeSpeech
  :super ros::object
  :slots ())

(setf (get lili_audio::RecognizeSpeech :md5sum-) "0f212b08e2dfacb9148fa1a62023e9ac")
(setf (get lili_audio::RecognizeSpeech :datatype-) "lili_audio/RecognizeSpeech")
(setf (get lili_audio::RecognizeSpeech :request) lili_audio::RecognizeSpeechRequest)
(setf (get lili_audio::RecognizeSpeech :response) lili_audio::RecognizeSpeechResponse)

(defmethod lili_audio::RecognizeSpeechRequest
  (:response () (instance lili_audio::RecognizeSpeechResponse :init)))

(setf (get lili_audio::RecognizeSpeechRequest :md5sum-) "0f212b08e2dfacb9148fa1a62023e9ac")
(setf (get lili_audio::RecognizeSpeechRequest :datatype-) "lili_audio/RecognizeSpeechRequest")
(setf (get lili_audio::RecognizeSpeechRequest :definition-)
      "
---
string speech

")

(setf (get lili_audio::RecognizeSpeechResponse :md5sum-) "0f212b08e2dfacb9148fa1a62023e9ac")
(setf (get lili_audio::RecognizeSpeechResponse :datatype-) "lili_audio/RecognizeSpeechResponse")
(setf (get lili_audio::RecognizeSpeechResponse :definition-)
      "
---
string speech

")



(provide :lili_audio/RecognizeSpeech "0f212b08e2dfacb9148fa1a62023e9ac")


