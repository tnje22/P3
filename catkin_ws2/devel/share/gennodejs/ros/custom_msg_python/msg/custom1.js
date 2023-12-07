// Auto-generated. Do not edit!

// (in-package custom_msg_python.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class custom1 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.z = null;
      this.e1 = null;
      this.e2 = null;
      this.e3 = null;
      this.e4 = null;
      this.velocity = null;
      this.acceleration = null;
      this.priority = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('z')) {
        this.z = initObj.z
      }
      else {
        this.z = 0.0;
      }
      if (initObj.hasOwnProperty('e1')) {
        this.e1 = initObj.e1
      }
      else {
        this.e1 = 0.0;
      }
      if (initObj.hasOwnProperty('e2')) {
        this.e2 = initObj.e2
      }
      else {
        this.e2 = 0.0;
      }
      if (initObj.hasOwnProperty('e3')) {
        this.e3 = initObj.e3
      }
      else {
        this.e3 = 0.0;
      }
      if (initObj.hasOwnProperty('e4')) {
        this.e4 = initObj.e4
      }
      else {
        this.e4 = 0.0;
      }
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = 0.0;
      }
      if (initObj.hasOwnProperty('acceleration')) {
        this.acceleration = initObj.acceleration
      }
      else {
        this.acceleration = 0.0;
      }
      if (initObj.hasOwnProperty('priority')) {
        this.priority = initObj.priority
      }
      else {
        this.priority = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type custom1
    // Serialize message field [x]
    bufferOffset = _serializer.float32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float32(obj.y, buffer, bufferOffset);
    // Serialize message field [z]
    bufferOffset = _serializer.float32(obj.z, buffer, bufferOffset);
    // Serialize message field [e1]
    bufferOffset = _serializer.float32(obj.e1, buffer, bufferOffset);
    // Serialize message field [e2]
    bufferOffset = _serializer.float32(obj.e2, buffer, bufferOffset);
    // Serialize message field [e3]
    bufferOffset = _serializer.float32(obj.e3, buffer, bufferOffset);
    // Serialize message field [e4]
    bufferOffset = _serializer.float32(obj.e4, buffer, bufferOffset);
    // Serialize message field [velocity]
    bufferOffset = _serializer.float32(obj.velocity, buffer, bufferOffset);
    // Serialize message field [acceleration]
    bufferOffset = _serializer.float32(obj.acceleration, buffer, bufferOffset);
    // Serialize message field [priority]
    bufferOffset = _serializer.bool(obj.priority, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type custom1
    let len;
    let data = new custom1(null);
    // Deserialize message field [x]
    data.x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z]
    data.z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [e1]
    data.e1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [e2]
    data.e2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [e3]
    data.e3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [e4]
    data.e4 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [velocity]
    data.velocity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [acceleration]
    data.acceleration = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [priority]
    data.priority = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 37;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/custom1';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '31d9aef80e7e38c1513be9d4decd01d5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x
    float32 y
    float32 z
    
    float32 e1
    float32 e2
    float32 e3
    float32 e4
    
    float32 velocity
    float32 acceleration
    bool priority
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new custom1(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.z !== undefined) {
      resolved.z = msg.z;
    }
    else {
      resolved.z = 0.0
    }

    if (msg.e1 !== undefined) {
      resolved.e1 = msg.e1;
    }
    else {
      resolved.e1 = 0.0
    }

    if (msg.e2 !== undefined) {
      resolved.e2 = msg.e2;
    }
    else {
      resolved.e2 = 0.0
    }

    if (msg.e3 !== undefined) {
      resolved.e3 = msg.e3;
    }
    else {
      resolved.e3 = 0.0
    }

    if (msg.e4 !== undefined) {
      resolved.e4 = msg.e4;
    }
    else {
      resolved.e4 = 0.0
    }

    if (msg.velocity !== undefined) {
      resolved.velocity = msg.velocity;
    }
    else {
      resolved.velocity = 0.0
    }

    if (msg.acceleration !== undefined) {
      resolved.acceleration = msg.acceleration;
    }
    else {
      resolved.acceleration = 0.0
    }

    if (msg.priority !== undefined) {
      resolved.priority = msg.priority;
    }
    else {
      resolved.priority = false
    }

    return resolved;
    }
};

module.exports = custom1;
