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

class allbrickslist {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.red_small = null;
      this.red_large = null;
      this.blue_small = null;
      this.blue_large = null;
      this.yelow_small = null;
      this.yelow_large = null;
      this.red_small_3d = null;
      this.red_large_3d = null;
      this.blue_small_3d = null;
      this.blue_large_3d = null;
      this.yelow_small_3d = null;
      this.yelow_large_3d = null;
    }
    else {
      if (initObj.hasOwnProperty('red_small')) {
        this.red_small = initObj.red_small
      }
      else {
        this.red_small = [];
      }
      if (initObj.hasOwnProperty('red_large')) {
        this.red_large = initObj.red_large
      }
      else {
        this.red_large = [];
      }
      if (initObj.hasOwnProperty('blue_small')) {
        this.blue_small = initObj.blue_small
      }
      else {
        this.blue_small = [];
      }
      if (initObj.hasOwnProperty('blue_large')) {
        this.blue_large = initObj.blue_large
      }
      else {
        this.blue_large = [];
      }
      if (initObj.hasOwnProperty('yelow_small')) {
        this.yelow_small = initObj.yelow_small
      }
      else {
        this.yelow_small = [];
      }
      if (initObj.hasOwnProperty('yelow_large')) {
        this.yelow_large = initObj.yelow_large
      }
      else {
        this.yelow_large = [];
      }
      if (initObj.hasOwnProperty('red_small_3d')) {
        this.red_small_3d = initObj.red_small_3d
      }
      else {
        this.red_small_3d = [];
      }
      if (initObj.hasOwnProperty('red_large_3d')) {
        this.red_large_3d = initObj.red_large_3d
      }
      else {
        this.red_large_3d = [];
      }
      if (initObj.hasOwnProperty('blue_small_3d')) {
        this.blue_small_3d = initObj.blue_small_3d
      }
      else {
        this.blue_small_3d = [];
      }
      if (initObj.hasOwnProperty('blue_large_3d')) {
        this.blue_large_3d = initObj.blue_large_3d
      }
      else {
        this.blue_large_3d = [];
      }
      if (initObj.hasOwnProperty('yelow_small_3d')) {
        this.yelow_small_3d = initObj.yelow_small_3d
      }
      else {
        this.yelow_small_3d = [];
      }
      if (initObj.hasOwnProperty('yelow_large_3d')) {
        this.yelow_large_3d = initObj.yelow_large_3d
      }
      else {
        this.yelow_large_3d = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type allbrickslist
    // Serialize message field [red_small]
    // Serialize the length for message field [red_small]
    bufferOffset = _serializer.uint32(obj.red_small.length, buffer, bufferOffset);
    obj.red_small.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [red_large]
    // Serialize the length for message field [red_large]
    bufferOffset = _serializer.uint32(obj.red_large.length, buffer, bufferOffset);
    obj.red_large.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [blue_small]
    // Serialize the length for message field [blue_small]
    bufferOffset = _serializer.uint32(obj.blue_small.length, buffer, bufferOffset);
    obj.blue_small.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [blue_large]
    // Serialize the length for message field [blue_large]
    bufferOffset = _serializer.uint32(obj.blue_large.length, buffer, bufferOffset);
    obj.blue_large.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [yelow_small]
    // Serialize the length for message field [yelow_small]
    bufferOffset = _serializer.uint32(obj.yelow_small.length, buffer, bufferOffset);
    obj.yelow_small.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [yelow_large]
    // Serialize the length for message field [yelow_large]
    bufferOffset = _serializer.uint32(obj.yelow_large.length, buffer, bufferOffset);
    obj.yelow_large.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose2D.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [red_small_3d]
    // Serialize the length for message field [red_small_3d]
    bufferOffset = _serializer.uint32(obj.red_small_3d.length, buffer, bufferOffset);
    obj.red_small_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [red_large_3d]
    // Serialize the length for message field [red_large_3d]
    bufferOffset = _serializer.uint32(obj.red_large_3d.length, buffer, bufferOffset);
    obj.red_large_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [blue_small_3d]
    // Serialize the length for message field [blue_small_3d]
    bufferOffset = _serializer.uint32(obj.blue_small_3d.length, buffer, bufferOffset);
    obj.blue_small_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [blue_large_3d]
    // Serialize the length for message field [blue_large_3d]
    bufferOffset = _serializer.uint32(obj.blue_large_3d.length, buffer, bufferOffset);
    obj.blue_large_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [yelow_small_3d]
    // Serialize the length for message field [yelow_small_3d]
    bufferOffset = _serializer.uint32(obj.yelow_small_3d.length, buffer, bufferOffset);
    obj.yelow_small_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [yelow_large_3d]
    // Serialize the length for message field [yelow_large_3d]
    bufferOffset = _serializer.uint32(obj.yelow_large_3d.length, buffer, bufferOffset);
    obj.yelow_large_3d.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type allbrickslist
    let len;
    let data = new allbrickslist(null);
    // Deserialize message field [red_small]
    // Deserialize array length for message field [red_small]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.red_small = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.red_small[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [red_large]
    // Deserialize array length for message field [red_large]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.red_large = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.red_large[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [blue_small]
    // Deserialize array length for message field [blue_small]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.blue_small = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.blue_small[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [blue_large]
    // Deserialize array length for message field [blue_large]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.blue_large = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.blue_large[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [yelow_small]
    // Deserialize array length for message field [yelow_small]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.yelow_small = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.yelow_small[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [yelow_large]
    // Deserialize array length for message field [yelow_large]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.yelow_large = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.yelow_large[i] = geometry_msgs.msg.Pose2D.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [red_small_3d]
    // Deserialize array length for message field [red_small_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.red_small_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.red_small_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [red_large_3d]
    // Deserialize array length for message field [red_large_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.red_large_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.red_large_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [blue_small_3d]
    // Deserialize array length for message field [blue_small_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.blue_small_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.blue_small_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [blue_large_3d]
    // Deserialize array length for message field [blue_large_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.blue_large_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.blue_large_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [yelow_small_3d]
    // Deserialize array length for message field [yelow_small_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.yelow_small_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.yelow_small_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [yelow_large_3d]
    // Deserialize array length for message field [yelow_large_3d]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.yelow_large_3d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.yelow_large_3d[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 24 * object.red_small.length;
    length += 24 * object.red_large.length;
    length += 24 * object.blue_small.length;
    length += 24 * object.blue_large.length;
    length += 24 * object.yelow_small.length;
    length += 24 * object.yelow_large.length;
    length += 24 * object.red_small_3d.length;
    length += 24 * object.red_large_3d.length;
    length += 24 * object.blue_small_3d.length;
    length += 24 * object.blue_large_3d.length;
    length += 24 * object.yelow_small_3d.length;
    length += 24 * object.yelow_large_3d.length;
    return length + 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/allbrickslist';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ba9bb7706e119d01cad46b2d7444f29';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose2D[] red_small
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new allbrickslist(null);
    if (msg.red_small !== undefined) {
      resolved.red_small = new Array(msg.red_small.length);
      for (let i = 0; i < resolved.red_small.length; ++i) {
        resolved.red_small[i] = geometry_msgs.msg.Pose2D.Resolve(msg.red_small[i]);
      }
    }
    else {
      resolved.red_small = []
    }

    if (msg.red_large !== undefined) {
      resolved.red_large = new Array(msg.red_large.length);
      for (let i = 0; i < resolved.red_large.length; ++i) {
        resolved.red_large[i] = geometry_msgs.msg.Pose2D.Resolve(msg.red_large[i]);
      }
    }
    else {
      resolved.red_large = []
    }

    if (msg.blue_small !== undefined) {
      resolved.blue_small = new Array(msg.blue_small.length);
      for (let i = 0; i < resolved.blue_small.length; ++i) {
        resolved.blue_small[i] = geometry_msgs.msg.Pose2D.Resolve(msg.blue_small[i]);
      }
    }
    else {
      resolved.blue_small = []
    }

    if (msg.blue_large !== undefined) {
      resolved.blue_large = new Array(msg.blue_large.length);
      for (let i = 0; i < resolved.blue_large.length; ++i) {
        resolved.blue_large[i] = geometry_msgs.msg.Pose2D.Resolve(msg.blue_large[i]);
      }
    }
    else {
      resolved.blue_large = []
    }

    if (msg.yelow_small !== undefined) {
      resolved.yelow_small = new Array(msg.yelow_small.length);
      for (let i = 0; i < resolved.yelow_small.length; ++i) {
        resolved.yelow_small[i] = geometry_msgs.msg.Pose2D.Resolve(msg.yelow_small[i]);
      }
    }
    else {
      resolved.yelow_small = []
    }

    if (msg.yelow_large !== undefined) {
      resolved.yelow_large = new Array(msg.yelow_large.length);
      for (let i = 0; i < resolved.yelow_large.length; ++i) {
        resolved.yelow_large[i] = geometry_msgs.msg.Pose2D.Resolve(msg.yelow_large[i]);
      }
    }
    else {
      resolved.yelow_large = []
    }

    if (msg.red_small_3d !== undefined) {
      resolved.red_small_3d = new Array(msg.red_small_3d.length);
      for (let i = 0; i < resolved.red_small_3d.length; ++i) {
        resolved.red_small_3d[i] = geometry_msgs.msg.Point.Resolve(msg.red_small_3d[i]);
      }
    }
    else {
      resolved.red_small_3d = []
    }

    if (msg.red_large_3d !== undefined) {
      resolved.red_large_3d = new Array(msg.red_large_3d.length);
      for (let i = 0; i < resolved.red_large_3d.length; ++i) {
        resolved.red_large_3d[i] = geometry_msgs.msg.Point.Resolve(msg.red_large_3d[i]);
      }
    }
    else {
      resolved.red_large_3d = []
    }

    if (msg.blue_small_3d !== undefined) {
      resolved.blue_small_3d = new Array(msg.blue_small_3d.length);
      for (let i = 0; i < resolved.blue_small_3d.length; ++i) {
        resolved.blue_small_3d[i] = geometry_msgs.msg.Point.Resolve(msg.blue_small_3d[i]);
      }
    }
    else {
      resolved.blue_small_3d = []
    }

    if (msg.blue_large_3d !== undefined) {
      resolved.blue_large_3d = new Array(msg.blue_large_3d.length);
      for (let i = 0; i < resolved.blue_large_3d.length; ++i) {
        resolved.blue_large_3d[i] = geometry_msgs.msg.Point.Resolve(msg.blue_large_3d[i]);
      }
    }
    else {
      resolved.blue_large_3d = []
    }

    if (msg.yelow_small_3d !== undefined) {
      resolved.yelow_small_3d = new Array(msg.yelow_small_3d.length);
      for (let i = 0; i < resolved.yelow_small_3d.length; ++i) {
        resolved.yelow_small_3d[i] = geometry_msgs.msg.Point.Resolve(msg.yelow_small_3d[i]);
      }
    }
    else {
      resolved.yelow_small_3d = []
    }

    if (msg.yelow_large_3d !== undefined) {
      resolved.yelow_large_3d = new Array(msg.yelow_large_3d.length);
      for (let i = 0; i < resolved.yelow_large_3d.length; ++i) {
        resolved.yelow_large_3d[i] = geometry_msgs.msg.Point.Resolve(msg.yelow_large_3d[i]);
      }
    }
    else {
      resolved.yelow_large_3d = []
    }

    return resolved;
    }
};

module.exports = allbrickslist;
