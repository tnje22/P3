; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude activmoveslist.msg.html

(cl:defclass <activmoveslist> (roslisp-msg-protocol:ros-message)
  ((listing
    :reader listing
    :initarg :listing
    :type (cl:vector custom_msg_python-msg:actimove)
   :initform (cl:make-array 0 :element-type 'custom_msg_python-msg:actimove :initial-element (cl:make-instance 'custom_msg_python-msg:actimove))))
)

(cl:defclass activmoveslist (<activmoveslist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <activmoveslist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'activmoveslist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<activmoveslist> is deprecated: use custom_msg_python-msg:activmoveslist instead.")))

(cl:ensure-generic-function 'listing-val :lambda-list '(m))
(cl:defmethod listing-val ((m <activmoveslist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:listing-val is deprecated.  Use custom_msg_python-msg:listing instead.")
  (listing m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <activmoveslist>) ostream)
  "Serializes a message object of type '<activmoveslist>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'listing))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'listing))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <activmoveslist>) istream)
  "Deserializes a message object of type '<activmoveslist>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'listing) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'listing)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'custom_msg_python-msg:actimove))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<activmoveslist>)))
  "Returns string type for a message object of type '<activmoveslist>"
  "custom_msg_python/activmoveslist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'activmoveslist)))
  "Returns string type for a message object of type 'activmoveslist"
  "custom_msg_python/activmoveslist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<activmoveslist>)))
  "Returns md5sum for a message object of type '<activmoveslist>"
  "ad5a8f0f1484d74e62d785ee2bf5ef94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'activmoveslist)))
  "Returns md5sum for a message object of type 'activmoveslist"
  "ad5a8f0f1484d74e62d785ee2bf5ef94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<activmoveslist>)))
  "Returns full string definition for message of type '<activmoveslist>"
  (cl:format cl:nil "custom_msg_python/actimove[] listing~%~%================================================================================~%MSG: custom_msg_python/actimove~%custom_msg_python/blockdata block~%float32 humanprio~%float32 poscertainty~%float32 stabilety~%~%================================================================================~%MSG: custom_msg_python/blockdata~%int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'activmoveslist)))
  "Returns full string definition for message of type 'activmoveslist"
  (cl:format cl:nil "custom_msg_python/actimove[] listing~%~%================================================================================~%MSG: custom_msg_python/actimove~%custom_msg_python/blockdata block~%float32 humanprio~%float32 poscertainty~%float32 stabilety~%~%================================================================================~%MSG: custom_msg_python/blockdata~%int32 xlen~%int32 ylen~%int32 zlen~%~%float32 xpos~%float32 ypos~%float32 zpos~%~%int32 rotation~%~%int32 blocktype~%int32 blockcolor~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <activmoveslist>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'listing) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <activmoveslist>))
  "Converts a ROS message object to a list"
  (cl:list 'activmoveslist
    (cl:cons ':listing (listing msg))
))
