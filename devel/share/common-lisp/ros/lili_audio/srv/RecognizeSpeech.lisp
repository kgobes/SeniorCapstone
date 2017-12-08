; Auto-generated. Do not edit!


(cl:in-package lili_audio-srv)


;//! \htmlinclude RecognizeSpeech-request.msg.html

(cl:defclass <RecognizeSpeech-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass RecognizeSpeech-request (<RecognizeSpeech-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeSpeech-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeSpeech-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lili_audio-srv:<RecognizeSpeech-request> is deprecated: use lili_audio-srv:RecognizeSpeech-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeSpeech-request>) ostream)
  "Serializes a message object of type '<RecognizeSpeech-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeSpeech-request>) istream)
  "Deserializes a message object of type '<RecognizeSpeech-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeSpeech-request>)))
  "Returns string type for a service object of type '<RecognizeSpeech-request>"
  "lili_audio/RecognizeSpeechRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeSpeech-request)))
  "Returns string type for a service object of type 'RecognizeSpeech-request"
  "lili_audio/RecognizeSpeechRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeSpeech-request>)))
  "Returns md5sum for a message object of type '<RecognizeSpeech-request>"
  "0f212b08e2dfacb9148fa1a62023e9ac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeSpeech-request)))
  "Returns md5sum for a message object of type 'RecognizeSpeech-request"
  "0f212b08e2dfacb9148fa1a62023e9ac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeSpeech-request>)))
  "Returns full string definition for message of type '<RecognizeSpeech-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeSpeech-request)))
  "Returns full string definition for message of type 'RecognizeSpeech-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeSpeech-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeSpeech-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeSpeech-request
))
;//! \htmlinclude RecognizeSpeech-response.msg.html

(cl:defclass <RecognizeSpeech-response> (roslisp-msg-protocol:ros-message)
  ((speech
    :reader speech
    :initarg :speech
    :type cl:string
    :initform ""))
)

(cl:defclass RecognizeSpeech-response (<RecognizeSpeech-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RecognizeSpeech-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RecognizeSpeech-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lili_audio-srv:<RecognizeSpeech-response> is deprecated: use lili_audio-srv:RecognizeSpeech-response instead.")))

(cl:ensure-generic-function 'speech-val :lambda-list '(m))
(cl:defmethod speech-val ((m <RecognizeSpeech-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lili_audio-srv:speech-val is deprecated.  Use lili_audio-srv:speech instead.")
  (speech m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RecognizeSpeech-response>) ostream)
  "Serializes a message object of type '<RecognizeSpeech-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'speech))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'speech))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RecognizeSpeech-response>) istream)
  "Deserializes a message object of type '<RecognizeSpeech-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speech) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'speech) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RecognizeSpeech-response>)))
  "Returns string type for a service object of type '<RecognizeSpeech-response>"
  "lili_audio/RecognizeSpeechResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeSpeech-response)))
  "Returns string type for a service object of type 'RecognizeSpeech-response"
  "lili_audio/RecognizeSpeechResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RecognizeSpeech-response>)))
  "Returns md5sum for a message object of type '<RecognizeSpeech-response>"
  "0f212b08e2dfacb9148fa1a62023e9ac")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RecognizeSpeech-response)))
  "Returns md5sum for a message object of type 'RecognizeSpeech-response"
  "0f212b08e2dfacb9148fa1a62023e9ac")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RecognizeSpeech-response>)))
  "Returns full string definition for message of type '<RecognizeSpeech-response>"
  (cl:format cl:nil "string speech~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RecognizeSpeech-response)))
  "Returns full string definition for message of type 'RecognizeSpeech-response"
  (cl:format cl:nil "string speech~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RecognizeSpeech-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'speech))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RecognizeSpeech-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RecognizeSpeech-response
    (cl:cons ':speech (speech msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RecognizeSpeech)))
  'RecognizeSpeech-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RecognizeSpeech)))
  'RecognizeSpeech-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RecognizeSpeech)))
  "Returns string type for a service object of type '<RecognizeSpeech>"
  "lili_audio/RecognizeSpeech")