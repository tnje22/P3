; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude custom2.msg.html

(cl:defclass <custom2> (roslisp-msg-protocol:ros-message)
  ((handposition
    :reader handposition
    :initarg :handposition
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (handvelocity
    :reader handvelocity
    :initarg :handvelocity
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (armposition
    :reader armposition
    :initarg :armposition
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (armvelocity
    :reader armvelocity
    :initarg :armvelocity
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (time
    :reader time
    :initarg :time
    :type cl:float
    :initform 0.0))
)

(cl:defclass custom2 (<custom2>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <custom2>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'custom2)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<custom2> is deprecated: use custom_msg_python-msg:custom2 instead.")))

(cl:ensure-generic-function 'handposition-val :lambda-list '(m))
(cl:defmethod handposition-val ((m <custom2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:handposition-val is deprecated.  Use custom_msg_python-msg:handposition instead.")
  (handposition m))

(cl:ensure-generic-function 'handvelocity-val :lambda-list '(m))
(cl:defmethod handvelocity-val ((m <custom2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:handvelocity-val is deprecated.  Use custom_msg_python-msg:handvelocity instead.")
  (handvelocity m))

(cl:ensure-generic-function 'armposition-val :lambda-list '(m))
(cl:defmethod armposition-val ((m <custom2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:armposition-val is deprecated.  Use custom_msg_python-msg:armposition instead.")
  (armposition m))

(cl:ensure-generic-function 'armvelocity-val :lambda-list '(m))
(cl:defmethod armvelocity-val ((m <custom2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:armvelocity-val is deprecated.  Use custom_msg_python-msg:armvelocity instead.")
  (armvelocity m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <custom2>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:time-val is deprecated.  Use custom_msg_python-msg:time instead.")
  (time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <custom2>) ostream)
  "Serializes a message object of type '<custom2>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'handposition) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'handvelocity) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'armposition) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'armvelocity) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <custom2>) istream)
  "Deserializes a message object of type '<custom2>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'handposition) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'handvelocity) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'armposition) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'armvelocity) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<custom2>)))
  "Returns string type for a message object of type '<custom2>"
  "custom_msg_python/custom2")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'custom2)))
  "Returns string type for a message object of type 'custom2"
  "custom_msg_python/custom2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<custom2>)))
  "Returns md5sum for a message object of type '<custom2>"
  "42115633ead9253039212ba53419851b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'custom2)))
  "Returns md5sum for a message object of type 'custom2"
  "42115633ead9253039212ba53419851b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<custom2>)))
  "Returns full string definition for message of type '<custom2>"
  (cl:format cl:nil "geometry_msgs/Point handposition~%geometry_msgs/Point handvelocity~%geometry_msgs/Point armposition~%geometry_msgs/Point armvelocity~%float32 time~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'custom2)))
  "Returns full string definition for message of type 'custom2"
  (cl:format cl:nil "geometry_msgs/Point handposition~%geometry_msgs/Point handvelocity~%geometry_msgs/Point armposition~%geometry_msgs/Point armvelocity~%float32 time~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <custom2>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'handposition))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'handvelocity))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'armposition))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'armvelocity))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <custom2>))
  "Converts a ROS message object to a list"
  (cl:list 'custom2
    (cl:cons ':handposition (handposition msg))
    (cl:cons ':handvelocity (handvelocity msg))
    (cl:cons ':armposition (armposition msg))
    (cl:cons ':armvelocity (armvelocity msg))
    (cl:cons ':time (time msg))
))
