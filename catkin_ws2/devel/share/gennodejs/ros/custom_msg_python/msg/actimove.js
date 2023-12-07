// Auto-generated. Do not edit!

// (in-package custom_msg_python.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let blockdata = require('./blockdata.js');

//-----------------------------------------------------------

class actimove {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.block = null;
      this.humanprio = null;
      this.poscertainty = null;
      this.stabilety = null;
    }
    else {
      if (initObj.hasOwnProperty('block')) {
        this.block = initObj.block
      }
      else {
        this.block = new blockdata();
      }
      if (initObj.hasOwnProperty('humanprio')) {
        this.humanprio = initObj.humanprio
      }
      else {
        this.humanprio = 0.0;
      }
      if (initObj.hasOwnProperty('poscertainty')) {
        this.poscertainty = initObj.poscertainty
      }
      else {
        this.poscertainty = 0.0;
      }
      if (initObj.hasOwnProperty('stabilety')) {
        this.stabilety = initObj.stabilety
      }
      else {
        this.stabilety = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type actimove
    // Serialize message field [block]
    bufferOffset = blockdata.serialize(obj.block, buffer, bufferOffset);
    // Serialize message field [humanprio]
    bufferOffset = _serializer.float32(obj.humanprio, buffer, bufferOffset);
    // Serialize message field [poscertainty]
    bufferOffset = _serializer.float32(obj.poscertainty, buffer, bufferOffset);
    // Serialize message field [stabilety]
    bufferOffset = _serializer.float32(obj.stabilety, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type actimove
    let len;
    let data = new actimove(null);
    // Deserialize message field [block]
    data.block = blockdata.deserialize(buffer, bufferOffset);
    // Deserialize message field [humanprio]
    data.humanprio = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [poscertainty]
    data.poscertainty = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [stabilety]
    data.stabilety = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/actimove';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '02dcd61482d1dd9838c30c59b919c3b8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    custom_msg_python/blockdata block
    float32 humanprio
    float32 poscertainty
    float32 stabilety
    
    ================================================================================
    MSG: custom_msg_python/blockdata
    int32 xlen
    int32 ylen
    int32 zlen
    
    float32 xpos
    float32 ypos
    float32 zpos
    
    int32 rotation
    
    int32 blocktype
    int32 blockcolor
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new actimove(null);
    if (msg.block !== undefined) {
      resolved.block = blockdata.Resolve(msg.block)
    }
    else {
      resolved.block = new blockdata()
    }

    if (msg.humanprio !== undefined) {
      resolved.humanprio = msg.humanprio;
    }
    else {
      resolved.humanprio = 0.0
    }

    if (msg.poscertainty !== undefined) {
      resolved.poscertainty = msg.poscertainty;
    }
    else {
      resolved.poscertainty = 0.0
    }

    if (msg.stabilety !== undefined) {
      resolved.stabilety = msg.stabilety;
    }
    else {
      resolved.stabilety = 0.0
    }

    return resolved;
    }
};

module.exports = actimove;
