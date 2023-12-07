; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude blockdata.msg.html

(cl:defclass <blockdata> (roslisp-msg-protocol:ros-message)
  ((xlen
    :reader xlen
    :initarg :xlen
    :type cl:integer
    :initform 0)
   (ylen
    :reader ylen
    :initarg :ylen
    :type cl:integer
    :initform 0)
   (zlen
    :reader zlen
    :initarg :zlen
    :type cl:integer
    :initform 0)
   (xpos
    :reader xpos
    :initarg :xpos
    :type cl:float
    :initform 0.0)
   (ypos
    :reader ypos
    :initarg :ypos
    :type cl:float
    :initform 0.0)
   (zpos
    :reader zpos
    :initarg :zpos
    :type cl:float
    :initform 0.0)
   (rotation
    :reader rotation
    :initarg :rotation
    :type cl:integer
    :initform 0)
   (blocktype
    :reader blocktype
    :initarg :blocktype
    :type cl:integer
    :initform 0)
   (blockcolor
    :reader blockcolor
    :initarg :blockcolor
    :type cl:integer
    :initform 0))
)

(cl:defclass blockdata (<blockdata>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <blockdata>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'blockdata)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<blockdata> is deprecated: use custom_msg_python-msg:blockdata instead.")))

(cl:ensure-generic-function 'xlen-val :lambda-list '(m))
(cl:defmethod xlen-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:xlen-val is deprecated.  Use custom_msg_python-msg:xlen instead.")
  (xlen m))

(cl:ensure-generic-function 'ylen-val :lambda-list '(m))
(cl:defmethod ylen-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:ylen-val is deprecated.  Use custom_msg_python-msg:ylen instead.")
  (ylen m))

(cl:ensure-generic-function 'zlen-val :lambda-list '(m))
(cl:defmethod zlen-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:zlen-val is deprecated.  Use custom_msg_python-msg:zlen instead.")
  (zlen m))

(cl:ensure-generic-function 'xpos-val :lambda-list '(m))
(cl:defmethod xpos-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:xpos-val is deprecated.  Use custom_msg_python-msg:xpos instead.")
  (xpos m))

(cl:ensure-generic-function 'ypos-val :lambda-list '(m))
(cl:defmethod ypos-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:ypos-val is deprecated.  Use custom_msg_python-msg:ypos instead.")
  (ypos m))

(cl:ensure-generic-function 'zpos-val :lambda-list '(m))
(cl:defmethod zpos-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:zpos-val is deprecated.  Use custom_msg_python-msg:zpos instead.")
  (zpos m))

(cl:ensure-generic-function 'rotation-val :lambda-list '(m))
(cl:defmethod rotation-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:rotation-val is deprecated.  Use custom_msg_python-msg:rotation instead.")
  (rotation m))

(cl:ensure-generic-function 'blocktype-val :lambda-list '(m))
(cl:defmethod blocktype-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:blocktype-val is deprecated.  Use custom_msg_python-msg:blocktype instead.")
  (blocktype m))

(cl:ensure-generic-function 'blockcolor-val :lambda-list '(m))
(cl:defmethod blockcolor-val ((m <blockdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:blockcolor-val is deprecated.  Use custom_msg_python-msg:blockcolor instead.")
  (blockcolor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <blockdata>) ostream)
  "Serializes a message object of type '<blockdata>"
  (cl:let* ((signed (cl:slot-value msg 'xlen)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ylen)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'zlen)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'xpos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ypos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'zpos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'rotation)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'blocktype)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'blockcolor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <blockdata>) istream)
  "Deserializes a message object of type '<blockdata>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'xlen) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ylen) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zlen) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'xpos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ypos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'zpos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rotation) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'blocktype) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'blockcolor) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<blockdata>)))
  "Returns string type for a message object of type '<blockdata>"
  "custom_msg_python/blockdata")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'blockdata)))
  "Returns string type for a message object of type 'blockdata"
  "custom_msg_python/blockdata")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<blockdata>)))
  "Returns md5sum for a message object of type '<blockdata>"
  "eac9cc71fe8df90f9f784800602aae10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'blockdata)))
  "Returns md5sum for a message object of type 'blockdata"
  "eac9cc71fe8df90f9f784800602aae10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<blockdata>)))
  "Returns full string definition for message of type '<blockdata>"
  (cl:format cl:nil "int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'blockdata)))
  "Returns full string definition for message of type 'blockdata"
  (cl:format cl:nil "int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <blockdata>))
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
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <blockdata>))
  "Converts a ROS message object to a list"
  (cl:list 'blockdata
    (cl:cons ':xlen (xlen msg))
    (cl:cons ':ylen (ylen msg))
    (cl:cons ':zlen (zlen msg))
    (cl:cons ':xpos (xpos msg))
    (cl:cons ':ypos (ypos msg))
    (cl:cons ':zpos (zpos msg))
    (cl:cons ':rotation (rotation msg))
    (cl:cons ':blocktype (blocktype msg))
    (cl:cons ':blockcolor (blockcolor msg))
))
