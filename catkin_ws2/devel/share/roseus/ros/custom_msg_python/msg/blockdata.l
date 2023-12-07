;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::blockdata)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'blockdata (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::BLOCKDATA")
  (make-package "CUSTOM_MSG_PYTHON::BLOCKDATA"))

(in-package "ROS")
;;//! \htmlinclude blockdata.msg.html


(defclass custom_msg_python::blockdata
  :super ros::object
  :slots (_xlen _ylen _zlen _xpos _ypos _zpos _rotation _blocktype _blockcolor ))

(defmethod custom_msg_python::blockdata
  (:init
   (&key
    ((:xlen __xlen) 0)
    ((:ylen __ylen) 0)
    ((:zlen __zlen) 0)
    ((:xpos __xpos) 0.0)
    ((:ypos __ypos) 0.0)
    ((:zpos __zpos) 0.0)
    ((:rotation __rotation) 0)
    ((:blocktype __blocktype) 0)
    ((:blockcolor __blockcolor) 0)
    )
   (send-super :init)
   (setq _xlen (round __xlen))
   (setq _ylen (round __ylen))
   (setq _zlen (round __zlen))
   (setq _xpos (float __xpos))
   (setq _ypos (float __ypos))
   (setq _zpos (float __zpos))
   (setq _rotation (round __rotation))
   (setq _blocktype (round __blocktype))
   (setq _blockcolor (round __blockcolor))
   self)
  (:xlen
   (&optional __xlen)
   (if __xlen (setq _xlen __xlen)) _xlen)
  (:ylen
   (&optional __ylen)
   (if __ylen (setq _ylen __ylen)) _ylen)
  (:zlen
   (&optional __zlen)
   (if __zlen (setq _zlen __zlen)) _zlen)
  (:xpos
   (&optional __xpos)
   (if __xpos (setq _xpos __xpos)) _xpos)
  (:ypos
   (&optional __ypos)
   (if __ypos (setq _ypos __ypos)) _ypos)
  (:zpos
   (&optional __zpos)
   (if __zpos (setq _zpos __zpos)) _zpos)
  (:rotation
   (&optional __rotation)
   (if __rotation (setq _rotation __rotation)) _rotation)
  (:blocktype
   (&optional __blocktype)
   (if __blocktype (setq _blocktype __blocktype)) _blocktype)
  (:blockcolor
   (&optional __blockcolor)
   (if __blockcolor (setq _blockcolor __blockcolor)) _blockcolor)
  (:serialization-length
   ()
   (+
    ;; int32 _xlen
    4
    ;; int32 _ylen
    4
    ;; int32 _zlen
    4
    ;; float32 _xpos
    4
    ;; float32 _ypos
    4
    ;; float32 _zpos
    4
    ;; int32 _rotation
    4
    ;; int32 _blocktype
    4
    ;; int32 _blockcolor
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _xlen
       (write-long _xlen s)
     ;; int32 _ylen
       (write-long _ylen s)
     ;; int32 _zlen
       (write-long _zlen s)
     ;; float32 _xpos
       (sys::poke _xpos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _ypos
       (sys::poke _ypos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _zpos
       (sys::poke _zpos (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _rotation
       (write-long _rotation s)
     ;; int32 _blocktype
       (write-long _blocktype s)
     ;; int32 _blockcolor
       (write-long _blockcolor s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _xlen
     (setq _xlen (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _ylen
     (setq _ylen (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _zlen
     (setq _zlen (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _xpos
     (setq _xpos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _ypos
     (setq _ypos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _zpos
     (setq _zpos (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _rotation
     (setq _rotation (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _blocktype
     (setq _blocktype (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _blockcolor
     (setq _blockcolor (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msg_python::blockdata :md5sum-) "eac9cc71fe8df90f9f784800602aae10")
(setf (get custom_msg_python::blockdata :datatype-) "custom_msg_python/blockdata")
(setf (get custom_msg_python::blockdata :definition-)
      "int32 xlen
int32 ylen
int32 zlen

float32 xpos
float32 ypos
float32 zpos

int32 rotation

int32 blocktype
int32 blockcolor

")



(provide :custom_msg_python/blockdata "eac9cc71fe8df90f9f784800602aae10")


