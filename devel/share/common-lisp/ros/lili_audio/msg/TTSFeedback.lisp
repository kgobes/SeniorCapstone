; Auto-generated. Do not edit!


(cl:in-package lili_audio-msg)


;//! \htmlinclude TTSFeedback.msg.html

(cl:defclass <TTSFeedback> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass TTSFeedback (<TTSFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TTSFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TTSFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lili_audio-msg:<TTSFeedback> is deprecated: use lili_audio-msg:TTSFeedback instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TTSFeedback>) ostream)
  "Serializes a message object of type '<TTSFeedback>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TTSFeedback>) istream)
  "Deserializes a message object of type '<TTSFeedback>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TTSFeedback>)))
  "Returns string type for a message object of type '<TTSFeedback>"
  "lili_audio/TTSFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TTSFeedback)))
  "Returns string type for a message object of type 'TTSFeedback"
  "lili_audio/TTSFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TTSFeedback>)))
  "Returns md5sum for a message object of type '<TTSFeedback>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TTSFeedback)))
  "Returns md5sum for a message object of type 'TTSFeedback"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TTSFeedback>)))
  "Returns full string definition for message of type '<TTSFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TTSFeedback)))
  "Returns full string definition for message of type 'TTSFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TTSFeedback>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TTSFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'TTSFeedback
))
