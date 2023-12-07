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

class custom {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.configurationmode = null;
    }
    else {
      if (initObj.hasOwnProperty('configurationmode')) {
        this.configurationmode = initObj.configurationmode
      }
      else {
        this.configurationmode = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type custom
    // Serialize message field [configurationmode]
    bufferOffset = _serializer.bool(obj.configurationmode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type custom
    let len;
    let data = new custom(null);
    // Deserialize message field [configurationmode]
    data.configurationmode = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/custom';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '63b9c1c4bde05e435d92eaf6475fe3c0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    bool configurationmode
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new custom(null);
    if (msg.configurationmode !== undefined) {
      resolved.configurationmode = msg.configurationmode;
    }
    else {
      resolved.configurationmode = false
    }

    return resolved;
    }
};

module.exports = custom;
