; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude custom1.msg.html

(cl:defclass <custom1> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0)
   (e1
    :reader e1
    :initarg :e1
    :type cl:float
    :initform 0.0)
   (e2
    :reader e2
    :initarg :e2
    :type cl:float
    :initform 0.0)
   (e3
    :reader e3
    :initarg :e3
    :type cl:float
    :initform 0.0)
   (e4
    :reader e4
    :initarg :e4
    :type cl:float
    :initform 0.0)
   (velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (acceleration
    :reader acceleration
    :initarg :acceleration
    :type cl:float
    :initform 0.0)
   (priority
    :reader priority
    :initarg :priority
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass custom1 (<custom1>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <custom1>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'custom1)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<custom1> is deprecated: use custom_msg_python-msg:custom1 instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:x-val is deprecated.  Use custom_msg_python-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:y-val is deprecated.  Use custom_msg_python-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:z-val is deprecated.  Use custom_msg_python-msg:z instead.")
  (z m))

(cl:ensure-generic-function 'e1-val :lambda-list '(m))
(cl:defmethod e1-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:e1-val is deprecated.  Use custom_msg_python-msg:e1 instead.")
  (e1 m))

(cl:ensure-generic-function 'e2-val :lambda-list '(m))
(cl:defmethod e2-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:e2-val is deprecated.  Use custom_msg_python-msg:e2 instead.")
  (e2 m))

(cl:ensure-generic-function 'e3-val :lambda-list '(m))
(cl:defmethod e3-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:e3-val is deprecated.  Use custom_msg_python-msg:e3 instead.")
  (e3 m))

(cl:ensure-generic-function 'e4-val :lambda-list '(m))
(cl:defmethod e4-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:e4-val is deprecated.  Use custom_msg_python-msg:e4 instead.")
  (e4 m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:velocity-val is deprecated.  Use custom_msg_python-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'acceleration-val :lambda-list '(m))
(cl:defmethod acceleration-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:acceleration-val is deprecated.  Use custom_msg_python-msg:acceleration instead.")
  (acceleration m))

(cl:ensure-generic-function 'priority-val :lambda-list '(m))
(cl:defmethod priority-val ((m <custom1>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:priority-val is deprecated.  Use custom_msg_python-msg:priority instead.")
  (priority m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <custom1>) ostream)
  "Serializes a message object of type '<custom1>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'e1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'e2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'e3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'e4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'priority) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <custom1>) istream)
  "Deserializes a message object of type '<custom1>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'e1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'e2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'e3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'e4) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'acceleration) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'priority) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<custom1>)))
  "Returns string type for a message object of type '<custom1>"
  "custom_msg_python/custom1")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'custom1)))
  "Returns string type for a message object of type 'custom1"
  "custom_msg_python/custom1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<custom1>)))
  "Returns md5sum for a message object of type '<custom1>"
  "31d9aef80e7e38c1513be9d4decd01d5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'custom1)))
  "Returns md5sum for a message object of type 'custom1"
  "31d9aef80e7e38c1513be9d4decd01d5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<custom1>)))
  "Returns full string definition for message of type '<custom1>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%~%float32 e1~%float32 e2~%float32 e3~%float32 e4~%~%float32 velocity~%float32 acceleration~%bool priority~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'custom1)))
  "Returns full string definition for message of type 'custom1"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%~%float32 e1~%float32 e2~%float32 e3~%float32 e4~%~%float32 velocity~%float32 acceleration~%bool priority~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <custom1>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <custom1>))
  "Converts a ROS message object to a list"
  (cl:list 'custom1
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':e1 (e1 msg))
    (cl:cons ':e2 (e2 msg))
    (cl:cons ':e3 (e3 msg))
    (cl:cons ':e4 (e4 msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':acceleration (acceleration msg))
    (cl:cons ':priority (priority msg))
))
