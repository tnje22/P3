;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::custom)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'custom (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::CUSTOM")
  (make-package "CUSTOM_MSG_PYTHON::CUSTOM"))

(in-package "ROS")
;;//! \htmlinclude custom.msg.html


(defclass custom_msg_python::custom
  :super ros::object
  :slots (_configurationmode ))

(defmethod custom_msg_python::custom
  (:init
   (&key
    ((:configurationmode __configurationmode) nil)
    )
   (send-super :init)
   (setq _configurationmode __configurationmode)
   self)
  (:configurationmode
   (&optional (__configurationmode :null))
   (if (not (eq __configurationmode :null)) (setq _configurationmode __configurationmode)) _configurationmode)
  (:serialization-length
   ()
   (+
    ;; bool _configurationmode
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _configurationmode
       (if _configurationmode (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _configurationmode
     (setq _configurationmode (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get custom_msg_python::custom :md5sum-) "63b9c1c4bde05e435d92eaf6475fe3c0")
(setf (get custom_msg_python::custom :datatype-) "custom_msg_python/custom")
(setf (get custom_msg_python::custom :definition-)
      "
bool configurationmode

")



(provide :custom_msg_python/custom "63b9c1c4bde05e435d92eaf6475fe3c0")


