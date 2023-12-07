; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude actimove.msg.html

(cl:defclass <actimove> (roslisp-msg-protocol:ros-message)
  ((block
    :reader block
    :initarg :block
    :type custom_msg_python-msg:blockdata
    :initform (cl:make-instance 'custom_msg_python-msg:blockdata))
   (humanprio
    :reader humanprio
    :initarg :humanprio
    :type cl:float
    :initform 0.0)
   (poscertainty
    :reader poscertainty
    :initarg :poscertainty
    :type cl:float
    :initform 0.0)
   (stabilety
    :reader stabilety
    :initarg :stabilety
    :type cl:float
    :initform 0.0))
)

(cl:defclass actimove (<actimove>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <actimove>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'actimove)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<actimove> is deprecated: use custom_msg_python-msg:actimove instead.")))

(cl:ensure-generic-function 'block-val :lambda-list '(m))
(cl:defmethod block-val ((m <actimove>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:block-val is deprecated.  Use custom_msg_python-msg:block instead.")
  (block m))

(cl:ensure-generic-function 'humanprio-val :lambda-list '(m))
(cl:defmethod humanprio-val ((m <actimove>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:humanprio-val is deprecated.  Use custom_msg_python-msg:humanprio instead.")
  (humanprio m))

(cl:ensure-generic-function 'poscertainty-val :lambda-list '(m))
(cl:defmethod poscertainty-val ((m <actimove>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:poscertainty-val is deprecated.  Use custom_msg_python-msg:poscertainty instead.")
  (poscertainty m))

(cl:ensure-generic-function 'stabilety-val :lambda-list '(m))
(cl:defmethod stabilety-val ((m <actimove>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:stabilety-val is deprecated.  Use custom_msg_python-msg:stabilety instead.")
  (stabilety m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <actimove>) ostream)
  "Serializes a message object of type '<actimove>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'block) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'humanprio))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'poscertainty))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'stabilety))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <actimove>) istream)
  "Deserializes a message object of type '<actimove>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'block) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'humanprio) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'poscertainty) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'stabilety) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<actimove>)))
  "Returns string type for a message object of type '<actimove>"
  "custom_msg_python/actimove")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'actimove)))
  "Returns string type for a message object of type 'actimove"
  "custom_msg_python/actimove")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<actimove>)))
  "Returns md5sum for a message object of type '<actimove>"
  "02dcd61482d1dd9838c30c59b919c3b8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'actimove)))
  "Returns md5sum for a message object of type 'actimove"
  "02dcd61482d1dd9838c30c59b919c3b8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<actimove>)))
  "Returns full string definition for message of type '<actimove>"
  (cl:format cl:nil "custom_msg_python/blockdata block~%float32 humanprio~%float32 poscertainty~%float32 stabilety~%~%================================================================================~%MSG: custom_msg_python/blockdata~%int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'actimove)))
  "Returns full string definition for message of type 'actimove"
  (cl:format cl:nil "custom_msg_python/blockdata block~%float32 humanprio~%float32 poscertainty~%float32 stabilety~%~%================================================================================~%MSG: custom_msg_python/blockdata~%int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <actimove>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'block))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <actimove>))
  "Converts a ROS message object to a list"
  (cl:list 'actimove
    (cl:cons ':block (block msg))
    (cl:cons ':humanprio (humanprio msg))
    (cl:cons ':poscertainty (poscertainty msg))
    (cl:cons ':stabilety (stabilety msg))
))
