;; Auto-generated. Do not edit!


(when (boundp 'lili_audio::TTSFeedback)
  (if (not (find-package "LILI_AUDIO"))
    (make-package "LILI_AUDIO"))
  (shadow 'TTSFeedback (find-package "LILI_AUDIO")))
(unless (find-package "LILI_AUDIO::TTSFEEDBACK")
  (make-package "LILI_AUDIO::TTSFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude TTSFeedback.msg.html


(defclass lili_audio::TTSFeedback
  :super ros::object
  :slots ())

(defmethod lili_audio::TTSFeedback
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

(setf (get lili_audio::TTSFeedback :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get lili_audio::TTSFeedback :datatype-) "lili_audio/TTSFeedback")
(setf (get lili_audio::TTSFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======


")



(provide :lili_audio/TTSFeedback "d41d8cd98f00b204e9800998ecf8427e")

