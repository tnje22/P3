;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::allbrickslist)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'allbrickslist (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::ALLBRICKSLIST")
  (make-package "CUSTOM_MSG_PYTHON::ALLBRICKSLIST"))

(in-package "ROS")
;;//! \htmlinclude allbrickslist.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass custom_msg_python::allbrickslist
  :super ros::object
  :slots (_red_small _red_large _blue_small _blue_large _yelow_small _yelow_large _red_small_3d _red_large_3d _blue_small_3d _blue_large_3d _yelow_small_3d _yelow_large_3d ))

(defmethod custom_msg_python::allbrickslist
  (:init
   (&key
    ((:red_small __red_small) ())
    ((:red_large __red_large) ())
    ((:blue_small __blue_small) ())
    ((:blue_large __blue_large) ())
    ((:yelow_small __yelow_small) ())
    ((:yelow_large __yelow_large) ())
    ((:red_small_3d __red_small_3d) ())
    ((:red_large_3d __red_large_3d) ())
    ((:blue_small_3d __blue_small_3d) ())
    ((:blue_large_3d __blue_large_3d) ())
    ((:yelow_small_3d __yelow_small_3d) ())
    ((:yelow_large_3d __yelow_large_3d) ())
    )
   (send-super :init)
   (setq _red_small __red_small)
   (setq _red_large __red_large)
   (setq _blue_small __blue_small)
   (setq _blue_large __blue_large)
   (setq _yelow_small __yelow_small)
   (setq _yelow_large __yelow_large)
   (setq _red_small_3d __red_small_3d)
   (setq _red_large_3d __red_large_3d)
   (setq _blue_small_3d __blue_small_3d)
   (setq _blue_large_3d __blue_large_3d)
   (setq _yelow_small_3d __yelow_small_3d)
   (setq _yelow_large_3d __yelow_large_3d)
   self)
  (:red_small
   (&rest __red_small)
   (if (keywordp (car __red_small))
       (send* _red_small __red_small)
     (progn
       (if __red_small (setq _red_small (car __red_small)))
       _red_small)))
  (:red_large
   (&rest __red_large)
   (if (keywordp (car __red_large))
       (send* _red_large __red_large)
     (progn
       (if __red_large (setq _red_large (car __red_large)))
       _red_large)))
  (:blue_small
   (&rest __blue_small)
   (if (keywordp (car __blue_small))
       (send* _blue_small __blue_small)
     (progn
       (if __blue_small (setq _blue_small (car __blue_small)))
       _blue_small)))
  (:blue_large
   (&rest __blue_large)
   (if (keywordp (car __blue_large))
       (send* _blue_large __blue_large)
     (progn
       (if __blue_large (setq _blue_large (car __blue_large)))
       _blue_large)))
  (:yelow_small
   (&rest __yelow_small)
   (if (keywordp (car __yelow_small))
       (send* _yelow_small __yelow_small)
     (progn
       (if __yelow_small (setq _yelow_small (car __yelow_small)))
       _yelow_small)))
  (:yelow_large
   (&rest __yelow_large)
   (if (keywordp (car __yelow_large))
       (send* _yelow_large __yelow_large)
     (progn
       (if __yelow_large (setq _yelow_large (car __yelow_large)))
       _yelow_large)))
  (:red_small_3d
   (&rest __red_small_3d)
   (if (keywordp (car __red_small_3d))
       (send* _red_small_3d __red_small_3d)
     (progn
       (if __red_small_3d (setq _red_small_3d (car __red_small_3d)))
       _red_small_3d)))
  (:red_large_3d
   (&rest __red_large_3d)
   (if (keywordp (car __red_large_3d))
       (send* _red_large_3d __red_large_3d)
     (progn
       (if __red_large_3d (setq _red_large_3d (car __red_large_3d)))
       _red_large_3d)))
  (:blue_small_3d
   (&rest __blue_small_3d)
   (if (keywordp (car __blue_small_3d))
       (send* _blue_small_3d __blue_small_3d)
     (progn
       (if __blue_small_3d (setq _blue_small_3d (car __blue_small_3d)))
       _blue_small_3d)))
  (:blue_large_3d
   (&rest __blue_large_3d)
   (if (keywordp (car __blue_large_3d))
       (send* _blue_large_3d __blue_large_3d)
     (progn
       (if __blue_large_3d (setq _blue_large_3d (car __blue_large_3d)))
       _blue_large_3d)))
  (:yelow_small_3d
   (&rest __yelow_small_3d)
   (if (keywordp (car __yelow_small_3d))
       (send* _yelow_small_3d __yelow_small_3d)
     (progn
       (if __yelow_small_3d (setq _yelow_small_3d (car __yelow_small_3d)))
       _yelow_small_3d)))
  (:yelow_large_3d
   (&rest __yelow_large_3d)
   (if (keywordp (car __yelow_large_3d))
       (send* _yelow_large_3d __yelow_large_3d)
     (progn
       (if __yelow_large_3d (setq _yelow_large_3d (car __yelow_large_3d)))
       _yelow_large_3d)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose2D[] _red_small
    (apply #'+ (send-all _red_small :serialization-length)) 4
    ;; geometry_msgs/Pose2D[] _red_large
    (apply #'+ (send-all _red_large :serialization-length)) 4
    ;; geometry_msgs/Pose2D[] _blue_small
    (apply #'+ (send-all _blue_small :serialization-length)) 4
    ;; geometry_msgs/Pose2D[] _blue_large
    (apply #'+ (send-all _blue_large :serialization-length)) 4
    ;; geometry_msgs/Pose2D[] _yelow_small
    (apply #'+ (send-all _yelow_small :serialization-length)) 4
    ;; geometry_msgs/Pose2D[] _yelow_large
    (apply #'+ (send-all _yelow_large :serialization-length)) 4
    ;; geometry_msgs/Point[] _red_small_3d
    (apply #'+ (send-all _red_small_3d :serialization-length)) 4
    ;; geometry_msgs/Point[] _red_large_3d
    (apply #'+ (send-all _red_large_3d :serialization-length)) 4
    ;; geometry_msgs/Point[] _blue_small_3d
    (apply #'+ (send-all _blue_small_3d :serialization-length)) 4
    ;; geometry_msgs/Point[] _blue_large_3d
    (apply #'+ (send-all _blue_large_3d :serialization-length)) 4
    ;; geometry_msgs/Point[] _yelow_small_3d
    (apply #'+ (send-all _yelow_small_3d :serialization-length)) 4
    ;; geometry_msgs/Point[] _yelow_large_3d
    (apply #'+ (send-all _yelow_large_3d :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose2D[] _red_small
     (write-long (length _red_small) s)
     (dolist (elem _red_small)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose2D[] _red_large
     (write-long (length _red_large) s)
     (dolist (elem _red_large)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose2D[] _blue_small
     (write-long (length _blue_small) s)
     (dolist (elem _blue_small)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose2D[] _blue_large
     (write-long (length _blue_large) s)
     (dolist (elem _blue_large)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose2D[] _yelow_small
     (write-long (length _yelow_small) s)
     (dolist (elem _yelow_small)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose2D[] _yelow_large
     (write-long (length _yelow_large) s)
     (dolist (elem _yelow_large)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _red_small_3d
     (write-long (length _red_small_3d) s)
     (dolist (elem _red_small_3d)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _red_large_3d
     (write-long (length _red_large_3d) s)
     (dolist (elem _red_large_3d)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _blue_small_3d
     (write-long (length _blue_small_3d) s)
     (dolist (elem _blue_small_3d)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _blue_large_3d
     (write-long (length _blue_large_3d) s)
     (dolist (elem _blue_large_3d)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _yelow_small_3d
     (write-long (length _yelow_small_3d) s)
     (dolist (elem _yelow_small_3d)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point[] _yelow_large_3d
     (write-long (length _yelow_large_3d) s)
     (dolist (elem _yelow_large_3d)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose2D[] _red_small
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _red_small (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _red_small)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose2D[] _red_large
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _red_large (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _red_large)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose2D[] _blue_small
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _blue_small (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _blue_small)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose2D[] _blue_large
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _blue_large (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _blue_large)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose2D[] _yelow_small
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yelow_small (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _yelow_small)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose2D[] _yelow_large
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yelow_large (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose2D :init) r)) r))
     (dolist (elem- _yelow_large)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _red_small_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _red_small_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _red_small_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _red_large_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _red_large_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _red_large_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _blue_small_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _blue_small_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _blue_small_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _blue_large_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _blue_large_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _blue_large_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _yelow_small_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yelow_small_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _yelow_small_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point[] _yelow_large_3d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yelow_large_3d (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _yelow_large_3d)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get custom_msg_python::allbrickslist :md5sum-) "8ba9bb7706e119d01cad46b2d7444f29")
(setf (get custom_msg_python::allbrickslist :datatype-) "custom_msg_python/allbrickslist")
(setf (get custom_msg_python::allbrickslist :definition-)
      "geometry_msgs/Pose2D[] red_small
geometry_msgs/Pose2D[] red_large
geometry_msgs/Pose2D[] blue_small
geometry_msgs/Pose2D[] blue_large
geometry_msgs/Pose2D[] yelow_small
geometry_msgs/Pose2D[] yelow_large

geometry_msgs/Point[] red_small_3d
geometry_msgs/Point[] red_large_3d
geometry_msgs/Point[] blue_small_3d
geometry_msgs/Point[] blue_large_3d
geometry_msgs/Point[] yelow_small_3d
geometry_msgs/Point[] yelow_large_3d

================================================================================
MSG: geometry_msgs/Pose2D
# Deprecated
# Please use the full 3D pose.

# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.

# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.


# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :custom_msg_python/allbrickslist "8ba9bb7706e119d01cad46b2d7444f29")


