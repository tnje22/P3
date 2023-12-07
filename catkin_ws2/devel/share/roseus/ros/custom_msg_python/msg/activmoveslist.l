;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::activmoveslist)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'activmoveslist (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::ACTIVMOVESLIST")
  (make-package "CUSTOM_MSG_PYTHON::ACTIVMOVESLIST"))

(in-package "ROS")
;;//! \htmlinclude activmoveslist.msg.html


(defclass custom_msg_python::activmoveslist
  :super ros::object
  :slots (_listing ))

(defmethod custom_msg_python::activmoveslist
  (:init
   (&key
    ((:listing __listing) ())
    )
   (send-super :init)
   (setq _listing __listing)
   self)
  (:listing
   (&rest __listing)
   (if (keywordp (car __listing))
       (send* _listing __listing)
     (progn
       (if __listing (setq _listing (car __listing)))
       _listing)))
  (:serialization-length
   ()
   (+
    ;; custom_msg_python/actimove[] _listing
    (apply #'+ (send-all _listing :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; custom_msg_python/actimove[] _listing
     (write-long (length _listing) s)
     (dolist (elem _listing)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; custom_msg_python/actimove[] _listing
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _listing (let (r) (dotimes (i n) (push (instance custom_msg_python::actimove :init) r)) r))
     (dolist (elem- _listing)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get custom_msg_python::activmoveslist :md5sum-) "ad5a8f0f1484d74e62d785ee2bf5ef94")
(setf (get custom_msg_python::activmoveslist :datatype-) "custom_msg_python/activmoveslist")
(setf (get custom_msg_python::activmoveslist :definition-)
      "custom_msg_python/actimove[] listing

================================================================================
MSG: custom_msg_python/actimove
custom_msg_python/blockdata block
float32 humanprio
float32 poscertainty
float32 stabilety

================================================================================
MSG: custom_msg_python/blockdata
int32 xlen
int32 ylen
int32 zlen

float32 xpos
float32 ypos
float32 zpos

int32 rotation

int32 blocktype
int32 blockcolor

")



(provide :custom_msg_python/activmoveslist "ad5a8f0f1484d74e62d785ee2bf5ef94")


