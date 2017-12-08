
(cl:in-package :asdf)

(defsystem "lili_audio-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RecognizeSpeech" :depends-on ("_package_RecognizeSpeech"))
    (:file "_package_RecognizeSpeech" :depends-on ("_package"))
  ))