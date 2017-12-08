; Auto-generated. Do not edit!


(cl:in-package lili_audio-msg)


;//! \htmlinclude TTSGoal.msg.html

(cl:defclass <TTSGoal> (roslisp-msg-protocol:ros-message)
  ((speech
    :reader speech
    :initarg :speech
    :type cl:string
    :initform "")
   (filepath
    :reader filepath
    :initarg :filepath
    :type cl:string
    :initform "")
   (voice
    :reader voice
    :initarg :voice
    :type cl:string
    :initform ""))
)

(cl:defclass TTSGoal (<TTSGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TTSGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TTSGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lili_audio-msg:<TTSGoal> is deprecated: use lili_audio-msg:TTSGoal instead.")))

(cl:ensure-generic-function 'speech-val :lambda-list '(m))
(cl:defmethod speech-val ((m <TTSGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lili_audio-msg:speech-val is deprecated.  Use lili_audio-msg:speech instead.")
  (speech m))

(cl:ensure-generic-function 'filepath-val :lambda-list '(m))
(cl:defmethod filepath-val ((m <TTSGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lili_audio-msg:filepath-val is deprecated.  Use lili_audio-msg:filepath instead.")
  (filepath m))

(cl:ensure-generic-function 'voice-val :lambda-list '(m))
(cl:defmethod voice-val ((m <TTSGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lili_audio-msg:voice-val is deprecated.  Use lili_audio-msg:voice instead.")
  (voice m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TTSGoal>) ostream)
  "Serializes a message object of type '<TTSGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'speech))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'speech))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'filepath))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'filepath))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'voice))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'voice))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TTSGoal>) istream)
  "Deserializes a message object of type '<TTSGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speech) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'speech) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'filepath) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'filepath) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'voice) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'voice) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TTSGoal>)))
  "Returns string type for a message object of type '<TTSGoal>"
  "lili_audio/TTSGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TTSGoal)))
  "Returns string type for a message object of type 'TTSGoal"
  "lili_audio/TTSGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TTSGoal>)))
  "Returns md5sum for a message object of type '<TTSGoal>"
  "69cdb2a3c22edb952c9d7579f657a5a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TTSGoal)))
  "Returns md5sum for a message object of type 'TTSGoal"
  "69cdb2a3c22edb952c9d7579f657a5a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TTSGoal>)))
  "Returns full string definition for message of type '<TTSGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string speech~%string filepath~%string voice~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TTSGoal)))
  "Returns full string definition for message of type 'TTSGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string speech~%string filepath~%string voice~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TTSGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'speech))
     4 (cl:length (cl:slot-value msg 'filepath))
     4 (cl:length (cl:slot-value msg 'voice))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TTSGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'TTSGoal
    (cl:cons ':speech (speech msg))
    (cl:cons ':filepath (filepath msg))
    (cl:cons ':voice (voice msg))
))
