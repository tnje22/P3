// Auto-generated. Do not edit!

// (in-package custom_msg_python.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class custom2 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.handposition = null;
      this.handvelocity = null;
      this.armposition = null;
      this.armvelocity = null;
      this.time = null;
    }
    else {
      if (initObj.hasOwnProperty('handposition')) {
        this.handposition = initObj.handposition
      }
      else {
        this.handposition = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('handvelocity')) {
        this.handvelocity = initObj.handvelocity
      }
      else {
        this.handvelocity = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('armposition')) {
        this.armposition = initObj.armposition
      }
      else {
        this.armposition = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('armvelocity')) {
        this.armvelocity = initObj.armvelocity
      }
      else {
        this.armvelocity = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type custom2
    // Serialize message field [handposition]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.handposition, buffer, bufferOffset);
    // Serialize message field [handvelocity]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.handvelocity, buffer, bufferOffset);
    // Serialize message field [armposition]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.armposition, buffer, bufferOffset);
    // Serialize message field [armvelocity]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.armvelocity, buffer, bufferOffset);
    // Serialize message field [time]
    bufferOffset = _serializer.float32(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type custom2
    let len;
    let data = new custom2(null);
    // Deserialize message field [handposition]
    data.handposition = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [handvelocity]
    data.handvelocity = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [armposition]
    data.armposition = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [armvelocity]
    data.armvelocity = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [time]
    data.time = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 100;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/custom2';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '42115633ead9253039212ba53419851b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Point handposition
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new custom2(null);
    if (msg.handposition !== undefined) {
      resolved.handposition = geometry_msgs.msg.Point.Resolve(msg.handposition)
    }
    else {
      resolved.handposition = new geometry_msgs.msg.Point()
    }

    if (msg.handvelocity !== undefined) {
      resolved.handvelocity = geometry_msgs.msg.Point.Resolve(msg.handvelocity)
    }
    else {
      resolved.handvelocity = new geometry_msgs.msg.Point()
    }

    if (msg.armposition !== undefined) {
      resolved.armposition = geometry_msgs.msg.Point.Resolve(msg.armposition)
    }
    else {
      resolved.armposition = new geometry_msgs.msg.Point()
    }

    if (msg.armvelocity !== undefined) {
      resolved.armvelocity = geometry_msgs.msg.Point.Resolve(msg.armvelocity)
    }
    else {
      resolved.armvelocity = new geometry_msgs.msg.Point()
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = 0.0
    }

    return resolved;
    }
};

module.exports = custom2;
