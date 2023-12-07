;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::actimove)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'actimove (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::ACTIMOVE")
  (make-package "CUSTOM_MSG_PYTHON::ACTIMOVE"))

(in-package "ROS")
;;//! \htmlinclude actimove.msg.html


(defclass custom_msg_python::actimove
  :super ros::object
  :slots (_block _humanprio _poscertainty _stabilety ))

(defmethod custom_msg_python::actimove
  (:init
   (&key
    ((:block __block) (instance custom_msg_python::blockdata :init))
    ((:humanprio __humanprio) 0.0)
    ((:poscertainty __poscertainty) 0.0)
    ((:stabilety __stabilety) 0.0)
    )
   (send-super :init)
   (setq _block __block)
   (setq _humanprio (float __humanprio))
   (setq _poscertainty (float __poscertainty))
   (setq _stabilety (float __stabilety))
   self)
  (:block
   (&rest __block)
   (if (keywordp (car __block))
       (send* _block __block)
     (progn
       (if __block (setq _block (car __block)))
       _block)))
  (:humanprio
   (&optional __humanprio)
   (if __humanprio (setq _humanprio __humanprio)) _humanprio)
  (:poscertainty
   (&optional __poscertainty)
   (if __poscertainty (setq _poscertainty __poscertainty)) _poscertainty)
  (:stabilety
   (&optional __stabilety)
   (if __stabilety (setq _stabilety __stabilety)) _stabilety)
  (:serialization-length
   ()
   (+
    ;; custom_msg_python/blockdata _block
    (send _block :serialization-length)
    ;; float32 _humanprio
    4
    ;; float32 _poscertainty
    4
    ;; float32 _stabilety
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; custom_msg_python/blockdata _block
       (send _block :serialize s)
     ;; float32 _humanprio
       (sys::poke _humanprio (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _poscertainty
       (sys::poke _poscertainty (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _stabilety
       (sys::poke _stabilety (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; custom_msg_python/blockdata _block
     (send _block :deserialize buf ptr-) (incf ptr- (send _block :serialization-length))
   ;; float32 _humanprio
     (setq _humanprio (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _poscertainty
     (setq _poscertainty (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _stabilety
     (setq _stabilety (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msg_python::actimove :md5sum-) "02dcd61482d1dd9838c30c59b919c3b8")
(setf (get custom_msg_python::actimove :datatype-) "custom_msg_python/actimove")
(setf (get custom_msg_python::actimove :definition-)
      "custom_msg_python/blockdata block
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



(provide :custom_msg_python/actimove "02dcd61482d1dd9838c30c59b919c3b8")


