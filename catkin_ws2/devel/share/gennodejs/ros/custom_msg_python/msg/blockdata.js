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

class blockdata {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.xlen = null;
      this.ylen = null;
      this.zlen = null;
      this.xpos = null;
      this.ypos = null;
      this.zpos = null;
      this.rotation = null;
      this.blocktype = null;
      this.blockcolor = null;
    }
    else {
      if (initObj.hasOwnProperty('xlen')) {
        this.xlen = initObj.xlen
      }
      else {
        this.xlen = 0;
      }
      if (initObj.hasOwnProperty('ylen')) {
        this.ylen = initObj.ylen
      }
      else {
        this.ylen = 0;
      }
      if (initObj.hasOwnProperty('zlen')) {
        this.zlen = initObj.zlen
      }
      else {
        this.zlen = 0;
      }
      if (initObj.hasOwnProperty('xpos')) {
        this.xpos = initObj.xpos
      }
      else {
        this.xpos = 0.0;
      }
      if (initObj.hasOwnProperty('ypos')) {
        this.ypos = initObj.ypos
      }
      else {
        this.ypos = 0.0;
      }
      if (initObj.hasOwnProperty('zpos')) {
        this.zpos = initObj.zpos
      }
      else {
        this.zpos = 0.0;
      }
      if (initObj.hasOwnProperty('rotation')) {
        this.rotation = initObj.rotation
      }
      else {
        this.rotation = 0;
      }
      if (initObj.hasOwnProperty('blocktype')) {
        this.blocktype = initObj.blocktype
      }
      else {
        this.blocktype = 0;
      }
      if (initObj.hasOwnProperty('blockcolor')) {
        this.blockcolor = initObj.blockcolor
      }
      else {
        this.blockcolor = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type blockdata
    // Serialize message field [xlen]
    bufferOffset = _serializer.int32(obj.xlen, buffer, bufferOffset);
    // Serialize message field [ylen]
    bufferOffset = _serializer.int32(obj.ylen, buffer, bufferOffset);
    // Serialize message field [zlen]
    bufferOffset = _serializer.int32(obj.zlen, buffer, bufferOffset);
    // Serialize message field [xpos]
    bufferOffset = _serializer.float32(obj.xpos, buffer, bufferOffset);
    // Serialize message field [ypos]
    bufferOffset = _serializer.float32(obj.ypos, buffer, bufferOffset);
    // Serialize message field [zpos]
    bufferOffset = _serializer.float32(obj.zpos, buffer, bufferOffset);
    // Serialize message field [rotation]
    bufferOffset = _serializer.int32(obj.rotation, buffer, bufferOffset);
    // Serialize message field [blocktype]
    bufferOffset = _serializer.int32(obj.blocktype, buffer, bufferOffset);
    // Serialize message field [blockcolor]
    bufferOffset = _serializer.int32(obj.blockcolor, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type blockdata
    let len;
    let data = new blockdata(null);
    // Deserialize message field [xlen]
    data.xlen = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [ylen]
    data.ylen = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [zlen]
    data.zlen = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [xpos]
    data.xpos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ypos]
    data.ypos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [zpos]
    data.zpos = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rotation]
    data.rotation = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [blocktype]
    data.blocktype = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [blockcolor]
    data.blockcolor = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_python/blockdata';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eac9cc71fe8df90f9f784800602aae10';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new blockdata(null);
    if (msg.xlen !== undefined) {
      resolved.xlen = msg.xlen;
    }
    else {
      resolved.xlen = 0
    }

    if (msg.ylen !== undefined) {
      resolved.ylen = msg.ylen;
    }
    else {
      resolved.ylen = 0
    }

    if (msg.zlen !== undefined) {
      resolved.zlen = msg.zlen;
    }
    else {
      resolved.zlen = 0
    }

    if (msg.xpos !== undefined) {
      resolved.xpos = msg.xpos;
    }
    else {
      resolved.xpos = 0.0
    }

    if (msg.ypos !== undefined) {
      resolved.ypos = msg.ypos;
    }
    else {
      resolved.ypos = 0.0
    }

    if (msg.zpos !== undefined) {
      resolved.zpos = msg.zpos;
    }
    else {
      resolved.zpos = 0.0
    }

    if (msg.rotation !== undefined) {
      resolved.rotation = msg.rotation;
    }
    else {
      resolved.rotation = 0
    }

    if (msg.blocktype !== undefined) {
      resolved.blocktype = msg.blocktype;
    }
    else {
      resolved.blocktype = 0
    }

    if (msg.blockcolor !== undefined) {
      resolved.blockcolor = msg.blockcolor;
    }
    else {
      resolved.blockcolor = 0
    }

    return resolved;
    }
};

module.exports = blockdata;
