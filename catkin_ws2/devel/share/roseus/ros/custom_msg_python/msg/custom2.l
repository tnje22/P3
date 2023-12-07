;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::custom2)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'custom2 (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::CUSTOM2")
  (make-package "CUSTOM_MSG_PYTHON::CUSTOM2"))

(in-package "ROS")
;;//! \htmlinclude custom2.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass custom_msg_python::custom2
  :super ros::object
  :slots (_handposition _handvelocity _armposition _armvelocity _time ))

(defmethod custom_msg_python::custom2
  (:init
   (&key
    ((:handposition __handposition) (instance geometry_msgs::Point :init))
    ((:handvelocity __handvelocity) (instance geometry_msgs::Point :init))
    ((:armposition __armposition) (instance geometry_msgs::Point :init))
    ((:armvelocity __armvelocity) (instance geometry_msgs::Point :init))
    ((:time __time) 0.0)
    )
   (send-super :init)
   (setq _handposition __handposition)
   (setq _handvelocity __handvelocity)
   (setq _armposition __armposition)
   (setq _armvelocity __armvelocity)
   (setq _time (float __time))
   self)
  (:handposition
   (&rest __handposition)
   (if (keywordp (car __handposition))
       (send* _handposition __handposition)
     (progn
       (if __handposition (setq _handposition (car __handposition)))
       _handposition)))
  (:handvelocity
   (&rest __handvelocity)
   (if (keywordp (car __handvelocity))
       (send* _handvelocity __handvelocity)
     (progn
       (if __handvelocity (setq _handvelocity (car __handvelocity)))
       _handvelocity)))
  (:armposition
   (&rest __armposition)
   (if (keywordp (car __armposition))
       (send* _armposition __armposition)
     (progn
       (if __armposition (setq _armposition (car __armposition)))
       _armposition)))
  (:armvelocity
   (&rest __armvelocity)
   (if (keywordp (car __armvelocity))
       (send* _armvelocity __armvelocity)
     (progn
       (if __armvelocity (setq _armvelocity (car __armvelocity)))
       _armvelocity)))
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _handposition
    (send _handposition :serialization-length)
    ;; geometry_msgs/Point _handvelocity
    (send _handvelocity :serialization-length)
    ;; geometry_msgs/Point _armposition
    (send _armposition :serialization-length)
    ;; geometry_msgs/Point _armvelocity
    (send _armvelocity :serialization-length)
    ;; float32 _time
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _handposition
       (send _handposition :serialize s)
     ;; geometry_msgs/Point _handvelocity
       (send _handvelocity :serialize s)
     ;; geometry_msgs/Point _armposition
       (send _armposition :serialize s)
     ;; geometry_msgs/Point _armvelocity
       (send _armvelocity :serialize s)
     ;; float32 _time
       (sys::poke _time (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _handposition
     (send _handposition :deserialize buf ptr-) (incf ptr- (send _handposition :serialization-length))
   ;; geometry_msgs/Point _handvelocity
     (send _handvelocity :deserialize buf ptr-) (incf ptr- (send _handvelocity :serialization-length))
   ;; geometry_msgs/Point _armposition
     (send _armposition :deserialize buf ptr-) (incf ptr- (send _armposition :serialization-length))
   ;; geometry_msgs/Point _armvelocity
     (send _armvelocity :deserialize buf ptr-) (incf ptr- (send _armvelocity :serialization-length))
   ;; float32 _time
     (setq _time (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msg_python::custom2 :md5sum-) "42115633ead9253039212ba53419851b")
(setf (get custom_msg_python::custom2 :datatype-) "custom_msg_python/custom2")
(setf (get custom_msg_python::custom2 :definition-)
      "geometry_msgs/Point handposition
geometry_msgs/Point handvelocity
geometry_msgs/Point armposition
geometry_msgs/Point armvelocity
float32 time


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :custom_msg_python/custom2 "42115633ead9253039212ba53419851b")


