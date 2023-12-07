
(cl:in-package :asdf)

(defsystem "custom_msg_python-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "actimove" :depends-on ("_package_actimove"))
    (:file "_package_actimove" :depends-on ("_package"))
    (:file "activmoveslist" :depends-on ("_package_activmoveslist"))
    (:file "_package_activmoveslist" :depends-on ("_package"))
    (:file "allbrickslist" :depends-on ("_package_allbrickslist"))
    (:file "_package_allbrickslist" :depends-on ("_package"))
    (:file "blockdata" :depends-on ("_package_blockdata"))
    (:file "_package_blockdata" :depends-on ("_package"))
    (:file "custom" :depends-on ("_package_custom"))
    (:file "_package_custom" :depends-on ("_package"))
    (:file "custom1" :depends-on ("_package_custom1"))
    (:file "_package_custom1" :depends-on ("_package"))
    (:file "custom2" :depends-on ("_package_custom2"))
    (:file "_package_custom2" :depends-on ("_package"))
  ))