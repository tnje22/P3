;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::custom1)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'custom1 (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::CUSTOM1")
  (make-package "CUSTOM_MSG_PYTHON::CUSTOM1"))

(in-package "ROS")
;;//! \htmlinclude custom1.msg.html


(defclass custom_msg_python::custom1
  :super ros::object
  :slots (_x _y _z _e1 _e2 _e3 _e4 _velocity _acceleration _priority ))

(defmethod custom_msg_python::custom1
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:e1 __e1) 0.0)
    ((:e2 __e2) 0.0)
    ((:e3 __e3) 0.0)
    ((:e4 __e4) 0.0)
    ((:velocity __velocity) 0.0)
    ((:acceleration __acceleration) 0.0)
    ((:priority __priority) nil)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _e1 (float __e1))
   (setq _e2 (float __e2))
   (setq _e3 (float __e3))
   (setq _e4 (float __e4))
   (setq _velocity (float __velocity))
   (setq _acceleration (float __acceleration))
   (setq _priority __priority)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:e1
   (&optional __e1)
   (if __e1 (setq _e1 __e1)) _e1)
  (:e2
   (&optional __e2)
   (if __e2 (setq _e2 __e2)) _e2)
  (:e3
   (&optional __e3)
   (if __e3 (setq _e3 __e3)) _e3)
  (:e4
   (&optional __e4)
   (if __e4 (setq _e4 __e4)) _e4)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:acceleration
   (&optional __acceleration)
   (if __acceleration (setq _acceleration __acceleration)) _acceleration)
  (:priority
   (&optional (__priority :null))
   (if (not (eq __priority :null)) (setq _priority __priority)) _priority)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _e1
    4
    ;; float32 _e2
    4
    ;; float32 _e3
    4
    ;; float32 _e4
    4
    ;; float32 _velocity
    4
    ;; float32 _acceleration
    4
    ;; bool _priority
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _e1
       (sys::poke _e1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _e2
       (sys::poke _e2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _e3
       (sys::poke _e3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _e4
       (sys::poke _e4 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acceleration
       (sys::poke _acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _priority
       (if _priority (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _e1
     (setq _e1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _e2
     (setq _e2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _e3
     (setq _e3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _e4
     (setq _e4 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _velocity
     (setq _velocity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acceleration
     (setq _acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _priority
     (setq _priority (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get custom_msg_python::custom1 :md5sum-) "31d9aef80e7e38c1513be9d4decd01d5")
(setf (get custom_msg_python::custom1 :datatype-) "custom_msg_python/custom1")
(setf (get custom_msg_python::custom1 :definition-)
      "float32 x
float32 y
float32 z

float32 e1
float32 e2
float32 e3
float32 e4

float32 velocity
float32 acceleration
bool priority

")



(provide :custom_msg_python/custom1 "31d9aef80e7e38c1513be9d4decd01d5")


