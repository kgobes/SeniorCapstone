
(cl:in-package :asdf)

(defsystem "lili_audio-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TTSAction" :depends-on ("_package_TTSAction"))
    (:file "_package_TTSAction" :depends-on ("_package"))
    (:file "TTSActionFeedback" :depends-on ("_package_TTSActionFeedback"))
    (:file "_package_TTSActionFeedback" :depends-on ("_package"))
    (:file "TTSActionGoal" :depends-on ("_package_TTSActionGoal"))
    (:file "_package_TTSActionGoal" :depends-on ("_package"))
    (:file "TTSActionResult" :depends-on ("_package_TTSActionResult"))
    (:file "_package_TTSActionResult" :depends-on ("_package"))
    (:file "TTSFeedback" :depends-on ("_package_TTSFeedback"))
    (:file "_package_TTSFeedback" :depends-on ("_package"))
    (:file "TTSGoal" :depends-on ("_package_TTSGoal"))
    (:file "_package_TTSGoal" :depends-on ("_package"))
    (:file "TTSResult" :depends-on ("_package_TTSResult"))
    (:file "_package_TTSResult" :depends-on ("_package"))
  ))